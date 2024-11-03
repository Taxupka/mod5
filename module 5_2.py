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


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))