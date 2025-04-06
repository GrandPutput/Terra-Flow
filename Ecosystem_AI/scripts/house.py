'''
Script: house.py
Description: Defines the House class, which represents the player's base in the virtual ecosystem. 
             Includes attributes and methods for managing the base's health, walls, and farm status.
Author: Patrick Davis
Date: April 5, 2025
Version: 1.0
'''

class House:
    '''
    Represents the player's base with attributes for health, walls, and farm status.
    Provides methods to update these attributes and retrieve the base's current state.
    '''

    def __init__(self, health: int = 100) -> None:
        '''
        Initialize the House instance with default attributes.

        Args:
            health (int): The initial health of the base. Defaults to 100.
        '''
        self.health = health
        self.walls = False
        self.farm = False

    def update_health(self, amount: int) -> None:
        '''
        Update the health of the base by a specified amount.

        Args:
            amount (int): The amount to adjust the base's health by.
        '''
        self.health += amount
        if self.health < 0:
            self.health = 0

    def set_walls(self) -> None:
        '''
        Toggle the walls status of the base. 
        Adds 50 health when walls are built, and subtracts 50 health when removed.
        This is called when species raid occurs.
        '''
        if not self.walls:
            self.walls = True
            self.health += 50
        else:
            self.walls = False
            self.health -= 50

    def set_farm(self) -> None:
        '''
        Toggle the farm status of the base.
        '''
        self.farm = not self.farm

    def get_house_info(self) -> dict[str, object]:
        '''
        Retrieve the current state of the base.
        This is called when species raid occurs.

        Returns:
            dict[str, object]: A dictionary containing the base's health, walls status, and farm status.
        '''
        return {
            'Base Status': self.health,
            'Walls Status': self.walls,
            'Farm Status': self.farm
        }

