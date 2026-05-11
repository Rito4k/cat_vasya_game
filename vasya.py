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
    """Класс персонажа с ветвлением логики по игровому классу"""
    def __init__(self, strength, dexterity, constitution, wisdom=0, intelligence=0, charisma=0, character_class='warrior'):
        # Проверяем, что передан допустимый игровой класс
        if character_class not in ('warrior', 'mage', 'hunter'):
            raise ValueError(
                f"Invalid character_class: '{character_class}'. "
                "Must be one of: 'warrior', 'mage', 'hunter'."
            )
        
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)
        self.character_class = character_class
        
        # Считаем стартовые характеристики
        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()

    def calculate_max_health(self):
        """Рассчитывает максимальное здоровье по общей формуле."""
        return math.floor(self.constitution * 10 + self.strength / 2)
    
    def calculate_damage(self):
        """Рассчитывает урон в зависимости от character_class."""
        if self.character_class == 'warrior':
            return math.floor(self.strength * 2.2 + self.constitution / 3)
        elif self.character_class == 'mage':
            return math.floor(self.intelligence * 2.5 + self.wisdom / 2)
        elif self.character_class == 'hunter':
            return math.floor(self.dexterity * 1.9 + self.strength / 3)
        return 0
    
    def calculate_defense(self):
        """Рассчитывает защиту в зависимости от character_class."""
        if self.character_class == 'warrior':
            return math.floor(self.constitution * 1.8 + self.strength / 4)
        elif self.character_class == 'mage':
            return math.floor(self.wisdom * 1.3 + self.intelligence / 6)
        elif self.character_class == 'hunter':
            return math.floor(self.dexterity * 1.6 + self.constitution / 5)
        return 0

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