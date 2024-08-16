class IncorrectVinNumber(Exception):
    def __init__(self, msg):
        self.msg = msg


class IncorrectCarNumbers(Exception):
    def __init__(self, msg):
        self.msg = msg


class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(__numbers)
    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber(f'{self.model}. Неверный vin-номер! - {vin_number}')
        elif not(1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber(f'{self.model}. Неверный диапазон для vin номера - {vin_number}')
        else:
            return True

    def __is_valid_numbers(self, __numbers):
        if not isinstance(__numbers, str):
            raise IncorrectCarNumbers(f'{self.model}. некорректный тип данных для номеров («{__numbers}»)')
        elif len(__numbers) != 6:
            raise IncorrectCarNumbers(f'{self.model}. Неверная длина номера («{__numbers}»)')
        else:
            return True

decor_string = f'{'':=<40}'
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.msg)
except IncorrectCarNumbers as exc:
    print(exc.msg)
else:
    print(f'{first.model} успешно создан')
print(decor_string)
try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.msg)
except IncorrectCarNumbers as exc:
    print(exc.msg)
else:
    print(f'{second.model} успешно создан')
print(decor_string)
try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.msg)
except IncorrectCarNumbers as exc:
    print(exc.msg)
else:
    print(f'{third.model} успешно создан')
