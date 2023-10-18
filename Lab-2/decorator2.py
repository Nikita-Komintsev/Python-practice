import time

# html декоратор должен работать после первого
# html декоратор получает только время и выводит его

class TimingDecorator:
    def __init__(self, func):
        self.func = func
        #self.call_history = []

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

       # call_info = f"{time.ctime()}: function {self.func.__name__} called with arguments {args}"
       # self.call_history.append(call_info)

        print(f"{self.func.__name__} took {execution_time:.4f} seconds to run")
        return result


class HtmlTimingDecorator:
    def __init__(self, func):
        self.func = func
        #self.call_history = self.func.call_history

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)

        #call_info = f"{time.ctime()}: function {self.func.func.__name__} called with arguments {args}"
        #self.call_history.append(call_info)

        print(f"{self.func} took {result:.4f} seconds to run")
        print(f'<html><body>{result:.4f}</body></html>')


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


numbers = list(range(1, 10000001))

square_for(numbers)
square_list_comprehension(numbers)
square_map(numbers)

# print("\nCall History:")
# for func_decorator in [square_for, square_list_comprehension, square_map]:
#     for call in func_decorator.call_history:
#         print(call)
