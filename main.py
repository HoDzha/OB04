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
class Fighter:
    def __init__(self, name, power):
        self.power = power
        self.name = name
        self.weapon = None  # Default weapon set to None

class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

# Абстраткный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def attack(self):
        pass

class Bow(Weapon):
    def __init__(self, name, range, damage):
        self.name = name
        self.range = range
        self.damage = damage
    def attack(self, monster,power):
        monster.health -= self.damage*power
        if monster.health <= 0:
            print(f"Победа! {monster.name} убит оружием {self.name} c расстоянием {self.range}!")
        else:
            print(f"Боец наносит удар! {monster.name} получил {self.damage*power} урона оружием {self.name} с расстояния {self.range} и осталось {monster.health} здоровья.")

class Sword(Weapon): #меч
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    def attack(self, monster,power):
        monster.health -= self.damage*power
        if monster.health <= 0:
            print(f"Победа! {monster.name} убит оружием {self.name}!")
        else:
            print(f"Боец наносит удар! {monster.name} получил {self.damage*power} урона оружием {self.name} и осталось {monster.health} здоровья.")


# игрок
class Player:
    def __init__(self,fighter, weapon, monster):
        self.fighter = fighter
        self.fighter.weapon = weapon
        self.monster = monster
        print(f"Текущий боец: {self.fighter.name} с оружием {self.fighter.weapon.name} и монстр {self.monster.name} с уровнем здоровья {self.monster.health}!")
    def select_fighter(self,fighter):
        self.fighter = fighter
    def select_monster(self,monster):
        self.monster = monster
    def change_weapon(self, weapon):
        self.fighter.weapon = weapon
        print(f"Боец {self.fighter.name} выбрал оружие {weapon.name}!")

    def fight(self):
        self.fighter.weapon.attack(self.monster,self.fighter.power)


gnome = Fighter("Гном",1)
sword_master = Fighter("Мастер меча",10)
archer = Fighter("Лучник",2)
sword = Sword("Меч", 10)
bow = Bow("Лук", 5, 5)
long_bow = Bow("Длинный лук", 10, 10)
troll = Monster("Тролль", 100)
cyclopus = Monster("Циклоп", 50)
gamer = Player(gnome, sword, cyclopus)
gamer.fight()
gamer.change_weapon(bow)
gamer.fight()
gamer.select_fighter(archer)
gamer.change_weapon(long_bow)
gamer.fight()
gamer.fight()
gamer.select_monster(troll)
gamer.select_fighter(sword_master)
gamer.change_weapon(sword)
gamer.fight()