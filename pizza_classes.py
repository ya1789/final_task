from abc import ABC, abstractmethod
from emoji import emojize


class Pizza(ABC):
    """Абстрактный класс Пиццы"""
    SIZES = ['L', 'XL']

    @abstractmethod
    def __init__(self, size: str):

        self.size = size
        self.ingredients = {
            'tomato sauce',
            'mozzarella'
        }
        if not (self.size in self.__class__.SIZES):
            raise ValueError(f"{self.size} != L or XL")

    def __eq__(self, other_pizza):
        """Проверка равенства"""
        if self is other_pizza:
            return True
        if isinstance(self, Pizza) & isinstance(other_pizza, Pizza):
            return (type(self) == type(other_pizza)) & (self.size == other_pizza.size)
        else:
            return False

    def dict(self) -> dict:
        """Выводит рецепт в виде словаря"""
        return {
            "name": self.__class__.__name__,
            "size": self.size,
            "ingredients": self.ingredients
        }

    def dict_out(self) -> None:
        """Красивый вывод ингридиентов пиццы"""
        return ', '.join("{}".format(v) for v in self.ingredients)


class Margherita(Pizza):
    """Класс Маргариты"""

    def __init__(self, size: str):
        super().__init__(size)
        self.ingredients.update({"tomatoes"})
        self.emj = emojize(':tomato:')


class Pepperoni(Pizza):
    """Класс Пеперони"""

    def __init__(self, size: str):
        super().__init__(size)
        self.ingredients.update({"pepperoni"})
        self.emj = emojize(':pizza:')


class Hawaiian(Pizza):
    """Класс Гавайской"""

    def __init__(self, size: str):
        super().__init__(size)
        self.ingredients.update({"chicken", "pineapples"})
        self.emj = emojize(':pineapple:')
