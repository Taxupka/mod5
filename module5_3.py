class House:    #создаю класс
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


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__