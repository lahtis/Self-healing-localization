from copy import deepcopy
from typing import Any, Dict, List

from shl.diff.blueprint_change import (
    BlueprintChange,
    ChangeType,
)


def patch_blueprint_safe(
    blueprint: Dict[str, Any],
    changes: List[BlueprintChange],
    *,
    min_confidence: float = 0.75,
):
    patched = deepcopy(blueprint)

    report = {
        "applied": [],
        "skipped": [],
    }

    for change in changes:
        # --- Confidence gate ---
        if change.confidence is not None and change.confidence < min_confidence:
            report["skipped"].append({
                "change": change,
                "reason": "confidence_too_low",
            })
            continue

        # --- Component-level ---
        if change.field == "__component__":
            if change.change_type == ChangeType.ADDED:
                patched.setdefault("components", {})[change.component_id] = change.new_value
                report["applied"].append(change)
            else:
                # REMOVED not allowed in safe mode
                report["skipped"].append({
                    "change": change,
                    "reason": "component_removal_not_allowed_in_safe_mode",
                })
            continue

        # --- Field-level ---
        ok = _apply_field_change(
            patched,
            change,
        )

        if ok:
            report["applied"].append(change)
        else:
            report["skipped"].append({
                "change": change,
                "reason": "invalid_path",
            })

    return patched, report

def _apply_field_change(
    blueprint: Dict[str, Any],
    change: BlueprintChange,
) -> bool:
    try:
        comp = blueprint["components"][change.component_id]
    except KeyError:
        return False

    parts = change.field.split(".")
    target = comp

    for key in parts[:-1]:
        if key not in target or not isinstance(target[key], dict):
            return False
        target = target[key]

    last = parts[-1]

    if change.change_type == ChangeType.ADDED:
        target[last] = change.new_value
    elif change.change_type == ChangeType.CHANGED:
        target[last] = change.new_value
    elif change.change_type == ChangeType.REMOVED:
        # Safe mode: allow field removal, but not component removal
        target.pop(last, None)

    return True
