#Task 1
import os
print("Current working dir:", os.getcwd())
import logging
from functools import wraps
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "w"))


def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pos_args = list(args) if args else "none"
        kw_args  = kwargs if kwargs else "none"

        result = func(*args, **kwargs)

        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters:{pos_args}")
        logger.log(logging.INFO, f"keyword parameters:{kw_args}")
        logger.log(logging.INFO,f"return:{result}")
        

        return result
    return wrapper

@logger_decorator
def say_hello():
    print("Hello, World!")

@logger_decorator
def accepts_positional_args(*args):
    return True

@logger_decorator
def accepts_keyword_args(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    say_hello()
    accepts_positional_args(1, 2, 3, 4)
    accepts_keyword_args(a=1, b=2, c="test")
