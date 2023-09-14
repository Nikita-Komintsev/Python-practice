import argparse
import json
import os
import tempfile

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def load_data():
    if not os.path.exists(storage_path):
        return {}
    with open(storage_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = {}
    return data

def save_data(data):
    with open(storage_path, 'w') as file:
        json.dump(data, file)

def add_value(key, value):
    data = load_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]
    save_data(data)

def get_values(key):
    data = load_data()
    return data.get(key, [])


parser = argparse.ArgumentParser()
parser.add_argument('--key', help='Ключ')
parser.add_argument('--val', help='Значение')
args = parser.parse_args()

if args.key and args.val:
    add_value(args.key, args.val)
elif args.key:
    values = get_values(args.key)
    print(', '.join(values))
