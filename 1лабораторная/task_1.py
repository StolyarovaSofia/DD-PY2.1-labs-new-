import doctest


class Clothes:
    def __init__(self, number: int, cost: float):
        """
        Создание и подготовка к работе объекта "Одежда"

        :param number: Количество вещей.
        :param cost: Цена вещи.

        Примеры:
        >>> clothes = Clothes(150, 3500) #инициализация экземпляра класса
        """
        if not isinstance(number, int):
            raise TypeError("Количество вещей должно быть типа int")
        if number <= 0:
            raise ValueError("Количество вещей должно быть положительным числом")
        self.number = number

        if not isinstance(cost, (int, float)):
            raise TypeError("Цена вещи должна быть int или float")
        if cost < 0:
            raise ValueError("Цена вещи не может быть отрицательным числом")
        self.cost = cost


    def presence(self) -> bool:
        """
        Функция, которая проверяет наличие вещей

        :return: Есть вещь или нет

        Примеры:
        >>> clothes = Сlothes(0, 3500)
        >>> clothes.presence()
        """
        ...

    def supply_of_clothing(self, amt: int ) -> None:
        """
        Добавление вещей.
        :param amt: Количество добавляемых вещей

        Примеры:
        >>> clothes = Сlothes(0, 3500)
        >>> clothes.supply_of_clothing(200)
        """
        if not isinstance(amt, int):
            raise TypeError("Количество вещей должно быть типа int")
        if amt < 0:
            raise ValueError("Количество вещей должно быть положительным числом")
        ...


class Flowers:
    def __init__(self, quantity: int, price: float):
        """
        Создание и подготовка к работе объекта "Цветы"

        :param quantity: Количество единиц цветов.
        :param price: Цена единицы цветов.

        Примеры:
        >>> flowers = Flowers(100, 15.99)  # инициализация экземпляра класса
        """
        if not isinstance(quantity, int):
            raise TypeError("Количество единиц цветов должно быть типа int")
        if quantity <= 0:
            raise ValueError("Количество единиц цветов должно быть положительным числом")
        self.quantity = quantity

        if not isinstance(price, (int, float)):
            raise TypeError("Цена цветов должна быть int или float")
        if price < 0:
            raise ValueError("Цена цветов не может быть отрицательным числом")
        self.price = price

    def is_same_flower(self, other_flower) -> bool:
        """
        Проверка, одинаковые ли цветы.

        :param other_flower: Другой объект цветов для сравнения.

        :return: True, если количество и цена одинаковы.
        """

    def is_price_in_range(self, low: float, high: float) -> bool:
        """
        Проверка, попадает ли цена за единицу в диапазон.

        :param low: Нижняя граница диапазона.
        :param high: Верхняя граница диапазона.

        :return: True, если цена в диапазоне.

        Примеры:
        >>> flowers = Flowers(10, 15.99)
        >>> flowers.is_price_in_range(10, 20)
        True
        """


class Appliance:
    def __init__(self, quantity: int, price: float):
        """
        Инициализация бытового устройства.

        :param quantity: Количество единиц бытовой техники.
        :param price: Цена единицы бытовой техники.

        Примеры:
        >>> appliance = Appliance(12, 1500)
        """
        if not isinstance(quantity, int):
            raise TypeError("Количество единиц бытовой техники должно быть типа int")
        if quantity <= 0:
            raise ValueError("Количество единиц бытовой техники должно быть положительным числом")
        self.quantity = quantity

        if not isinstance(price, (int, float)):
            raise TypeError("Цена бытовой техники должна быть int или float")
        if price < 0:
            raise ValueError("Цена бытовой техники не может быть отрицательным числом")
        self.price = price


    def total_value(self) -> float:
        """
        Получение общей стоимости всех единиц бытовой техники.

        :return: Общая стоимость.

        Примеры:
        >>> appliance = Appliance(12, 1500)
        >>> appliance.total_value()
        18000
        """
        ...

    def description(self) -> str:
        """
        Получение описания бытовой техники.

        :return: Описание.

        Примеры:
        >>> appliance = Appliance(12, 1500)
        >>> appliance.description()
        'Бытовая техника: 12 единиц по 1500 каждая.'
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
