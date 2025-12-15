from enum import Enum
from dataclasses import dataclass
from typing import Optional, List, Dict

class ItemType(Enum):
    WEAPON = "weapon"
    ARMOR = "armor"
    POTION = "potion"
    SCROLL = "scroll"
    CURRENCY = "currency"

class ArmorType(Enum):
    LIGHT = "light"
    MEDIUM = "medium"
    HEAVY = "heavy"
    SHIELD = "shield"

class WeaponType(Enum):
    SWORD = "sword"
    AXE = "axe"
    BOW = "bow"
    DAGGER = "dagger"
    STAFF = "staff"
    WAND = "wand"

class PotionType(Enum):
    HEALTH = "health"
    MANA = "mana"
    STRENGTH = "strength"
    DEFENSE = "defense"
    SPEED = "speed"

class ScrollType(Enum):
    FIREBALL = "fireball"
    HEALING = "healing"
    TELEPORT = "teleport"
    IDENTIFY = "identify"
    ENCHANT = "enchant"

@dataclass
class MagicBonus:
    type: str
    value: int
    description: str

@dataclass
class Item:
    id: str
    name: str
    type: ItemType
    subtype: Optional[Enum]
    value: int
    weight: float
    description: str
    magic_bonuses: List[MagicBonus] = None
    stack_size: int = 1
    max_stack: int = 1

    def __post_init__(self):
        if self.magic_bonuses is None:
            self.magic_bonuses = []

@dataclass
class Weapon(Item):
    damage: int
    damage_type: str
    
@dataclass
class Armor(Item):
    defense: int
    armor_class: int

@dataclass
class Potion(Item):
    effect_strength: int
    duration: int

@dataclass
class Scroll(Item):
    spell_level: int
    uses: int = 1
