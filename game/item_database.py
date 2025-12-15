from .items import *

# Weapon Templates
WEAPONS = {
    "iron_sword": Weapon(
        id="iron_sword",
        name="Iron Sword",
        type=ItemType.WEAPON,
        subtype=WeaponType.SWORD,
        value=100,
        weight=3.0,
        description="A basic iron sword",
        damage=5,
        damage_type="slash"
    ),
    "magic_staff": Weapon(
        id="magic_staff",
        name="Staff of Magic",
        type=ItemType.WEAPON,
        subtype=WeaponType.STAFF,
        value=300,
        weight=2.0,
        description="A magical staff",
        damage=3,
        damage_type="magic",
        magic_bonuses=[MagicBonus("magic_damage", 2, "Increases magic damage")]
    )
}

# Armor Templates
ARMOR = {
    "leather_armor": Armor(
        id="leather_armor",
        name="Leather Armor",
        type=ItemType.ARMOR,
        subtype=ArmorType.LIGHT,
        value=50,
        weight=8.0,
        description="Basic leather armor",
        defense=3,
        armor_class=11
    )
}

# Potion Templates
POTIONS = {
    "health_potion": Potion(
        id="health_potion",
        name="Health Potion",
        type=ItemType.POTION,
        subtype=PotionType.HEALTH,
        value=50,
        weight=0.5,
        description="Restores 20 health",
        effect_strength=20,
        duration=0,
        max_stack=5
    )
}

# Scroll Templates
SCROLLS = {
    "fireball_scroll": Scroll(
        id="fireball_scroll",
        name="Fireball Scroll",
        type=ItemType.SCROLL,
        subtype=ScrollType.FIREBALL,
        value=100,
        weight=0.1,
        description="Casts a powerful fireball",
        spell_level=3
    )
}
