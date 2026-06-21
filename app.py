"""Root entrypoint for simple local execution.
Run: uvicorn app:app --reload
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from agriops.main import app  # noqa: E402
