from pathlib import Path
import json

records_file = Path(__file__).resolve().parent / "records.json"

default_records = {
    "Easy": 10,
    "Medium": 5,
    "Hard": 3
}

def load_records():
    if not records_file.exists():
        return default_records

    try:
        with open(records_file, 'r') as ff:
            return json.load(ff)
    except (json.JSONDecodeError, FileNotFoundError):
        return default_records

def save_records(records):
    with open(records_file, "w") as ff:
        json.dump(records, ff, indent=4)

