import json

# 1. Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод реализуют подклассы")

    def eat(self):
        print(f"{self.name} is eating.")

# 2. Подклассы
class Bird(Animal):
    def make_sound(self):
        return "Чирик!"

class Mammal(Animal):
    def make_sound(self):
        return "Ррр!"

class Reptile(Animal):
    def make_sound(self):
        return "Шшш!"

# 3. Полиморфизм
def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} says: {animal.make_sound()}")

# 4. Класс Zoo с композицией
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)


# 5. Классы для сотрудников
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")


class Veterinarian:
    def __init__(self, name):
        self.name = name


    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")


# 6. Сохранение и загрузка информации о зоопарке
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json_data = {
                "animals": [{"name": animal.name, "age": animal.age, "type": animal.__class__.__name__} for animal in self.animals],
                "staff": [staff_member.name for staff_member in self.staff]
            }
            json.dump(json_data, f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
            for animal_data in json_data['animals']:
                if animal_data['type'] == "Bird":
                    animal = Bird(animal_data['name'], animal_data['age'])
                elif animal_data['type'] == "Mammal":
                    animal = Mammal(animal_data['name'], animal_data['age'])
                elif animal_data['type'] == "Reptile":
                    animal = Reptile(animal_data['name'], animal_data['age'])
                self.add_animal(animal)

            for staff_name in json_data['staff']:
                self.add_staff(ZooKeeper(staff_name))  # Можно добавить разные типы сотрудников

# Пример использования
if __name__ == "__main__":
    zoo = Zoo()

    # Добавляем животных
    zoo.add_animal(Bird("Воробей", 2))
    zoo.add_animal(Mammal("Лев", 5))
    zoo.add_animal(Reptile("Змея", 3))

    # Добавляем сотрудников
    zoo.add_staff(ZooKeeper("Анна"))
    zoo.add_staff(Veterinarian("Виктор"))

    # Вызываем звуки животных
    animal_sound(zoo.animals)

    # Сохраняем зоопарк в файл
    zoo.save_to_file("zoo_data.json")

    # Загружаем зоопарк из файла
    new_zoo = Zoo()
    new_zoo.load_from_file("zoo_data.json")
    animal_sound(new_zoo.animals)



