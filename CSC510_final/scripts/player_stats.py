class Player:
    def __init__(self, name, energy = 10, actions = 10, health=100):
        # Player attributes
        self.name = name
        self.health = health
        self.energy = energy
        self.actions = actions
        self.inventory = {}  # Inventory as a dictionary {item_name: count}
    
    '''def get_player_instance(self):
        return self.player'''

    def add_item_to_inventory(self, item, count=1):
        """
        Add an item to the player's inventory or increase its count.
        :param item: Item to add
        :param count: Number of items to add (default is 1)
        """
        if item in self.inventory:
            self.inventory[item] += count
        else:
            self.inventory[item] = count

    def remove_item_from_inventory(self, item, count=1):
        """
        Remove an item or decrease its count in the player's inventory.
        :param item: Item to remove
        :param count: Number of items to remove (default is 1)
        """
        if item in self.inventory:
            self.inventory[item] -= count
            if self.inventory[item] <= 0:
                del self.inventory[item]

    def update_health(self, amount):
        self.health += amount
        if self.health < 0:
            self.health = 0

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
            "level": self.energy,
            "actions": self.actions,
            "health": self.health,
            "inventory": self.inventory
        }