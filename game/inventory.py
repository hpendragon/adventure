from typing import Dict, List, Optional
from .items import Item, ItemType

class InventorySlot:
    def __init__(self, item: Item, quantity: int = 1):
        self.item = item
        self.quantity = quantity

    def add(self, amount: int = 1) -> int:
        """Add items to slot, return amount that couldn't be added"""
        space_left = self.item.max_stack - self.quantity
        can_add = min(amount, space_left)
        self.quantity += can_add
        return amount - can_add

    def remove(self, amount: int = 1) -> int:
        """Remove items from slot, return amount actually removed"""
        can_remove = min(amount, self.quantity)
        self.quantity -= can_remove
        return can_remove

class Inventory:
    def __init__(self, capacity: int = 20):
        self.capacity = capacity
        self.slots: Dict[int, InventorySlot] = {}
        self.gold = 0

    def add_item(self, item: Item, quantity: int = 1) -> bool:
        """Try to add item to inventory, return True if successful"""
        # First try to stack with existing items
        for slot in self.slots.values():
            if slot.item.id == item.id and slot.quantity < slot.item.max_stack:
                quantity = slot.add(quantity)
                if quantity == 0:
                    return True

        # If we still have items to add, find new slots
        while quantity > 0 and len(self.slots) < self.capacity:
            new_slot_id = self._find_empty_slot()
            if new_slot_id is None:
                return False
            
            new_slot = InventorySlot(item)
            quantity = new_slot.add(quantity)
            self.slots[new_slot_id] = new_slot

        return quantity == 0

    def remove_item(self, item_id: str, quantity: int = 1) -> bool:
        """Try to remove item from inventory, return True if successful"""
        remaining = quantity
        for slot in list(self.slots.values()):
            if slot.item.id == item_id:
                removed = slot.remove(remaining)
                remaining -= removed
                if slot.quantity == 0:
                    self._remove_slot(slot)
                if remaining == 0:
                    return True
        return False

    def get_items_by_type(self, item_type: ItemType) -> List[Item]:
        """Get all items of a specific type"""
        return [
            slot.item for slot in self.slots.values()
            if slot.item.type == item_type
        ]

    def add_gold(self, amount: int):
        """Add gold to inventory"""
        self.gold += amount

    def remove_gold(self, amount: int) -> bool:
        """Remove gold from inventory if possible"""
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False

    def _find_empty_slot(self) -> Optional[int]:
        """Find first empty slot id"""
        for i in range(self.capacity):
            if i not in self.slots:
                return i
        return None

    def _remove_slot(self, slot: InventorySlot):
        """Remove a slot from inventory"""
        for key, value in self.slots.items():
            if value == slot:
                del self.slots[key]
                break
