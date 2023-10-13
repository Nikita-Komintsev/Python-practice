
import time
from functools import wraps

class TimingDecorator:
    def __init__(self, func):
        self.func = func
        self.call_history = []

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()

        call_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        info = f"{call_time}: function {self.func.__name__} called with arguments {args}"
        self.call_history.append(info)

        print(f"Функция '{self.func.__name__}': {end_time - start_time:.4f} секунд")
        return result


class HTMLTimingDecorator(TimingDecorator):
    def __call__(self, *args, **kwargs):
        result = super().__call__(*args, **kwargs)
        html_output = f"<html><body>{result}</body></html>"
        return html_output


@HTMLTimingDecorator
def square_for(nums):
    result = []
    for num in nums:
        result.append(num ** 2)
    return result


@HTMLTimingDecorator
def square_list_comprehension(nums):
    return [num ** 2 for num in nums]


@HTMLTimingDecorator
def square_map(nums):
    return list(map(lambda x: x ** 2, nums))


numbers = list(range(1, 10001))

result1 = square_for(numbers)
result2 = square_list_comprehension(numbers)
result3 = square_map(numbers)

print("History:")
for call_info in square_for.call_history:
    print(call_info)

for call_info in square_list_comprehension.call_history:
    print(call_info)

for call_info in square_map.call_history:
    print(call_info)
