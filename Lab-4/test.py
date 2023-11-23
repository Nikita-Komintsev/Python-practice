import csv

def write_lab_data_to_csv(labs_data, output_file):
    # Открываем файл для записи в режиме 'w'
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        # Определяем заголовки CSV-файла
        fieldnames = ['Имя лабораторной'] + [lab['name'] for lab in labs_data]

        # Создаем объект writer с указанными заголовками
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Записываем заголовки в файл
        writer.writeheader()

        # Собираем уникальные имена студентов из всех лабораторных работ
        all_students = set()
        for lab in labs_data:
            students = lab.get('students', '').split(',')
            all_students.update(students)

        # Записываем данные по лабораторным работам
        for key in ['Дедлайн', 'Описание'] + list(all_students):
            row_data = {'Имя лабораторной': key}
            for lab in labs_data:
                if key == 'Дедлайн':
                    row_data[lab['name']] = lab['deadline']
                elif key == 'Описание':
                    row_data[lab['name']] = lab['description']
                else:
                    row_data[lab['name']] = '+' if key in lab.get('students', '').split(',') else ''

            # Записываем данные в файл
            writer.writerow(row_data)

# Пример использования функции для одной лабораторной работы
lab_data_single = {'deadline': '03.01.2023', 'description': 'NEW DESCR', 'students': 'Student1,Student3', 'name': 'Lab1'}
write_lab_data_to_csv([lab_data_single], 'output_lab_data_single.csv')
