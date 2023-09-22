import time


def decorator_time(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        all_time = end_time - start_time
        print(f"Функция '{func.__name__}': {all_time:.4f} секунд")
        return result
    return wrapper


@decorator_time
def square_for(nums):
    result = []
    for num in nums:
        result.append(num ** 2)
    return result


@decorator_time
def square_list_comprehension(nums):
    return [num ** 2 for num in nums]


@decorator_time
def square_map(nums):
    return list(map(lambda x: x ** 2, nums))


numbers = list(range(1, 10000001))

square_for(numbers)
square_list_comprehension(numbers)
square_map(numbers)
