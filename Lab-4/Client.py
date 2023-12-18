import aiohttp
import asyncio
import argparse
import json
import docx


async def write_lab_data_to_word(labs_data, file_name):
    document = docx.Document()

    if isinstance(labs_data, dict):
        labs_data = [labs_data]

    table = document.add_table(rows=1, cols=len(labs_data) + 1)
    header_cells = table.rows[0].cells
    header_cells[0].text = 'Название'
    for i, lab in enumerate(labs_data):
        header_cells[i + 1].text = lab['name']

    all_students = set()
    for lab in labs_data:
        students = lab.get('students', '').split(',')
        if students and any(name.strip() for name in students):
            all_students.update(students)

    for key in ['Дедлайн', 'Описание'] + list(all_students):
        row_cells = table.add_row().cells
        row_cells[0].text = key
        for i, lab in enumerate(labs_data):
            if key == 'Дедлайн':
                row_cells[i + 1].text = lab.get('deadline', '')
            elif key == 'Описание':
                row_cells[i + 1].text = lab.get('description', '')
            else:
                row_cells[i + 1].text = '+' if key in lab.get('students', '').split(',') else ''

    document.save(f'{file_name}.docx')


async def print_response(response):
    print(f"Status: {response.status}")
    location_header = response.headers.get('Location', '')
    if location_header:
        print(f'URL: {location_header}')
    text = await response.text()
    if text:
        print(text)


async def add_lab(url, lab, deadline, description):
    async with aiohttp.ClientSession() as session:
        request = {'name': lab, 'deadline': deadline, 'description': description}
        async with session.post(url=f"{url}/labs", data=json.dumps(request)) as response:
            await print_response(response)


async def update_lab(url, lab, deadline=None, description=None, students=None):
    request_data = {}
    if deadline is not None:
        request_data['deadline'] = deadline
    if description is not None:
        request_data['description'] = description
    if students is not None:
        request_data['students'] = students

    async with aiohttp.ClientSession() as session:
        async with session.patch(url=f"{url}/labs/{lab}", data=json.dumps(request_data)) as response:
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
                    await write_lab_data_to_word(data, name)
                except json.JSONDecodeError as ex:
                    print(f"Error decoding JSON: {ex}")


async def get_all(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=f"{url}/labs") as response:
            await print_response(response)
            try:
                data = await response.json()
                await write_lab_data_to_word(data, 'all_info_labs')
            except json.JSONDecodeError as ex:
                print(f"Error decoding JSON: {ex}")


async def process_cli_args(cli_args):
    url = 'http://0.0.0.0:8080'

    if cli_args.add:
        if not cli_args.deadline:
            print("Deadline is required (--deadline)")
        else:
            description = getattr(cli_args, 'description', None)
            await add_lab(url, cli_args.add, cli_args.deadline, description)

    if cli_args.update:
        if not (cli_args.deadline or cli_args.description or cli_args.students):
            print("Required --deadline --description or --students")
        else:
            await update_lab(url, cli_args.update, cli_args.deadline, cli_args.description, cli_args.students)

    if cli_args.delete:
        await delete_lab(url, cli_args.delete)

    if cli_args.get_lab:
        await get_lab(url, cli_args.get_lab)

    if cli_args.get_all:
        await get_all(url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process command line arguments for lab management.")

    parser.add_argument('--deadline', type=str, help="Deadline of laboratory - day.month.year")
    parser.add_argument('--description', type=str, help="Description of laboratory")
    parser.add_argument('--students', type=str, help="Students who completed the laboratory")

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('--add', type=str, help="adding new laboratory")

    group.add_argument('--update', type=str, help="updating fields")

    group.add_argument('--delete', type=str, help="delete laboratory")

    group.add_argument('--get_lab', type=str, help="getting data of laboratory")

    group.add_argument('--get_all', action='store_true', help="getting all data of laboratory")

    args = parser.parse_args()
    asyncio.run(process_cli_args(args))
