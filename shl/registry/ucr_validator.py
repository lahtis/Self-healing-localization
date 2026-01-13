import json
from pathlib import Path
from jsonschema import validate, ValidationError, SchemaError


def validate_ucr(ucr_path: str | Path, schema_path: str | Path) -> bool:
    """
    Validates a UCR JSON file against the UCR schema.

    Raises:
        ValidationError: if UCR data is invalid
        RuntimeError: if the schema itself is invalid
    """

    ucr_path = Path(ucr_path)
    schema_path = Path(schema_path)

    with open(ucr_path, "r", encoding="utf-8") as f:
        ucr_data = json.load(f)

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    try:
        validate(instance=ucr_data, schema=schema)
        return True

    except ValidationError as e:
        path = ".".join(str(p) for p in e.absolute_path) or "<root>"
        raise ValidationError(
            f"UCR validation failed at '{path}': {e.message}"
        ) from e

    except SchemaError as e:
        raise RuntimeError(
            "UCR schema is invalid. This is a developer error."
        ) from e
