import math
from abc import ABC, abstractmethod


class Unit(ABC):
    """Создаем абстрактный класс"""
    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

    @abstractmethod
    def calculate_max_health(self):
        """Метод, считающий максимальное здоровье"""
        pass

    @abstractmethod
    def calculate_damage(self):
        """Метод, считающий урон"""
        pass

    @abstractmethod
    def calculate_defense(self):
        """Метод, считающий защиту"""
        pass


class Character(Unit):
    """Создаем дочерний класс - Персонаж"""
    def __init__(self, strength, dexterity, constitution, wisdom=0, intelligence=0, charisma=0):
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)

    def calculate_max_health(self):
        return math.floor(self.constitution*10 + self.strength/2)
    
    def calculate_damage(self):
        return math.floor(self.strength * 1.5 + self.dexterity / 4)
    
    def calculate_defense(self):
        return math.floor(self.constitution * 1.5 + self.dexterity / 3)


class Monster(Unit):
    """Создаем дочерний класс - Монстр"""
    def __init__(self, strength, constitution, dexterity=0, wisdom=0, intelligence=0, charisma=0):
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)

    def calculate_max_health(self):
        return math.floor(self.constitution * 8 + self.strength / 3)

    def calculate_damage(self):
        return math.floor(self.strength * 2 + self.constitution / 5)

    def calculate_defense(self):
        return math.floor(self.constitution * 1.2 + self.strength / 5)