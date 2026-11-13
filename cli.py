from game_engine import get_available_characters, process_game_action
from storage import load_game, save_game


def print_header(title: str):
    print("\n" + "=" * 45)
    print(f" {title.upper()}")
    print("=" * 45)


def select_character() -> dict | None:
    """Діалог вибору персонажа."""
    print_header("Вибір персонажа")
    characters = get_available_characters()

    for idx, char in enumerate(characters, start=1):
        print(
            f"[{idx}] {char['name']} ({char['class']}) | HP: {char['hp']} -"
            f" {char['desc']}"
        )
    print("[0] Назад до головного меню")

    while True:
        choice = input("\nВведіть номер персонажа: ").strip()
        if choice == "0":
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(characters):
            selected = characters[int(choice) - 1]
            return {
                "character_name": selected["name"],
                "character_class": selected["class"],
                "hp": selected["hp"],
                "score": 0,
                "turn": 1,
                "is_game_over": False,
            }
        print("Помилка: введіть коректний номер зі списку.")


def game_loop(state: dict):
    """Основний цикл текстової гри."""
    print_header(f"Гра почалася! Герой: {state['character_name']}")

    while not state["is_game_over"]:
        print(
            f"\n--- Хід #{state['turn']} | HP: {state['hp']} | Рахунок:"
            f" {state['score']} ---"
        )
        print("Оберіть дію:")
        print("[1] Дослідити локацію")
        print("[2] Вступити в бій")
        print("[3] Зберегти гру")
        print("[0] Вийти в головне меню")

        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            state, msg = process_game_action(state, "explore")
            print(f"\n>> {msg}")
        elif choice == "2":
            state, msg = process_game_action(state, "fight")
            print(f"\n>> {msg}")
        elif choice == "3":
            if save_game(state):
                print("\n>> [Система]: Прогрес успішно збережено!")
            else:
                print("\n>> [Система]: Помилка при збереженні файлу.")
        elif choice == "0":
            print("\nПовернення до головного меню...")
            return
        else:
            print("\nНевідома команда. Спробуйте ще раз.")

    print_header("Підсумки гри")
    print(f"Персонаж: {state['character_name']} ({state['character_class']})")
    print(f"Фінальний рахунок: {state['score']}")
    save_game(state)
    input("\nНатисніть Enter, щоб повернутися в головне меню...")


def run_cli():
    """Головне меню програми."""
    while True:
        print_header("Текстова RPG - Головне меню")
        print("[1] Почати нову гру")
        print("[2] Завантажити збережену гру")
        print("[0] Вихід")

        choice = input("\nОберіть пункт меню: ").strip()

        if choice == "1":
            initial_state = select_character()
            if initial_state:
                game_loop(initial_state)
        elif choice == "2":
            saved_state = load_game()
            if saved_state:
                if saved_state.get("is_game_over"):
                    print(
                        "\n>> Остання збережена гра вже завершена (Рахунок:"
                        f" {saved_state['score']}). Почніть нову!"
                    )
                else:
                    print("\n>> Збереження успішно завантажено!")
                    game_loop(saved_state)
            else:
                print("\n>> Збережених ігор не знайдено.")
        elif choice == "0":
            print("\nДякуємо за гру! До побачення.")
            break
        else:
            print("\nПомилка вводу. Оберіть 1, 2 або 0.")
