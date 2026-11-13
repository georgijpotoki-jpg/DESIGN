


def get_available_characters() -> list[dict]:
    """Стаб: повертає список доступних персонажів."""
    return [
        {
            "id": 1,
            "name": "Артур",
            "class": "Лицар",
            "hp": 120,
            "desc": "Високий захист, сильний у ближньому бою.",
        },
        {
            "id": 2,
            "name": "Ліра",
            "class": "Маг",
            "hp": 80,
            "desc": "Висока магічна шкода, але низьке здоров'я.",
        },
        {
            "id": 3,
            "name": "Тінь",
            "class": "Розвідник",
            "hp": 100,
            "desc": "Швидкий та спритний, має шанс уникнути удару.",
        },
    ]


def process_game_action(state: dict, action: str) -> tuple[dict, str]:
    """Стаб: обробляє дію гравця та повертає новий стан і опис події."""
    state["turn"] += 1

    if action == "explore":
        state["score"] += 10
        message = (
            "[Стаб події]: Ви дослідили темний коридор і знайшли стародавню"
            " монету! (+10 очок)"
        )
    elif action == "fight":
        state["hp"] -= 15
        state["score"] += 25
        message = (
            "[Стаб події]: Ви зустріли гобліна! Бій був важким: ви втратили 15"
            " HP, але перемогли (+25 очок)."
        )
    else:
        message = "[Стаб події]: Нічого не сталося."

    if state["hp"] <= 0:
        state["is_game_over"] = True
        message += "\nВаше здоров'я впало до нуля. Гра завершена!"
    elif state["turn"] >= 5:
        state["is_game_over"] = True
        message += "\nВітаємо! Ви успішно пройшли демо-рівень гри!"

    return state, message
