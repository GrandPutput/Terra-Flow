'''
Script: player_stats.py
Description: Defines the Player class, which represents the player in the virtual ecosystem. 
             Includes attributes and methods for managing player stats, inventory, and equipment.
Author: Patrick Davis
Date: April 5, 2025
Version: 1.0
'''

class Player:
    '''
    Represents the player with attributes for health, energy, actions, armor, inventory, and equipment.
    Provides methods to update these attributes and retrieve the player's current state.
    '''

    def __init__(self, name: str, energy: int = 10, actions: int = 10, health: int = 100, armor: int = 0) -> None:
        '''
        Initialize the Player instance with default attributes.

        Args:
            name (str): The name of the player.
            energy (int): The initial energy of the player. Defaults to 10.
            actions (int): The initial number of actions available to the player. Defaults to 10.
            health (int): The initial health of the player. Defaults to 100.
            armor (int): The initial armor value of the player. Defaults to 0.
        '''
        self.name = name
        self.health = health
        self.energy = energy
        self.actions = actions
        self.armor = armor
        self.spear = False
        self.shield = False
        self.axe = False
        self.inventory = {}  # Inventory as a dictionary {item_name: count}

    def add_item_to_inventory(self, item: str, count: int = 1) -> None:
        '''
        Add an item to the player's inventory.

        Args:
            item (str): The name of the item to add.
            count (int): The quantity of the item to add. Defaults to 1.
        '''
        if item in self.inventory:
            self.inventory[item] += count
        else:
            self.inventory[item] = count

    def remove_item_from_inventory(self, item: str, count: int = 1) -> None:
        '''
        Remove an item from the player's inventory.

        Args:
            item (str): The name of the item to remove.
            count (int): The quantity of the item to remove. Defaults to 1.
        '''
        if item in self.inventory:
            self.inventory[item] -= count
            if self.inventory[item] <= 0:
                del self.inventory[item]

    def update_health(self, amount: int) -> None:
        '''
        Update the player's health by a specified amount.

        Args:
            amount (int): The amount to adjust the player's health by.
        '''
        self.health += amount
        if self.health < 0:
            self.health = 0

    def update_armor(self, amount: int) -> None:
        '''
        Update the player's armor by a specified amount.

        Args:
            amount (int): The amount to adjust the player's armor by.
        '''
        self.armor += amount

    def energy_change(self, amount: int) -> None:
        '''
        Update the player's energy by a specified amount.

        Args:
            amount (int): The amount to adjust the player's energy by.
        '''
        self.energy += amount

    def action_change(self, amount: int) -> None:
        '''
        Update the player's actions by a specified amount.

        Args:
            amount (int): The amount to adjust the player's actions by.
        '''
        self.actions += amount

    def set_spear(self) -> None:
        '''
        Toggle the spear status of the player.
        Adds 10 armor when equipped, and removes 10 armor when unequipped.
        '''
        if not self.spear:
            self.spear = True
            self.update_armor(10)
        else:
            self.spear = False
            self.update_armor(-10)

    def set_shield(self) -> None:
        '''
        Toggle the shield status of the player.
        Adds 10 armor when equipped, and removes 10 armor when unequipped.
        '''
        if not self.shield:
            self.shield = True
            self.update_armor(10)
        else:
            self.shield = False
            self.update_armor(-10)

    def set_axe(self) -> None:
        '''
        Toggle the axe status of the player.
        Adds 5 armor when equipped, and removes 5 armor when unequipped.
        '''
        if not self.axe:
            self.axe = True
            self.update_armor(5)
        else:
            self.axe = False
            self.update_armor(-5)

    def get_player_info(self) -> dict[str, object]:
        '''
        Retrieve the current state of the player.

        Returns:
            dict[str, object]: A dictionary containing the player's stats, inventory, and equipment status.
        '''
        return {
            'name': self.name,
            'energy': self.energy,
            'actions': self.actions,
            'health': self.health + self.armor,
            'inventory': self.inventory,
            'armor': self.armor,
            'spear': self.spear,
            'shield': self.shield,
            'axe': self.axe
        }