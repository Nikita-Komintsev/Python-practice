import aiohttp
import asyncio
import argparse
import json
import csv


def write_lab_data_to_csv(labs_data, file_name):
    if isinstance(labs_data, dict):
        labs_data = [labs_data]

    with open(f'{file_name}.csv', mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Название'] + [lab['name'] for lab in labs_data]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        all_students = set()
        for lab in labs_data:
            students = lab.get('students', '').split(',')
            if students and any(name.strip() for name in students):
                all_students.update(students)

        for key in ['Дедлайн', 'Описание'] + list(all_students):
            row_data = {'Название': key}
            for lab in labs_data:
                if key == 'Дедлайн':
                    row_data[lab['name']] = lab.get('deadline', '')
                elif key == 'Описание':
                    row_data[lab['name']] = lab.get('description', '')
                else:
                    row_data[lab['name']] = '+' if key in lab.get('students', '').split(',') else ''

            writer.writerow(row_data)


async def print_response(response):
    print(f"Status: {response.status}")
    location_header = response.headers.get('Location', '')
    if len(location_header):
        print(f'URL:{location_header}')
    text = await response.text()
    if text:
        print(text)


async def add_lab(url, lab, deadline, description):
    async with aiohttp.ClientSession() as session:
        request = {'name': lab, 'deadline': deadline, 'description': description}
        async with session.post(url=f"{url}/labs", data=json.dumps(request)) as response:
            await print_response(response)


async def update_lab(url, lab, deadline, description, students):
    async with aiohttp.ClientSession() as session:
        request = {}
        if deadline is not None:
            request['deadline'] = deadline
        if description is not None:
            request['description'] = description
        if students is not None:
            request['students'] = students

        async with session.patch(url=f"{url}/labs/{lab}", data=json.dumps(request)) as response:
            await print_response(response)


async def delete_lab(url, lab):
    async with aiohttp.ClientSession() as session:
        async with session.delete(url=f"{url}/labs/{lab}") as response:
            await print_response(response)


async def get_lab(url, name):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=f"{url}/labs/{name}") as response:
            await print_response(response)
            if response.status == 200:
                try:
                    data = await response.json()
                    write_lab_data_to_csv(data, name)
                except Exception as ex:
                    print(ex)


async def get_all(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=f"{url}/labs") as response:
            await print_response(response)
            try:
                data = await response.json()
                write_lab_data_to_csv(data, 'all_info_labs')
            except Exception as ex:
                print(ex)


async def process_cli_args(cli_args):
    url = 'http://0.0.0.0:8080'

    if cli_args.add and not cli_args.deadline:
        print("Deadline is required (--deadline)")
    elif cli_args.add and cli_args.deadline:
        description = cli_args.description if hasattr(cli_args, 'description') else None
        await add_lab(url, cli_args.add, cli_args.deadline, description)

    if cli_args.update and not (cli_args.deadline or cli_args.description or cli_args.students):
        print("Required --deadline --description or --students")
    elif cli_args.update:
        await update_lab(url, cli_args.update, cli_args.deadline, cli_args.description, cli_args.students)

    if cli_args.delete:
        await delete_lab(url, cli_args.delete)

    if cli_args.get_lab:
        await get_lab(url, cli_args.get_lab)

    if cli_args.get_all:
        await get_all(url)


parser = argparse.ArgumentParser()

parser.add_argument('--deadline', type=str, help="Deadline of laboratory - day.month.year")
parser.add_argument('--description', type=str, help="Description of laboratory")
parser.add_argument('--students', type=str, help="Students who completed the laboratory")

group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('--add', type=str, help="adding laboratory")

group.add_argument('--update', type=str, help="updating fields")

group.add_argument('--delete', type=str, help="delete laboratory")

group.add_argument('--get_lab', type=str, help="getting data of laboratory")

group.add_argument('--get_all', action='store_true', help="getting all data of laboratory")

args = parser.parse_args()
asyncio.run(process_cli_args(args))
