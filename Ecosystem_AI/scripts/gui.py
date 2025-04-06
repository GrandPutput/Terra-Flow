'''
Script: gui.py
Description: Implements the main GUI application using Tkinter. This script manages scene switching,
             player interactions, and ecosystem data visualization for the virtual ecosystem.
Author: Patrick Davis
Date: April 5, 2025
Version: 1.0
'''
import tkinter as tk
from scripts.species_creation import ecosystem  # Import the ecosystem list
from scripts.symbolic_ai_test import RuleEngine, rule_resource_health, rule_predator_prey, rule_self_aggression, rule_reproduction
from scripts.player_stats import Player  # Import the Player class
from scenes.area_1 import Area1Screen
from scenes.area_2 import Area2Screen
from scenes.area_3 import Area3Screen
from scenes.base import BaseScreen
from scenes.gui_screen import GuiScreen
from scenes.training_screens import TrainingScreen, TrainedScreen
from scripts.house import House  # Import the House class
from scripts.neuralnetwork import train_neural, AI_test


class App:
    def __init__(self, root: tk.Tk) -> None:
        '''
        Initialize the application with the main Tkinter window.

        Args:
            root (tk.Tk): The main Tkinter window.
        '''
        self.root = root
        self.root.title('Scene Switching Example')

        # Create a Player instance
        self.player = Player(name='Ima Borat')  # Temporary name

        # Create a House instance
        self.base = House()

        # Initialize all frames (screens)
        # Designed to mimic video game scene logic
        self.frames = {}

        # Create the frames
        self.frames['Training AI'] = TrainingScreen(self)
        self.frames['Trained AI'] = TrainedScreen(self)
        self.frames['Area 1'] = Area1Screen(self)
        self.frames['Area 2'] = Area2Screen(self)
        self.frames['Area 3'] = Area3Screen(self)
        self.frames['gui'] = GuiScreen(self)
        self.frames['Base'] = BaseScreen(self)

        # Start with the Training AI screen
        self.show_frame('Training AI')

    def get_player_instance(self) -> Player:
        '''Return the Player instance.'''
        return self.player

    def get_base_instance(self) -> House:
        '''Return the House instance.'''
        return self.base

    def show_frame(self, frame_name: str) -> None:
        '''
        Display the specified frame and update its data if necessary.

        Args:
            frame_name (str): The name of the frame to display.
        '''
        # Hide all frames
        for frame in self.frames.values():
            frame.pack_forget()

        # Show the requested frame
        frame = self.frames[frame_name]
        frame.pack(fill='both', expand=True)

        # Map frame names to their corresponding data-fetching methods
        # Data calls get data for respective frames
        data_fetch_methods = {
            'gui': self.get_ecosystem_data,
            'Area 1': lambda: self.get_ecosystem_data_area('Area 1'),
            'Area 2': lambda: self.get_ecosystem_data_area('Area 2'),
            'Area 3': lambda: self.get_ecosystem_data_area('Area 3')
        }

        # Fetch and update data if the frame requires it
        if frame_name == 'gui':
            ecosystem_data = self.get_ecosystem_data()
            player_data = self.get_player_data()
            frame.update_data(ecosystem_data, player_data)
        elif frame_name == 'Base':
            frame.refresh_screen()
        elif frame_name in data_fetch_methods:
            ecosystem_data = data_fetch_methods[frame_name]()
            player_data = self.get_player_data()
            frame.update_data(ecosystem_data, player_data)

    def get_player_data(self) -> str:
        '''
        Fetch player data from the existing Player instance.

        Returns:
            str: Formatted player data.
        '''
        player_info = self.player.get_player_info()
        player_data = (
            f"Name: {player_info['name']}\n"
            f"Health: {player_info['health']}\n"
            f"Armor: {player_info['armor']}\n"
            f"Energy: {player_info['energy']}\n"
            f"Actions: {player_info['actions']}\n"
            f"Inventory: {', '.join([f'{item} (x{count})' for item, count in player_info['inventory'].items()]) if player_info['inventory'] else 'Empty'}"
        )
        return player_data

    def get_base_data(self) -> str:
        '''
        Fetch base data from the existing House instance.

        Returns:
            str: Formatted base data.
        '''
        base_info = self.base.get_house_info()
        base_data = (
            f"Base Health: {base_info['Base Status']}\n"
            f"Walls Status: {'Repaired!' if self.base.walls else 'In need of repair!'}\n"
            f"Farm Status: {'Active!' if self.base.farm else 'Inactive!'}\n"
        )
        return base_data

    def get_ecosystem_data(self) -> str:
        '''
        Fetch ecosystem data from species_creation.py.

        Returns:
            str: Formatted ecosystem data.
        '''
        data = ''
        for forest in ecosystem:
            forest_status = [f'\n{forest.name} Ecosystem:']
            for carnivore in forest.carnivores:
                forest_status.append(
                    f"Carnivore: {carnivore.name}, Population: {carnivore.current_population}, "
                    f"Health: {carnivore.health}, Aggression: {carnivore.current_aggression}, "
                    f"Prey: {[p.name for p in carnivore.prey]}"
                )
            for herbivore in forest.herbivores:
                forest_status.append(
                    f"Herbivore: {herbivore.name}, Population: {herbivore.current_population}, "
                    f"Health: {herbivore.health}, Aggression: {herbivore.current_aggression}, "
                    f"Predators: {[p.name for p in herbivore.predators]}, "
                    f"Prey: {[p.name for p in herbivore.prey]}"
                )
            for herb in forest.herbs:
                forest_status.append(
                    f"Herb: {herb.name}, Population: {herb.current_population}, "
                    f"Health: {herb.health}, Predators: {[p.name for p in herb.predators]}"
                )
            for resource in forest.resources:
                forest_status.append(f"Resource: {resource.name}, Population: {resource.current_population}")
            data += '\n'.join(forest_status) + '\n'
        return data

    def get_ecosystem_data_area(self, area: str) -> str:
        '''
        Fetch ecosystem data for a specific area from species_creation.py.

        Args:
            area (str): The name of the area.

        Returns:
            str: Formatted ecosystem data for the specified area.
        '''
        data = ''
        for forest in ecosystem:
            if forest.name == area:
                forest_status = [f'\n{forest.name} Ecosystem:']
                for carnivore in forest.carnivores:
                    forest_status.append(
                        f"Carnivore: {carnivore.name}, Population: {carnivore.current_population}, "
                        f"Health: {carnivore.health}, Aggression: {carnivore.current_aggression}, "
                        f"Prey: {[p.name for p in carnivore.prey]}"
                    )
                for herbivore in forest.herbivores:
                    forest_status.append(
                        f"Herbivore: {herbivore.name}, Population: {herbivore.current_population}, "
                        f"Health: {herbivore.health}, Aggression: {herbivore.current_aggression}, "
                        f"Predators: {[p.name for p in herbivore.predators]}, "
                        f"Prey: {[p.name for p in herbivore.prey]}"
                    )
                for herb in forest.herbs:
                    forest_status.append(
                        f"Herb: {herb.name}, Population: {herb.current_population}, "
                        f"Health: {herb.health}, Predators: {[p.name for p in herb.predators]}"
                    )
                for resource in forest.resources:
                    forest_status.append(f"Resource: {resource.name}, Population: {resource.current_population}")
                data += '\n'.join(forest_status) + '\n'
        return data


if __name__ == '__main__':
    # Initialize the main Tkinter window
    root = tk.Tk()
    root.geometry('900x600')  # Set the window size

    # Create the app and pass the root window to it
    app = App(root)

    # Run the Tkinter main loop
    root.mainloop()