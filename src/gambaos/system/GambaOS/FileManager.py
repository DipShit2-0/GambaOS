import os, sys
from pathlib import Path

base = Path(__file__).resolve().parent
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, f"../../{relative_path}")
    return os.path.join(base, f"../../{relative_path}")