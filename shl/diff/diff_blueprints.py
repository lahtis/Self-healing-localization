"""
File: diff_blueprints.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
Compares two SHL blueprints and produces a list of component additions, 
removals, and field modifications as BlueprintChange objects.

Vertaa kahta SHL‑blueprinttia ja tuottaa listan komponenttien lisäys‑, 
poisto‑ ja kenttämuutoksista BlueprintChange‑olioina.
"""
from typing import Any, Dict, List
from shl.diff.blueprint_change import (
    BlueprintChange,
    ChangeType,
    ChangeReason,
)

def infer_confidence(old: Any, new: Any) -> float:
    if old is None or new is None:
        return 0.9
    return 0.7


def diff_blueprints(
    old_bp: Dict[str, Any],
    new_bp: Dict[str, Any],
    *,
    reason: str = ChangeReason.UNKNOWN,
    confidence: float | None = None,
) -> List[BlueprintChange]:
    changes: List[BlueprintChange] = []

    old_components = old_bp.get("components", {})
    new_components = new_bp.get("components", {})

    # -------------------------
    # Component-level diff
    # -------------------------
    all_component_ids = set(old_components) | set(new_components)

    for comp_id in all_component_ids:
        old_comp = old_components.get(comp_id)
        new_comp = new_components.get(comp_id)

        # Component added
        if old_comp is None:
            changes.append(
                BlueprintChange(
                    component_id=comp_id,
                    field="__component__",
                    old_value=None,
                    new_value=new_comp,
                    change_type=ChangeType.ADDED,
                    reason=reason,
                    confidence=confidence if confidence is not None else infer_confidence(None, new_comp),

                )
            )
            continue

        # Component removed
        if new_comp is None:
            changes.append(
                BlueprintChange(
                    component_id=comp_id,
                    field="__component__",
                    old_value=old_comp,
                    new_value=None,
                    change_type=ChangeType.REMOVED,
                    reason=reason,
                    confidence=confidence if confidence is not None else infer_confidence(old_comp, None),
                )
            )
            continue

        # Component exists in both → diff fields
        _diff_dict(
            comp_id=comp_id,
            old=old_comp,
            new=new_comp,
            path="",
            changes=changes,
            reason=reason,
            confidence=confidence,
        )

    return changes

def _diff_dict(
    *,
    comp_id: str,
    old: Dict[str, Any],
    new: Dict[str, Any],
    path: str,
    changes: List[BlueprintChange],
    reason: str,
    confidence: float | None,
):
    all_keys = set(old) | set(new)

    for key in all_keys:
        old_val = old.get(key)
        new_val = new.get(key)

        field_path = f"{path}.{key}" if path else key

        # Added field
        if key not in old:
            conf = confidence if confidence is not None else infer_confidence(None, new_val)

            changes.append(
                BlueprintChange(
                    component_id=comp_id,
                    field=field_path,
                    old_value=None,
                    new_value=new_val,
                    change_type=ChangeType.ADDED,
                    reason=reason,
                    confidence=conf,
                )
            )
            continue

        # Removed field
        if key not in new:
            conf = confidence if confidence is not None else infer_confidence(old_val, None)

            changes.append(
                BlueprintChange(
                    component_id=comp_id,
                    field=field_path,
                    old_value=old_val,
                    new_value=None,
                    change_type=ChangeType.REMOVED,
                    reason=reason,
                    confidence=conf,
                )
            )
            continue

        # Both exist
        if isinstance(old_val, dict) and isinstance(new_val, dict):
            _diff_dict(
                comp_id=comp_id,
                old=old_val,
                new=new_val,
                path=field_path,
                changes=changes,
                reason=reason,
                confidence=confidence,
            )
        elif old_val != new_val:
            conf = confidence if confidence is not None else infer_confidence(old_val, new_val)

            changes.append(
                BlueprintChange(
                    component_id=comp_id,
                    field=field_path,
                    old_value=old_val,
                    new_value=new_val,
                    change_type=ChangeType.CHANGED,
                    reason=reason,
                    confidence=conf,
                )
            )

