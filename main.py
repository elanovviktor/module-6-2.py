class Vehicle:
    __COLOR_VARIANTS = ['black', 'white', ' yellow', 'blue', 'red']
    def __init__(self, owner, __model, __color, __engin_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engin_power = __engin_power

    def get_model(self):
        return f'Модель: <название модели транспорта>{self.__model}'
    def get_horsepower (self):
        return f'Мощность двигателя: <мощность>{self.__engin_power}'
    def get_color (self):
        return f'Цвет: <цвет транспорта>{self.__color}'
    def print_info (self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')
    def set_color(self, new_color):
        self.new_color = new_color
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = self.new_color
        else:
            print(f'Нельзя сменить цвет на <новый цвет>"{self.new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
