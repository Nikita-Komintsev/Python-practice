# 3.	Реализуйте декоратор, который измеряет время выполнения функции и выводит его в консоль, в виде класса.
# Реализуйте дополнительный класс-декоратор для вывода полученного времени в формате HTML: <html><body>Время</body></html>.
# Оба декоратора должны также обеспечивать ведение истории вызовов исходной функции в формате:
# <время вызова>: function <имя функции> called with arguments <аргументы>
# Используйте данные декораторы вместе на примерах из задачи 5 семинара 1.

from functools import wraps
import time


class TimerDecorator:
    def __init__(self, function):
        self.function = function
        self.counter = 0
        self.runtime = 0

    # @wraps
    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.function(*args, **kwargs)
        runtime = time.perf_counter() - start
        self.runtime = runtime
        return result


class HtmlOutputDecorator:
    def __init__(self, function):
        self.function = function
        self.counter = 0

    # @wraps
    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)
        print(f"<html><body>{result:.4f}</body></html>")


@HtmlOutputDecorator
@TimerDecorator
def func(count):
    i = 1
    for j in range(1, count):
        i *= j
    return i


if __name__ == "__main__":
    func(99999)