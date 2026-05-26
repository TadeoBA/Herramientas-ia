import json
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
_CONFIG_PATH = _PROJECT_ROOT / "01-planning" / "config_compliance.json"


def load_compliance_config() -> dict:
    """Carga la configuración de cumplimiento desde config_compliance.json."""
    if not _CONFIG_PATH.is_file():
        raise FileNotFoundError(
            f"No se encontró el archivo de configuración: {_CONFIG_PATH}"
        )

    with _CONFIG_PATH.open(encoding="utf-8") as archivo:
        return json.load(archivo)
