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

h1 = House('ЖК Горский', 18)    #присвоение переменной h1 класса House с атрибутами
h2 = House('Домик в деревне', 2)
h1.go_to(5) #вызов атрибутов переменной h1 методом go_to
h2.go_to(10)