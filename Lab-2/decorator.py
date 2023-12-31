import time


class Decorator:
    def __init__(self, function):
        self.function = function
        self.call_history = []

    @property
    def __name__(self):
        return self.function.__name__

    def log(self, *args):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        info = f"{current_time}: function {self.function.__name__} called with arguments {args}"
        self.call_history.append(info)



class TimingDecorator(Decorator):
    @property
    def __name__(self):
        return self.function.__name__

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.function(*args, **kwargs)
        self.finish = time.perf_counter() - start

        self.log(*args)

        print(f"\n{self.finish:.4f} in {__class__.__name__}")
        return result


class HtmlTimingDecorator(Decorator):
    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)

        self.log(*args)

        print(f"<html><body>{self.function.finish:.4f}</body></html> in {__class__.__name__}")

        return result


@HtmlTimingDecorator
@TimingDecorator
def square_for(nums):
    result = []
    for num in nums:
        result.append(num ** 2)
    return result


@HtmlTimingDecorator
@TimingDecorator
def square_list_comprehension(nums):
    return [num ** 2 for num in nums]


@HtmlTimingDecorator
@TimingDecorator
def square_map(nums):
    return list(map(lambda x: x ** 2, nums))


numbers = list(range(1, 10001))

square_for(numbers)
square_list_comprehension(numbers)
square_map(numbers)

print("\nHistory:")
for func_decorator in [square_for, square_list_comprehension, square_map]:
    for call_info in func_decorator.call_history:
        print(call_info)
