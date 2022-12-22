from cli import menu, order
import random
from click.testing import CliRunner
from unittest.mock import patch
from pytest_unordered import unordered
import pytest


def test_menu():
    real_menu = (
        "-  Margherita 🍅: mozzarella, tomatoes, tomato sauce\n"
        "-  Pepperoni 🍕: pepperoni, mozzarella, tomato sauce\n"
        "-  Hawaiian 🍍: pineapples, mozzarella, chicken, tomato sauce\n"

    )
    runner = CliRunner()
    result = runner.invoke(menu)
    assert result.exit_code == 0
    assert result.output == unordered(real_menu)


def test_wrong_pizza():
    runner = CliRunner()
    result = runner.invoke(order, ['мам пицу', '--size=L'])
    assert result.exit_code == 0
    assert result.output == 'Ознакомьтесь с меню! Такой пиццы нет...\n'


def test_no_size():
    runner = CliRunner()
    result = runner.invoke(order, ['Pepperoni'])
    assert result.exit_code == 1
    assert result.output == ""


if __name__ == '__main__':
    pytest.main()
