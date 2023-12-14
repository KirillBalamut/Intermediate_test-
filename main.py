# Промежуточная контрольная работа по блоку специализация
# Урок 1. Приложение заметки (Python)
# Напишите проект, содержащий функционал работы с заметками. Программа должна уметь создавать заметку, 
# сохранять её, читать список заметок, редактировать заметку, удалять заметку.
import json
import datetime

def create_note():
    title = input("Введите заголовок заметки: ")
    message = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": message,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes()

def read_notes():
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['message']}")
        print(f"Дата/время: {note['timestamp']}")
        print()

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            print("Выберите, что вы хотите изменить:")
            print("1. Название заметки")
            print("2. Содержимое заметки")
            choice = input("Введите номер выбранной команды: ")
            if choice == "1":
                title = input("Введите новое название заметки: ")
                note['title'] = title
            elif choice == "2":
                message = input("Введите новое содержимое заметки: ")
                note['message'] = message
            else:
                print("Некорректная команда.")
                return
            note['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes()
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes()
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным ID не найдена.")

def filter_notes():
    date_str = input("Введите дату (гггг-мм-дд): ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        filtered_notes = [note for note in notes if datetime.datetime.strptime(note['timestamp'], "%Y-%m-%d %H:%M:%S") > date]
        if filtered_notes:
            print("Заметки после указанной даты:")
            for note in filtered_notes:
                print(f"ID: {note['id']}")
                print(f"Заголовок: {note['title']}")
                print(f"Текст: {note['message']}")
                print(f"Дата/время: {note['timestamp']}")
                print()
        else:
            print("Нет заметок после указанной даты.")
    except ValueError:
        print("Некорректный формат даты.")

def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def load_notes():
    try:
        with open("notes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    global notes
    notes = load_notes()
    while True:
        command = input("Введите команду (add, read, edit, delete, filter, exit): ")
        if command == "add":
            create_note()
        elif command == "read":
            read_notes()
        elif command == "edit":
            edit_note()
        elif command == "delete":
            delete_note()
        elif command == "filter":
            filter_notes()
        elif command == "exit":
            break
        else:
            print("Некорректная команда.")

if __name__ == "__main__":
    main()