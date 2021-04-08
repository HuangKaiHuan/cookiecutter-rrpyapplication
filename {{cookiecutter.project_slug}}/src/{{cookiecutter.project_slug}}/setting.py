import os
import sys
from pathlib import Path

_DEFAULT_PROJECT_ROOT = Path(
    getattr(sys, "_MEIPASS", Path(__file__).parent.parent.parent)
)
_DEFAULT_LIB_PATH = _DEFAULT_PROJECT_ROOT.joinpath("lib")
_DEFAULT_INPUT_PATH = _DEFAULT_PROJECT_ROOT.joinpath("data")
_DEFAULT_OUTPUT_PATH = Path().home().joinpath(".nameless")

PROJECT_ROOT = Path(os.environ.get("DEFAULT_PROJECT_ROOT", _DEFAULT_PROJECT_ROOT))
LIB_PATH = Path(os.environ.get("LIB_PATH", _DEFAULT_LIB_PATH))
INPUT_PATH = Path(os.environ.get("INPUT_PATH", _DEFAULT_INPUT_PATH))
OUTPUT_PATH = Path(os.environ.get("OUTPUT_PATH", _DEFAULT_OUTPUT_PATH))

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

CHANGE_LOG_PATH = PROJECT_ROOT.joinpath("CHANGELOG.rst")
