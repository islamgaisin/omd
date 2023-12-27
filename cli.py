import click
import random


class Pizza:
    def __init__(self, size: str):
        """
        Инициализатор базового класса Pizza
        :param size: размер пиццы, может быть либо 'L', либо 'XL'
        receipt: поле, хранящее рецепт пиццы
        """
        self.size = size
        self.receipt = {}

    def dict(self) -> dict:
        """
        Метод возвращает рецепт пиццы
        :return: поле receirp - рецепт пиццы
        """
        return self.receipt

    def __eq__(self, other):
        """
        Метод сравнивает две пиццы. Если у них одинаковые названия и размеры,
        то пиццы совпадают
        :param other: пицца, с которой надо сравнить
        :return: результат сравнения
        >>> Margherita('L') == Margherita('L')
        True
        >>> Margherita('L') == Margherita('XL')
        False
        >>> Margherita('L') == Pepperoni('L')
        False
        >>> Margherita('L') == Pepperoni('XL')
        False
        """
        return self.receipt.keys() == other.receipt.keys() and \
            self.size == other.size


class Margherita(Pizza):
    def __init__(self, size: str):
        super().__init__(size)
        self.receipt = {'Margherita \U0001F9C0': ['tomato sauce', 'mozzarella', 'tomatoes']}


class Pepperoni(Pizza):
    def __init__(self, size: str):
        super().__init__(size)
        self.receipt = {'Pepperoni \U0001F355': ['tomato sauce', 'mozzarella', 'pepperoni']}


class Hawaiian(Pizza):
    def __init__(self, size: str):
        super().__init__(size)
        self.receipt = {'Hawaiian \U0001F34D': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']}


def log(template_time: str):
    def decorator(in_function):
        def print_time(pizza: Pizza):
            click.echo(template_time.format(in_function(pizza)))

        return print_time

    return decorator


@log('\U0001F468 Приготовили за {}с!')
def bake_pizza(pizza: Pizza):
    """
    Готовит пиццу
    :param pizza: пицца, которая будет готовиться
    :return: время, за которое приготовили пиццу
    """
    return random.randint(1, 30)


@log('\U0001F6F5 Доставили за {}с!')
def delivery_pizza(pizza: Pizza):
    """
    Доставляет пиццу
    :param pizza: пицца, которая будет доставляться
    :return: время, за которое доставили пиццу
    """
    return random.randint(5, 60)


@log('\U0001F3E0 Забрали за {}с!')
def pick_up(pizza: Pizza):
    """
    Самовывоз
    :param pizza: пицца, которая будут забирать
    :return: время, за которое забрали пиццу
    """
    return random.randint(10, 45)


@click.group()
def cli():
    pass


@cli.command()
@click.argument('pizza', nargs=1)
@click.option('--delivery', default=False, is_flag=True)
def order(pizza: str, delivery: bool):
    """
    Готовит и доставляет пиццу
    :param pizza: пицца, которую будут готовить и доставлять
    :param delivery: флаг, показывающий, будет ли пицца доставляться
    :return: функция ничего не возвращает
    """
    if pizza == 'Margherita':
        pizza = Margherita('L')
    elif pizza == 'Pepperoni':
        pizza = Pepperoni('L')
    else:
        pizza = Hawaiian('L')
    bake_pizza(pizza)
    if delivery:
        delivery_pizza(pizza)
    else:
        pick_up(pizza)


@cli.command()
def menu():
    """
    Выводит меню
    :return: функция ничего не возвращает
    """
    pizzas = [Margherita('L'), Pepperoni('L'), Hawaiian('L')]
    for pizza in pizzas:
        click.echo('- ' + list(pizza.receipt.keys())[0] + ': ' + \
                   ', '.join(list(pizza.receipt.values())[0]))


if __name__ == '__main__':
    cli()
