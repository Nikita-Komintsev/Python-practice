import time
import functools


class TimingDecorator:
    def __init__(self, func):
        self.func = func
        self.call_history = []

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        function_name = self.func
        self.call_history.append(f"{end_time}: function {function_name} called with arguments {args}")
        print(f"Function {function_name} took {end_time - start_time} seconds to execute in {__class__.__name__}")
        return result


class HtmlTimingDecorator:
    def __init__(self, func):
        self.func = func
        self.call_history = []

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        function_name = self.func.__name__
        self.call_history.append(f"{end_time}: function {function_name} called with arguments {args}")
        time_taken = end_time - start_time
        html_time = f'<html><body>{time_taken}</body></html>'
        print(f"\nFunction {function_name} took {time_taken} seconds to execute in {__class__.__name__}")
        print(f"HTML format: {html_time}")
        return result


@TimingDecorator
@HtmlTimingDecorator
def square_for(nums):
    result = []
    for num in nums:
        result.append(num ** 2)
    return result


@TimingDecorator
@HtmlTimingDecorator
def square_list_comprehension(nums):
    return [num ** 2 for num in nums]


@TimingDecorator
@HtmlTimingDecorator
def square_map(nums):
    return list(map(lambda x: x ** 2, nums))


numbers = list(range(1, 100))

result1 = square_for(numbers)
result2 = square_list_comprehension(numbers)
result3 = square_map(numbers)

print("\nCall History:")
for func_decorator in [square_for, square_list_comprehension, square_map]:
    for call in func_decorator.call_history:
        print(call)
