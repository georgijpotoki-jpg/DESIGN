import json
import os

SAVE_FILE = "save_data.json"


def save_game(state: dict) -> bool:
    """Зберігає поточний стан гри у JSON-файл."""
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=4)
        return True
    except IOError:
        return False


def load_game() -> dict | None:
    """Завантажує стан гри з JSON-файлу, якщо він існує."""
    if not os.path.exists(SAVE_FILE):
        return None
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        return None
