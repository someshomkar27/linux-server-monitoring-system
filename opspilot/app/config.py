import json, os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CONFIG_PATH=ROOT/os.getenv("OPSPILOT_CONFIG","config/config.json")
DB_PATH=ROOT/os.getenv("OPSPILOT_DB","data/opspilot.db")
def load_config(): return json.loads(CONFIG_PATH.read_text())
