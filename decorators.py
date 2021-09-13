import logging
logging.basicConfig(filename='input.log', level=logging.INFO)


def logger_decorator(func):
    def wrapper_func(*args, **kwargs):
        logging.info(f'Parameters {args[0]}, {args[1]} have been used')
        return func(*args, **kwargs)
    return wrapper_func


@logger_decorator
def sum(num1, num2):
    return num1 + num2


sum(2, 3)
sum(4, 6)
sum(1, 9)
sum(2, 4)
sum(1, 6)
sum(4, 7)
sum(9, 6)
