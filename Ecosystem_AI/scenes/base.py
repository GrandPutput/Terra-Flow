'''
Script: base.py
Description: Implements the BaseScreen class, which represents the GUI for the player's base in the virtual ecosystem.
             Includes methods for managing player actions, crafting items, building farms, and interacting with the rule engine.
Author: Patrick Davis
Date: April 5, 2025
Version: 1.0
'''

import tkinter as tk
import random
import numpy as np
from scripts.player_stats import Player
from scripts.house import House
from scenes.training_screens import TrainingScreen
from scripts.neuralnetwork import AI_test
from scripts.symbolic_ai_test import RuleEngine, rule_resource_health, rule_self_aggression, rule_predator_prey, rule_reproduction


class BaseScreen(tk.Frame):
    '''
    Represents the GUI for the player's base in the virtual ecosystem.
    Allows the player to manage their base, craft items, and interact with the rule engine.
    '''

    def __init__(self, parent) -> None:
        '''
        Initialize the BaseScreen with GUI elements and the rule engine.

        Args:
            parent: The parent object (usually the main application).
        '''
        super().__init__(parent.root)
        self.parent = parent

        # Initialize the Rule Engine
        self.rule_engine = RuleEngine()
        self.rule_engine.add_rule(rule_resource_health)
        self.rule_engine.add_rule(rule_self_aggression)
        self.rule_engine.add_rule(rule_predator_prey)
        self.rule_engine.add_rule(rule_reproduction)

        # Initialize context for the Rule Engine
        self.context = {
            'species': self.get_species_data(),
            'resources': self.get_resource_data()
        }

        # Initialize GUI elements
        self.init_gui()

    def get_species_data(self) -> list:
        '''
        Retrieve species data for the rule engine context.

        Returns:
            list: A list of species objects from the ecosystem.
        '''
        from scripts.species_creation import ecosystem
        species = []
        for forest in ecosystem:
            species.extend(forest.carnivores + forest.herbivores + forest.herbs)
        return species

    def get_resource_data(self) -> list:
        '''
        Retrieve resource data for the rule engine context.

        Returns:
            list: A list of resource objects from the ecosystem.
        '''
        from scripts.species_creation import ecosystem
        resources = []
        for forest in ecosystem:
            resources.extend(forest.resources)
        return resources

    def update_context(self) -> None:
        '''
        Update the context with the latest species and resource data.
        '''
        self.context['species'] = self.get_species_data()
        self.context['resources'] = self.get_resource_data()

    def init_gui(self) -> None:
        '''
        Initialize the GUI elements for the BaseScreen.
        '''
        # Player Data Section
        self.player_label = tk.Label(self, text='Player Data', font=('Arial', 14))
        self.player_label.pack(pady=10)
        self.player_data_text = tk.Text(self, wrap='word', height=7, width=80)
        self.player_data_text.pack(pady=10)

        # Base Data Section
        self.base_label = tk.Label(self, text='Base Data', font=('Arial', 14))
        self.base_label.pack(pady=10)
        self.base_data_text = tk.Text(self, wrap='word', height=7, width=80)
        self.base_data_text.pack(pady=10)

        # Action Buttons
        buttons = [
            ('Eat Food', self.eat_meat),
            ('Heal HP', self.heal_hp),
            ('Build Farm', self.build_farm),
            ('Craft Spear', self.craft_spear),
            ('Craft Shield', self.craft_shield),
            ('Craft Axe', self.craft_axe),
            ('Sleep', self.sleep),
            ('Leave Base', self.goto_gui),
        ]
        for text, command in buttons:
            tk.Button(self, text=text, command=command).pack(side='left', padx=10)

    def update_data(self, player_data: str, base_data: str) -> None:
        '''
        Update the GUI with the latest player and base data.

        Args:
            player_data (str): The updated player data.
            base_data (str): The updated base data.
        '''
        self.player_data_text.delete(1.0, tk.END)
        self.player_data_text.insert(tk.END, player_data)
        self.base_data_text.delete(1.0, tk.END)
        self.base_data_text.insert(tk.END, base_data)

    def refresh_screen(self) -> None:
        '''
        Refresh the screen with updated ecosystem and player data.
        '''
        player_data = self.parent.get_player_data()
        base_data = self.parent.get_base_data()
        self.update_data(player_data, base_data)

    def eat_meat(self) -> None:
        '''
        Handle the action of eating meat.
        '''
        player = self.parent.get_player_instance()
        if 'Meat' in player.inventory and player.energy <= 100:
            player.remove_item_from_inventory('Meat')
            player.energy_change(3)
            player.action_change(-1)
            message = 'Meat eaten successfully.'
        else:
            message = 'Not able to eat meat.'

        self._update_and_display_message(message)

    def heal_hp(self) -> None:
        '''
        Handle the action of healing HP.
        '''
        player = self.parent.get_player_instance()
        if 'Herb' in player.inventory and player.health < 100:
            player.remove_item_from_inventory('Herb')
            player.update_health(30)
            player.action_change(-1)
            message = 'Player healed 30 HP.'
        elif player.health >= 100:
            message = 'Player already at max health.'
        else:
            message = 'No herb in inventory.'

        self._update_and_display_message(message)

    def build_farm(self) -> None:
        '''
        Handle the action of building a farm.
        '''
        base = self.parent.get_base_instance()
        player = self.parent.get_player_instance()
        if player.inventory.get('Wood', 0) < 5 or player.energy < 5:
            message = 'Not enough wood or energy to build farm.'
        elif not base.farm:
            player.remove_item_from_inventory('Wood', 5)
            player.energy_change(-5)
            player.action_change(-1)
            base.set_farm()
            message = 'Farm built successfully!'
        else:
            message = 'Farm already built.'

        self._update_and_display_message(message)

    def craft_item(self, item_name: str, wood_required: int, energy_required: int, set_item_method: str, item_flag: str) -> None:
        '''
        Generic method to handle crafting items.

        Args:
            item_name (str): The name of the item to craft.
            wood_required (int): The amount of wood required to craft the item.
            energy_required (int): The energy required to craft the item.
            set_item_method (str): The method to set the crafted item.
            item_flag (str): The attribute flag indicating if the item is already crafted.
        '''
        player = self.parent.get_player_instance()
        if player.inventory.get('Wood', 0) < wood_required or player.energy < energy_required:
            message = f'Not enough resources to craft {item_name}.'
        elif not getattr(player, item_flag):
            player.remove_item_from_inventory('Wood', wood_required)
            player.energy_change(-energy_required)
            player.action_change(-1)
            getattr(player, set_item_method)()
            message = f'{item_name} crafted successfully!'
        else:
            message = f'{item_name} already crafted.'

        self._update_and_display_message(message)

    def craft_spear(self) -> None:
        '''
        Handle the action of crafting a spear.
        '''
        self.craft_item('Spear', 3, 5, 'set_spear', 'spear')

    def craft_shield(self) -> None:
        '''
        Handle the action of crafting a shield.
        '''
        self.craft_item('Shield', 3, 5, 'set_shield', 'shield')

    def craft_axe(self) -> None:
        '''
        Handle the action of crafting an axe.
        '''
        self.craft_item('Axe', 2, 5, 'set_axe', 'axe')

    def sleep(self) -> None:
        '''
        Handle the action of sleeping.
        '''
        player = self.parent.get_player_instance()
        base = self.parent.get_base_instance()
        player.energy = 10
        player.actions = 10

        # Update context and evaluate rules
        self.update_context()
        self.rule_engine.evaluate(self.context)

        # Check for farm raids
        farm_raid_chance = self.check_aggressive_prey()
        if 'Action' in farm_raid_chance and base.farm:
            message = 'Aggressive prey raided the farm! They ate all your crops!'
            base.set_farm()
        elif 'Warning' in farm_raid_chance and base.farm:
            if random.randint(1, 2) == 1:
                message = 'Agitated prey raided the farm! They ate all your crops!'
                base.set_farm()
            else:
                message = 'Agitated prey are nearby. Stay alert!'
        else:
            message = 'You sleep peacefully.'

        self._update_and_display_message(message)

    def check_aggressive_prey(self) -> str:
        '''
        Use ANN to check for aggressive prey actions.

        Returns:
            str: The result of the AI test for aggressive prey.
        '''
        model = self.parent.trained_model
        base = self.parent.get_base_instance()
        from scripts.species_creation import ecosystem

        species_action = ''
        for forest in ecosystem:
            forest_status = [f'\n{forest.name} Ecosystem:']
            for herbivore in forest.herbivores:
                game_data = np.array([[base.health, herbivore.current_aggression]]) / 100.0
                results = AI_test(model, game_data)
                forest_status.append(str(results))
            species_action += '\n'.join(forest_status) + '\n'
        return species_action

    def goto_gui(self) -> None:
        '''
        Switch to the main GUI.
        '''
        self.parent.show_frame('gui')

    def _update_and_display_message(self, message: str) -> None:
        '''
        Helper method to update data and display a message.

        Args:
            message (str): The message to display.
        '''
        player_data = self.parent.get_player_data()
        base_data = self.parent.get_base_data()
        self.update_data(player_data, base_data)
        self.player_data_text.insert(tk.END, f'\n{message}')