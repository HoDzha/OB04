#  Есть класс `Fighter`, представляющий бойца.
# - Есть класс `Monster`, представляющий монстра.
# - Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
# Шаг 1:Создайте абстрактный класс для оружия
# - Создайте абстрактный класс `Weapon`, который будет содержать абстрактный метод `attack()`.
# Шаг 2: Реализуйте конкретные типы оружия
# - Создайте несколько классов, унаследованных от `Weapon`, например, `Sword` и `Bow`. Каждый из этих классов
# реализует метод `attack()` своим уникальным способом.
# Шаг 3: Модифицируйте класс `Fighter`
# - Добавьте в класс `Fighter` поле, которое будет хранить объект класса `Weapon`.
# - Добавьте метод `change_weapon()`, который позволяет изменить оружие бойца.
# Шаг 4: Реализация боя
# - Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
# Требования к заданию:
# - Код должен быть написан на Python.
# - Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия можно
# легко добавлять, не изменяя существующие классы бойцов и механизм боя.
# - Программа должна выводить результат боя в консоль.
from abc import ABC, abstractmethod

# боец
Class Fighter()
    def __init__(self,name,power):
        self.power = power
        self.name = name
        self.weapon = None
# монстр
Class Monster()
    def __init__(self, health):
        self.health = health

# Абстраткный класс для оружия
Class Weapon(ABC)

    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def attack(self):
        pass

Class Bow(Weapon) #лук
    def __init__(self, name, range, damage):
        self.name = name
        self.range = range
        self.damage = damage
    def attack(self,monster):
        monster.health -= self.damage
        if monster.health <= 0:
            print(f"Победа! Монстр убит оружием {self.name} c расстоянием {self.range}!")
        else:
            print(f"Боец наносит удар! Монстр получил {self.damage} урона оружием {self.name} с расстояния {self.range} и осталось {monster.health} здоровья.")

Class Sword(Weapon) #меч
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    def attack(self, monster):
        monster.health -= self.damage
        if monster.health <= 0:
            print(f"Победа! Монстр убит оружием {self.name}!") ")
        else:
            print(f"Боец наносит удар! Монстр получил {self.damage} урона оружием {self.name} и осталось {monster.health} здоровья.")


# игрок
Class Player()
    def __init__(self,fighter, weapon, monster):
        self.fighter = fighter
        self.fihter.weapon = weapon
        self.monster = monster
    def select_fighter(self,fighter):
        self.fighter = fighter
    def change_weapon(self, weapon):
        self.fighter.weapon = weapon
        print(f"Боец {fighter.name} выбрал оружие {weapon.name}!")

    def fight(self):
        self.fighter.weapon.attack(self.monster)
