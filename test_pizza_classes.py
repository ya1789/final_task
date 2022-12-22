from pizza_classes import Pizza, Margherita, Pepperoni, Hawaiian
import pytest
from pytest_unordered import unordered


def test_no_object_from_abstract_init():
    with pytest.raises(TypeError) as e:
        p = Pizza()
    assert "Can't instantiate abstract class Pizza with abstract method __init__" == e.value.args[0]


def test_incorrect_size():
    with pytest.raises(ValueError) as e:
        p = Pepperoni('S')
    assert "S != L or XL" == e.value.args[0]


def test_equality():
    assert Pepperoni('L') == Pepperoni('L')


def test_equality_different_classes():
    assert Pepperoni('L') != Hawaiian('L')


def test_equality_different_sizes():
    assert Pepperoni('L') != Pepperoni('XL')


def test_dict_method():
    expected_output = {'name': 'Hawaiian',
                       'size': 'L',
                       'ingredients': {'mozzarella', 'pineapples',
                                       'chicken', 'tomato sauce'}
                       }
    assert Hawaiian('L').dict() == expected_output


def test_dict_out_method():
    assert unordered("chicken, pineapples, tomato sauce, mozzarella") == Hawaiian('L').dict_out()


if __name__ == '__main__':
    pytest.main()
