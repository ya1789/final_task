from emoji import emojize
import time
import random
from functools import wraps


def log(line: str) -> callable:
    """Декоратор, принимающий строку line и подставляющий время"""

    def decorator(function: callable) -> callable:
        @wraps(function)
        def wrapper(*args, **kwargs):
            value = function(*args, **kwargs)
            timer = random.randint(1, 4)
            print(function.__name__)
            time.sleep(timer)
            print(line.format(timer))
            return value

        return wrapper

    return decorator


@log(emojize(':cook:') + " Приготовили за {}с!")
def baking(pizza: "Pizza") -> "Pizza":
    """Готовит пиццу"""
    return pizza


@log(emojize(':automobile:') + " Доставили за {}с!")
def delivering(pizza: "Pizza") -> "Pizza":
    """Доставляет пиццу"""
    return pizza


def pickup(pizza: "Pizza") -> "Pizza":
    """Самовывоз или еда в заведении"""
    print("Приятного аппетита!")
    return pizza


def processing(pizza: "Pizza", delivery: bool) -> None:
    """Реализует полный процесс доставки до клиента"""
    baking(pizza)
    delivering(pizza) if delivery else pickup(pizza)
