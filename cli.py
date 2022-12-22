from pizza_classes import *
from pizza_functions import *
from emoji import emojize
import click
import random
import time


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option('--size', type=click.Choice(['L', 'XL']), multiple=False)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool, size: str) -> None:
    """Готовит и доставляет пиццу"""
    if pizza.lower() == 'pepperoni':
        cur_pizza = Pepperoni(size)
    elif pizza.lower() == 'margherita':
        cur_pizza = Margherita(size)
    elif pizza.lower() == 'hawaiian':
        cur_pizza = Hawaiian(size)
    else:
        print("Ознакомьтесь с меню! Такой пиццы нет...")
        return
    processing(cur_pizza, delivery)


@cli.command()
def menu() -> None:
    """Выводит меню"""
    for x in [Margherita("L"), Pepperoni("L"), Hawaiian("L")]:
        print('- ', x.__class__.__name__, x.emj + ':', x.dict_out())


if __name__ == '__main__':
    cli()
