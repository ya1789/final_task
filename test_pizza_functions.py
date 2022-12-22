from pizza_functions import baking, delivering, pickup
from pizza_classes import Margherita, Pepperoni, Hawaiian
import random
import pytest
from unittest.mock import patch


def test_baking(capsys):
    with patch("random.randint") as false_int:
        false_int.return_value = 1
        baking(Margherita('L'))
        captured = capsys.readouterr()
        assert captured.out == "baking\n🧑‍🍳 Приготовили за 1с!\n"
        assert captured.err == ""


def test_delivery(capsys):
    with patch("random.randint") as false_int:
        false_int.return_value = 1
        delivering(Margherita('L'))
        captured = capsys.readouterr()
        assert captured.out == "delivering\n🚗 Доставили за 1с!\n"
        assert captured.err == ""


def test_pickup(capsys):
    pickup(Hawaiian("XL"))
    captured = capsys.readouterr()
    assert captured.out == "Приятного аппетита!\n"
    assert captured.err == ""


if __name__ == '__main__':
    pytest.main()
