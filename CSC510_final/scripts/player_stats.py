class Player:
    def __init__(self, name, energy = 10, actions = 10, health=100, armor = 0):
        # Player attributes
        self.name = name
        self.health = health
        self.energy = energy
        self.actions = actions
        self.armor = armor
        self.inventory = {}  # Inventory as a dictionary {item_name: count}

    def add_item_to_inventory(self, item, count=1):
        if item in self.inventory:
            self.inventory[item] += count
        else:
            self.inventory[item] = count

    def remove_item_from_inventory(self, item, count=1):
        if item in self.inventory:
            self.inventory[item] -= count
            if self.inventory[item] <= 0:
                del self.inventory[item]

    def update_health(self, amount):
        self.health += amount
        if self.health < 0:
            self.health = 0
    
    def update_armor(self, amount):
        self.armor += amount

    # Update the player's energy.
    def energy_change(self, amount):
        self.energy += amount

    # Update the player's actions.
    def action_change(self, amount):
        self.actions += amount


    def get_player_info(self):
        # Return a dictionary of the player's current stats.
        return {
            "name": self.name,
            "energy": self.energy,
            "actions": self.actions,
            "health": self.health,
            "inventory": self.inventory,
            "armor": self.armor
        }