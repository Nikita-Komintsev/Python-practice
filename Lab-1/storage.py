import argparse
import json
import tempfile

# Создаем парсер аргументов командной строки
parser = argparse.ArgumentParser()
parser.add_argument('--key', help='Имя ключа')
parser.add_argument('--val', help='Значение')
args = parser.parse_args()

# Открываем или создаем временный файл хранилища
storage_file = tempfile.NamedTemporaryFile(mode='a+', delete=False)
storage_file.close()

# Читаем данные из временного файла
with open(storage_file.name, 'r+') as file:
    try:
        storage_data = json.load(file)
    except json.decoder.JSONDecodeError:
        storage_data = {}

    # Если переданы оба ключа, добавляем значение по ключу и сохраняем данные в файл
    if args.key and args.val:
        if args.key in storage_data:
            storage_data[args.key].append(args.val)
        else:
            storage_data[args.key] = [args.val]
        file.seek(0)
        json.dump(storage_data, file)
    # Если передано только имя ключа, выводим значения по ключу из файла
    elif args.key:
        values = storage_data.get(args.key)
        if values:
            print(', '.join(values))
        else:
            print(None)
    # Если не передано ни одного аргумента, выводим данные из файла
    else:
        file.seek(0)
        print(file.read())
