class House: # Создайте класс House.
    def __init__(self, name, number_of_floors): # Внутри класса House определите метод __init__, в который передадите название и кол-во этажей.
        # Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
        self.name = name
        self.number_of_floors =number_of_floors

    # Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
    def go_to(self, new_floor):
        int(new_floor)
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

# Исходные данные:
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Москвы', 20)
h1.go_to(5) # Вывод на консоль: 1, 2, 3, 4, 5
h2.go_to(10) # Вывод на консоль: "Такого этажа не существует"
h3.go_to(12) # Вывод на консоль: от 1 до 12 (включительно)

