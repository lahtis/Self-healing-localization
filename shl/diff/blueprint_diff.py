from dataclasses import dataclass
from typing import Any


class ChangeType:
    ADDED = "added"
    REMOVED = "removed"
    CHANGED = "changed"


class ChangeReason:
    HEALER = "healer_update"
    MANUAL = "manual_edit"
    NORMALIZATION = "normalization"
    UNKNOWN = "unknown"


@dataclass
class BlueprintChange:
    component_id: str
    field: str
    old_value: Any
    new_value: Any
    change_type: str   # added | removed | changed
    reason: str        # healer_update | manual_edit | normalization | unknown
    confidence: float | None = None

    def __post_init__(self):
        assert self.change_type in (
            ChangeType.ADDED,
            ChangeType.REMOVED,
            ChangeType.CHANGED,
        ), f"Invalid change_type: {self.change_type}"

        assert self.reason in (
            ChangeReason.HEALER,
            ChangeReason.MANUAL,
            ChangeReason.NORMALIZATION,
            ChangeReason.UNKNOWN,
        ), f"Invalid reason: {self.reason}"
