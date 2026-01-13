from dataclasses import dataclass
from datetime import datetime


@dataclass
class HealerLogEntry:
    component_id: str
    old_key: str
    new_key: str
    reason: str
    confidence: float
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
