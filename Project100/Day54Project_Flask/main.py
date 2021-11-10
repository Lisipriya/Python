import time


def speed_calc_decorator(function):
    def wrapper_function():
        first_time = time.time()
        function()
        second_time = time.time()
        time_executed = second_time - first_time
        print(time_executed)

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
