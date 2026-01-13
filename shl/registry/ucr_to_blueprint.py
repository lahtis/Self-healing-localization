import json
from pathlib import Path


def ucr_to_blueprint(ucr_path: str | Path, output_path: str | Path):
    """
    Converts a UCR JSON file back into a UI Blueprint JSON file.
    - UCR: strict, SHL-internal registry format
    - Blueprint: human-friendly, semantic, purpose-driven
    """

    ucr_path = Path(ucr_path)
    output_path = Path(output_path)

    with open(ucr_path, "r", encoding="utf-8") as f:
        ucr = json.load(f)

    blueprint = {
        "components": {}
    }

    for comp_id, comp_data in ucr.get("components", {}).items():
        original_framework_map = comp_data.get("framework_map", {})
        healer_map = original_framework_map.get("Healer")

        framework_map = dict(original_framework_map)
        framework_map.pop("Healer", None)

        bp_entry = {
            "type": comp_data.get("type"),
            "text_keys": comp_data.get("text_keys", {}),
            "framework_map": framework_map
        }

        # Extract healer_key
        if healer_map and "selector" in healer_map:
            bp_entry["healer_key"] = healer_map["selector"]

        # Extract user_key if present
        if "user_key" in comp_data:
            bp_entry["user_key"] = comp_data["user_key"]

        # Optional: data binding
        if "data_binding" in comp_data:
            bp_entry["data_binding"] = comp_data["data_binding"]

        blueprint["components"][comp_id] = bp_entry

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(blueprint, f, indent=2, ensure_ascii=False)

    return output_path
