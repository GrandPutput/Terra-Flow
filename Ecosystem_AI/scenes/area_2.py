'''
Script: area_2.py
Description: Implements the Area2Screen class, which represents the GUI for Area 2 in the virtual ecosystem.
             Includes methods for interacting with the ecosystem, such as hunting predators, hunting prey,
             collecting herbs, and managing resources.
Author: Patrick Davis
Date: April 5, 2025
Version: 1.0
'''

import tkinter as tk
import random
import numpy as np
from scripts.species_creation import ecosystem, Species, Forest  # Import ecosystem and relevant classes
from scripts.symbolic_ai_test import RuleEngine, rule_resource_health, rule_predator_prey, rule_self_aggression, rule_reproduction  # Import RuleEngine and rules
from scripts.player_stats import Player  # Import Player class
from scripts.neuralnetwork import AI_test  # Import AI_test function
from scenes.training_screens import TrainingScreen  # Import TrainingScreen class


class Area2Screen(tk.Frame):
    '''
    Represents the GUI for Area 2 in the virtual ecosystem.
    Allows the player to interact with the ecosystem by hunting, collecting resources, and managing actions.
    '''

    def __init__(self, parent) -> None:
        '''
        Initialize the Area2Screen with GUI components and buttons for player actions.

        Args:
            parent: The parent object (usually the main application).
        '''
        super().__init__(parent.root)
        self.parent = parent  # Store the parent reference

        # Ecosystem Data Section
        self.ecosystem_label = tk.Label(self, text='Area 2', font=('Arial', 14))
        self.ecosystem_label.pack(pady=10)

        self.ecosystem_data_text = tk.Text(self, wrap='word', height=15, width=80)
        self.ecosystem_data_text.pack(pady=10)

        # Player Data Section
        self.player_label = tk.Label(self, text='Player Data', font=('Arial', 14))
        self.player_label.pack(pady=10)

        self.player_data_text = tk.Text(self, wrap='word', height=7, width=80)
        self.player_data_text.pack(pady=10)

        # Action Buttons Section
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        self.create_action_buttons(button_frame)

    def create_action_buttons(self, button_frame: tk.Frame) -> None:
        '''
        Create action buttons for interacting with the ecosystem.

        Args:
            button_frame (tk.Frame): The frame to hold the buttons.
        '''
        actions = [
            ('Hunt Predator | -3 energy', self.hunt_predator),
            ('Hunt Prey | -2 energy', self.hunt_prey),
            ('Collect Herb | -1 energy', self.collect_herb),
            ('Collect Wood | -4 or (-2 w axe) energy', self.collect_resource),
            ('Plant Tree | -2 energy', self.fix_resource),
            ('Return to Main Area', self.goto_gui),
        ]

        for text, command in actions:
            button = tk.Button(button_frame, text=text, command=command)
            button.pack(side='left', padx=10)

    def update_data(self, ecosystem_data: str, player_data: str) -> None:
        '''
        Update the GUI with the latest ecosystem and player data.

        Args:
            ecosystem_data (str): The updated ecosystem data.
            player_data (str): The updated player data.
        '''
        self.ecosystem_data_text.delete(1.0, tk.END)
        self.ecosystem_data_text.insert(tk.END, ecosystem_data)

        self.player_data_text.delete(1.0, tk.END)
        self.player_data_text.insert(tk.END, player_data)

    def goto_gui(self) -> None:
        '''
        Switch back to the main GUI screen.
        '''
        self.parent.show_frame('gui')

    def refresh_screen(self) -> None:
        '''
        Refresh the screen with updated ecosystem and player data.
        '''
        ecosystem_data = self.parent.get_ecosystem_data_area('Area 2')
        player_data = self.parent.get_player_data()
        self.update_data(ecosystem_data, player_data)
        self.parent.show_frame('Area 2')

    def hunt_predator(self) -> None:
        '''
        Simulate hunting a predator in the ecosystem.
        '''
        self.perform_hunt('carnivores', energy_cost=3, health_loss_ranges=(20, 10, (1, 10)))

    def hunt_prey(self) -> None:
        '''
        Simulate hunting prey in the ecosystem.
        '''
        self.perform_hunt('herbivores', energy_cost=2, health_loss_ranges=(10, 5, (1, 5)))

    def collect_herb(self) -> None:
        '''
        Simulate collecting herbs from the ecosystem.
        '''
        self.perform_collection('herbs', 'Herb', energy_cost=1)

    def collect_resource(self) -> None:
        '''
        Simulate collecting resources (e.g., wood) from the ecosystem.
        '''
        forest = self.get_forest('Area 2')
        player = self.parent.get_player_instance()

        if player.energy >= 4:
            if forest.resources and any(r.current_population > 0 for r in forest.resources):
                resource = random.choice([r for r in forest.resources if r.current_population > 0])
                resource.current_population = max(0, resource.current_population - 1)

                if player.axe:
                    player.energy_change(-2)
                else:
                    player.energy_change(-4)

                player.action_change(-1)
                player.add_item_to_inventory('Wood', 1)
                message = f'You collected Wood x 1! Remaining Trees: {resource.current_population}.'
            else:
                message = 'No Wood left to collect!'
        else:
            message = 'Not enough energy to collect resources!'

        self.update_screen(message)

    def fix_resource(self) -> None:
        '''
        Simulate planting trees to restore resources in the ecosystem.
        '''
        forest = self.get_forest('Area 2')
        player = self.parent.get_player_instance()

        if player.energy >= 2:
            if forest.resources and any(r.current_population < 10 for r in forest.resources):
                resource = random.choice([r for r in forest.resources if r.current_population < 10])
                resource.current_population += 1
                player.energy_change(-2)
                player.action_change(-1)
                message = f'You planted a tree! Remaining Trees: {resource.current_population}.'
            else:
                message = 'The forest is already full of trees!'
        else:
            message = 'Not enough energy to plant trees!'

        self.update_screen(message)

    def perform_hunt(self, target_type: str, energy_cost: int, health_loss_ranges: tuple) -> None:
        '''
        Perform a hunting action (predator or prey).

        Args:
            target_type (str): The type of target to hunt ('carnivores' or 'herbivores').
            energy_cost (int): The energy cost of the action.
            health_loss_ranges (tuple): The health loss ranges for different AI actions.
        '''
        forest = self.get_forest('Area 2')
        player = self.parent.get_player_instance()

        if player.energy >= energy_cost:
            targets = getattr(forest, target_type)
            if targets and any(t.current_population > 0 for t in targets):
                target = random.choice([t for t in targets if t.current_population > 0])
                target.current_population = max(0, target.current_population - 1)

                model = self.parent.trained_model
                if model:
                    game_data = np.array([[player.health, target.current_aggression]]) / 100
                    results = AI_test(model, game_data)

                    if any(action == 'Action' for _, action in results):
                        player.update_health(-health_loss_ranges[0])
                        message = f'You hunted a {target.name}! + 1 Meat | Aggressive behavior caused -{health_loss_ranges[0]} HP.'
                    elif any(action == 'Warning' for _, action in results):
                        player.update_health(-health_loss_ranges[1])
                        message = f'You hunted a {target.name}! + 1 Meat | Warning behavior caused -{health_loss_ranges[1]} HP.'
                    elif any(action == 'Nothing' for _, action in results):
                        random_health_loss = random.randint(*health_loss_ranges[2])
                        player.update_health(-random_health_loss)
                        message = f'You hunted a {target.name}! + 1 Meat | Neutral behavior caused -{random_health_loss} HP.'
                    else:
                        message = 'No action taken by the AI.'
                else:
                    message = 'Error: No trained model available!'
            else:
                message = f'No {target_type[:-1]} left to hunt!'
        else:
            message = f'Not enough energy to hunt {target_type[:-1]}!'

        player.energy_change(-energy_cost)
        player.action_change(-1)
        self.update_screen(message)

    def perform_collection(self, target_type: str, item_name: str, energy_cost: int) -> None:
        '''
        Perform a collection action (e.g., herbs or resources).

        Args:
            target_type (str): The type of target to collect ('herbs' or 'resources').
            item_name (str): The name of the item to add to the inventory.
            energy_cost (int): The energy cost of the action.
        '''
        forest = self.get_forest('Area 2')
        player = self.parent.get_player_instance()

        if player.energy >= energy_cost:
            targets = getattr(forest, target_type)
            if targets and any(t.current_population > 0 for t in targets):
                target = random.choice([t for t in targets if t.current_population > 0])
                target.current_population = max(0, target.current_population - 1)
                player.add_item_to_inventory(item_name, 1)
                message = f'You collected {item_name} x 1! Remaining {target.name}: {target.current_population}.'
            else:
                message = f'No {target_type[:-1]} left to collect!'
        else:
            message = f'Not enough energy to collect {target_type[:-1]}!'

        player.energy_change(-energy_cost)
        player.action_change(-1)
        self.update_screen(message)

    def update_screen(self, message: str) -> None:
        '''
        Update the screen with the latest data and display a message.

        Args:
            message (str): The message to display.
        '''
        ecosystem_data = self.parent.get_ecosystem_data_area('Area 2')
        player_data = self.parent.get_player_data()
        self.update_data(ecosystem_data, player_data)
        self.ecosystem_data_text.insert(tk.END, f'\n{message}')

    def get_forest(self, area_name: str) -> Forest:
        '''
        Retrieve the forest object for the given area.

        Args:
            area_name (str): The name of the area.

        Returns:
            Forest: The forest object for the specified area.
        '''
        for forest in ecosystem:
            if forest.name == area_name:
                return forest
        return None