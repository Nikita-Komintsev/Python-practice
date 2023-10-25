# Python-practice
Практики по дисциплине высокоуровневые языки программирования

## Lab-1
1. Функция lensort, которая принимает список строк и сортирует его в порядке возрастания их длины. 
2. Функция unique, которая удаляет дубликаты из списка и возвращает результат.
3. Функция my_enumerate, которая принимает произвольный список, и возвращает список кортежей, в каждом из которых два элемента: элемент списка и порядковый номер данного элемента.
4. Функция, принимающую имя файла с текстом и подсчитывающую частоту встречающихся в нём слов. Каждая линия вывода имеет формат:<br/>
«<Слово>: <Сколько раз встречается это слово>».
5. Декоратор, который измеряет время выполнения функции и выводит его в консоль. Функции принимают список целых чисел и возвращают список их квадратов: через цикл for, через list comprehension и с использованием встроенной функции map.
6. Key-value хранилище. Данные будут сохраняться в файле storage.data. Добавление новых данных в хранилище и получение текущих значений осуществляется с помощью утилиты командной строки storage.py.<br/>
Пример работы утилиты:
  - Сохранение значения value по ключу key_name: <br/>$ storage.py --key key_name --val value
  - Получение значения по ключу key_name: <br/>$ storage.py --key key_name
 ## Lab-2
 1. Класс вектора на плоскости. Перегрузка операторов.
 2. Иерархия классов для расчёта площади плоских фигур: прямоугольника, треугольника, круга.
 3. Декоратор, который измеряет время выполнения функции и выводит его в консоль, в виде класса + дополнительный класс-декоратор для вывода полученного времени в формате HTML: <html><body>Время</body></html>. Оба декоратора обеспечивют ведение истории вызовов исходной функции в формате:<br/><время вызова>: function <имя функции> called with arguments <аргументы>
 4. Класс для логирования сообщений в файл. Сообщения выводятся в формате: <br/>[<статус>] <время вывода>: <сообщение>
 ## Lab-3
Бинарное дерево поиска, поддерживающее протокол итерации с получением элементов в порядке возрастания. Дерево имеет метод для вставки элементов. Обход элементов дерева в цикле for c выводом значений элементов в порядке возрастания.
