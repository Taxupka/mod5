class House:    #создаю класс

    houses_history = []

    def __new__(cls, *args, **kwargs):  #переопределить метод new
        inst = object.__new__(cls)  #присвоение переменной inst объекта класса
        args = args[0]              #присвоение переменной args 1го эл-та списка
        cls.houses_history.append(args)     #добавление значения args в список сквозь методы класса
        return inst                 # возвращает inst


    def __init__(self, name, number_of_floors): #инициализация атрибутов
        self.name = name    #присвоение переменной name атрибута self.name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor): #создание метода go_to
        if new_floor > 0 and new_floor < self.number_of_floors + 1: #условие, удовлетворяющее логике
            for i in range(1, new_floor + 1):   #обозначение области цикла
                print(i)    #печать номера этажа
        elif new_floor > self.number_of_floors or new_floor < 1:    #условие, не удовлетворяющее логике
            print('Такого этажа не сущесвует')  #печать результата выполнения elif


    def __len__(self):  #добавление метода len
        return self.number_of_floors    #метод вернет значение number_of_floors


    def __str__(self):  #добавление метода str
        return f'Название: {self.name} Количество этажей: {self.number_of_floors}'


    def __eq__(self, other):    # сравнивание количества этажей
        isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int)  #убедиться, что типа данных совпадают
        return self.number_of_floors == other.number_of_floors  #вернуть результат сравнения


    def __lt__(self, other):    #проверить какой объект меньше
        return self.number_of_floors < other.number_of_floors


    def __le__(self, other):    #проверитть <=
        return self.number_of_floors <= other.number_of_floors


    def __gt__(self, other):    #проверить кто больше
        return self.number_of_floors > other.number_of_floors


    def __ge__(self, other):    #проверить >=
        return self.number_of_floors >= other.number_of_floors


    def __ne__(self, other):    #проверить неравенство
        return self.number_of_floors != self.number_of_floors


    def __add__(self, value):   #увеличить количество этажей на заданное value
        isinstance(self.number_of_floors, int)  #убедиться, что типы данных соответствуют
        isinstance(value, int)
        self.number_of_floors += value  #сложить этажи и value
        return self


    def __radd__(self, value):
        self.number_of_floors += value
        return self


    def __iadd__(self, value):
        self.number_of_floors += value
        return self


    def __del__(self):
        return print(f'{self.name} снесен, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
h4 = House('Домдом', 55)
print(House.houses_history)


# Удаление объектов
del h2
del h3

print(House.houses_history)
