"""
Файл, содержащий 3 класса и описания их структуры:  
~ Unit (ABC) - абстрактный класс, содержащий все характеристики и абстрактные методы;
~ Character - наследующий класс от Unit реализующий calculate_max_health, calculate_damage и calculate_defense 
с помощью проверки атрибута character_class;
~ Spell (ABC) - абстрактный класс с названием, уроном и стоимостью маны, и хотя бы три конкретных заклинания.
"""

import math
from abc import ABC, abstractmethod


class Unit(ABC):
    """Абстрактный базовый класс для всех игровых сущностей."""
    
    def __init__(self, strength: int, dexterity: int, constitution: int, wisdom: int, intelligence: int, 
                 charisma: int) -> None:
        self.strength: int = strength
        self.dexterity: int = dexterity
        self.constitution: int = constitution
        self.wisdom: int = wisdom
        self.intelligence: int = intelligence
        self.charisma: int = charisma
        self.spells: list = []
        self.mana: int = 0

    @abstractmethod
    def calculate_max_health(self) -> int:
        """Рассчитывает максимальное здоровье."""
        pass

    @abstractmethod
    def calculate_damage(self) -> int:
        """Рассчитывает урон."""
        pass

    @abstractmethod
    def calculate_defense(self) -> int:
        """Рассчитывает защиту."""
        pass

    def add_spell(self, spell: "Spell") -> None:
        """Добавляет заклинание в список доступных."""
        self.spells.append(spell)

    def cast_spell(self, index: int) -> int:
        """Применяет заклинание по индексу, если достаточно маны."""
        if not (0 <= index < len(self.spells)):
            raise IndexError("Spell index out of range.")
            
        spell = self.spells[index]
        if self.mana < spell.mana_cost:
            raise ValueError("Not enough mana to cast this spell.")
            
        self.mana -= spell.mana_cost
        return spell.cast()


class Spell(ABC):
    """Абстрактный базовый класс для заклинаний."""
    
    def __init__(self, name: str, damage: int, mana_cost: int) -> None:
        self.name: str = name
        self.damage: int = damage
        self.mana_cost: int = mana_cost

    @abstractmethod
    def cast(self) -> int:
        """Возвращает итоговый урон или эффект заклинания."""
        pass


class Fireball(Spell):
    """Заклинание 'Огненный шар'."""
    def __init__(self) -> None:
        super().__init__("Fireball", 35, 15)

    def cast(self) -> int:
        return self.damage


class IceLance(Spell):
    """Заклинание 'Ледяное копье'."""
    def __init__(self) -> None:
        super().__init__("IceLance", 25, 10)

    def cast(self) -> int:
        return self.damage


class LightningBolt(Spell):
    """Заклинание 'Молния'."""
    def __init__(self) -> None:
        super().__init__("LightningBolt", 40, 20)

    def cast(self) -> int:
        return self.damage


class Character(Unit):
    """Класс персонажа с ветвлением логики по игровому классу."""
    
    def __init__(self, strength: int, dexterity: int, constitution: int, wisdom: int = 0, intelligence: int = 0, 
                 charisma: int = 0, character_class: str = 'warrior') -> None:
        if character_class not in ('warrior', 'mage', 'hunter'):
            raise ValueError(f"Invalid character_class: '{character_class}'. Must be 'warrior', 'mage' or 'hunter'.")
        
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)
        self.character_class: str = character_class
        self.max_health: int = self.calculate_max_health()
        self.current_health: int = self.max_health
        self.damage: int = self.calculate_damage()
        self.defense: int = self.calculate_defense()
        self.mana: int = self.calculate_max_mana()

    def calculate_max_mana(self) -> int:
        """Рассчитывает максимальную ману в зависимости от character_class."""
        if self.character_class == 'warrior':
            return math.floor(self.intelligence + self.strength / 2)
        elif self.character_class == 'mage':
            return math.floor(self.intelligence * 3 + self.wisdom)
        elif self.character_class == 'hunter':
            return math.floor(self.dexterity * 1.5 + self.wisdom / 2)
        return 0

    def calculate_max_health(self) -> int:
        """Рассчитывает максимальное здоровье по общей формуле."""
        return math.floor(self.constitution * 10 + self.strength / 2)
    
    def calculate_damage(self) -> int:
        """Рассчитывает урон в зависимости от character_class."""
        if self.character_class == 'warrior':
            return math.floor(self.strength * 2.2 + self.constitution / 3)
        elif self.character_class == 'mage':
            return math.floor(self.intelligence * 2.5 + self.wisdom / 2)
        elif self.character_class == 'hunter':
            return math.floor(self.dexterity * 1.9 + self.strength / 3)
        return 0
    
    def calculate_defense(self) -> int:
        """Рассчитывает защиту в зависимости от character_class."""
        if self.character_class == 'warrior':
            return math.floor(self.constitution * 1.8 + self.strength / 4)
        elif self.character_class == 'mage':
            return math.floor(self.wisdom * 1.3 + self.intelligence / 6)
        elif self.character_class == 'hunter':
            return math.floor(self.dexterity * 1.6 + self.constitution / 5)
        return 0


class Monster(Unit):
    """Класс монстра."""
    
    def __init__(self, strength: int, constitution: int, dexterity: int = 0, wisdom: int = 0, 
                 intelligence: int = 0, charisma: int = 0) -> None:
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)

    def calculate_max_health(self) -> int:
        """Рассчитывает максимальное здоровье монстра."""
        return math.floor(self.constitution * 8 + self.strength / 3)

    def calculate_damage(self) -> int:
        """Рассчитывает урон монстра."""
        return math.floor(self.strength * 2 + self.constitution / 5)

    def calculate_defense(self) -> int:
        """Рассчитывает защиту монстра."""
        return math.floor(self.constitution * 1.2 + self.strength / 5)