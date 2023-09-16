import argparse
import json
import os
import tempfile


def get_storage_path():
    # Создаем временную директорию и возвращаем путь к файлу хранилища
    storage_directory = tempfile.gettempdir()
    storage_path = os.path.join(storage_directory, 'storage.data')
    return storage_path


def read_data():
    # Чтение данных из файла хранилища
    storage_path = get_storage_path()
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = {}

    return data


def write_data(data):
    # Запись данных в файл хранилища
    storage_path = get_storage_path()
    with open(storage_path, 'w') as file:
        json.dump(data, file)


def add_value(key, value):
    data = read_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]
    write_data(data)


def get_values(key):
    data = read_data()
    return data.get(key, [])


def main():
    parser = argparse.ArgumentParser(description="Key-Value Storage")
    parser.add_argument("--key", type=str, help="Key for storing/retrieving values")
    parser.add_argument("--val", type=str, help="Value to be stored")

    args = parser.parse_args()

    if args.key:
        if args.val:
            add_value(args.key, args.val)
        else:
            values = get_values(args.key)
            if values:
                print(", ".join(values))
            else:
                print("None")
    else:
        print("Key argument is required.")


if __name__ == "__main__":
    main()
