import os
import json

def save_message(message_data):
    filename = "json/messages.json"

    try:
        # Всегда начинаем с пустого списка если есть ошибки
        messages = []

        # Пытаемся прочитать существующие данные
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if content:  # Если файл не пустой
                    messages = json.loads(content)

        # Добавляем новое сообщение (структурированные данные)
        messages.append(message_data)

        # Сохраняем обратно
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(messages, f, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f"Ошибка при сохранении: {e}")
        # Создаем файл с одним сообщением
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([message_data], f, ensure_ascii=False, indent=4)


def load_messages():
    filename = "json/messages.json"
    try:
        # Проверяем существование файла
        if not os.path.exists(filename):
            print("Файл не существует")
            return []

        # Пытаемся прочитать существующие данные
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:  # Если файл пустой
                print("Файл пустой")
                return []

            # Загружаем JSON данные
            messages = json.loads(content)
            print(f"Успешно загружено {len(messages)} объявлений")
            return messages

    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON: {e}")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []