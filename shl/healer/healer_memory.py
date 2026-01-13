import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from datetime import datetime


@dataclass
class HealerMemory:
    text_success: int = 0
    text_fail: int = 0

    type_success: int = 0
    type_fail: int = 0

    context_success: int = 0
    context_fail: int = 0

    selector_history: list = field(default_factory=list)

    # -----------------------------
    #  Learning updates
    # -----------------------------
    def record_success(self, method: str, selector: str | None):
        setattr(self, f"{method}_success", getattr(self, f"{method}_success") + 1)
        if selector:
            self.selector_history.append(selector)

    def record_fail(self, method: str):
        setattr(self, f"{method}_fail", getattr(self, f"{method}_fail") + 1)

    def confidence(self, method: str) -> float:
        s = getattr(self, f"{method}_success")
        f = getattr(self, f"{method}_fail")
        total = s + f
        return s / total if total > 0 else 0.5

    # -----------------------------
    #  Persistence (save/load)
    # -----------------------------
    def save(self, path: str | Path):
        path = Path(path)

        # Create directory if missing
        path.parent.mkdir(parents=True, exist_ok=True)

        # If file exists, archive it
        if path.exists():
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            archive_path = path.parent / f"memory_{timestamp}.json"
            path.rename(archive_path)

        # Save new memory.json
        with open(path, "w", encoding="utf-8") as f:
            json.dump(asdict(self), f, indent=2, ensure_ascii=False)


    @classmethod
    def load(cls, path: str | Path):
        path = Path(path)
        if not path.exists():
            return cls()  # return empty memory

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return cls(**data)
