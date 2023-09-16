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
                word = word.strip('.,!?-:;').lower()
                if len(word) == 0:
                    continue
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1

    for key, value in word_dict.items():
        print(f"{key}: {value}")


print('\n#4 Функция my_enumerate:')
count_word("text.txt")

