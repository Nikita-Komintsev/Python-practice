import os
import time
import argparse
import json
import tempfile


# 1
def lensort(lst):
    return sorted(lst, key=lambda x: len(x))


print('\n#1 Функция lensort:')
print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))


# 2
def unique(lst):
    return list(set(lst))


print('\n#2 Функция unique:')
print(unique([1, 2, 1, 3, 2, 5]))


# 3
def my_enumerate(lst):
    return list(zip(lst, range(len(lst))))


print('\n#3 Функция my_enumerate:')
print(my_enumerate(["a", "b", "c"]))


# # 4
def count_word(file_name):
    word_dict = {}

    with open(file_name, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = word.strip('.,!?-:;')
                # if word == '': continue
                if len(word) == 0:
                    continue
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1

    for word, frequency in word_dict.items():
        print(f"{word}: {frequency}")


print('\n#4 Функция my_enumerate:')
count_word("/home/nikita/PycharmProjects/Python-practice/Lab-1/text.txt")

# 5
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"Время выполнения функции {func.__name__}: {execution_time} секунд")
#         return result
#
#     return wrapper
#
#
# @measure_time
# def square_with_for_loop(numbers):
#     result = []
#     for number in numbers:
#         result.append(number ** 2)
#     return result
#
#
# @measure_time
# def square_with_list_comprehension(numbers):
#     return [number ** 2 for number in numbers]
#
#
# @measure_time
# def square_with_map(numbers):
#     return list(map(lambda number: number ** 2, numbers))
#
#
# numbers = [1, 2, 3, 4, 5]
#
# square_with_for_loop(numbers)
# square_with_list_comprehension(numbers)
# square_with_map(numbers)
