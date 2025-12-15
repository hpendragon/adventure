class Player:
    def __init__(self):
        self.inventory = []
        self.stats = {
            "health": 100,
            "level": 1,
            "experience": 0
        }
        self.location = "start"

    def update_stats(self, stat, value):
        self.stats[stat] = value

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
