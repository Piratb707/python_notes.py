import os


def create_note():
    """
    Создает новую заметку.

    Returns:
        str: Строка с данными заметки.
    """
    title = input("Введите заголовок заметки: ")
    content = input("Введите текст заметки: ")
    note = f"Заголовок: {title}\n{content}\n"
    return note


def save_note(note):
    """
    Сохраняет заметку в файл.

    Args:
        note (str): Строка с данными заметки.
    """
    with open("notes.txt", "a") as file:
        file.write(note)
    print("Заметка сохранена.")


def read_notes():
    """
    Читает список заметок из файла и выводит на экран.
    """
    if not os.path.exists("notes.txt"):
        print("Файл заметок не найден.")
        return

    with open("notes.txt", "r") as file:
        notes = file.read()
    print("Список заметок:")
    print(notes)


def edit_note():
    """
    Редактирует существующую заметку.

    Note:
        Для редактирования заметки необходимо знать ее номер в списке.

    """
    note_number = int(input("Введите номер заметки для редактирования: "))
    with open("notes.txt", "r") as file:
        lines = file.readlines()

    if note_number <= len(lines) // 3:
        note_index = (note_number - 1) * 3
        title = input("Введите новый заголовок заметки: ")
        content = input("Введите новый текст заметки: ")
        lines[note_index] = f"Заголовок: {title}\n"
        lines[note_index + 1] = f"{content}\n"

        with open("notes.txt", "w") as file:
            file.writelines(lines)
        print("Заметка отредактирована.")
    else:
        print("Заметка не найдена.")


def delete_note():
    """
    Удаляет существующую заметку.

    Note:
        Для удаления заметки необходимо знать ее номер в списке.
    """
    note_number = int(input("Введите номер заметки для удаления: "))
    with open("notes.txt", "r") as file:
        lines = file.readlines()

    if note_number <= len(lines) // 3:
        note_index = (note_number - 1) * 3
        del lines[note_index:note_index + 3]

        with open("notes.txt", "w") as file:
            file.writelines(lines)
        print("Заметка удалена.")
    else:
        print("Заметка не найдена.")


while True:
    print("1. Создать заметку")
    print("2. Просмотреть список заметок")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        note = create_note()
        save_note(note)
    elif choice == "2":
        read_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите снова.")
