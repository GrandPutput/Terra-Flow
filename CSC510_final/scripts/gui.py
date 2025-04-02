import tkinter as tk
from scripts.species_creation import ecosystem  # Import the ecosystem list
from scripts.symbolic_ai_test import RuleEngine, rule_resource_health, rule_predator_prey, rule_self_aggression, rule_reproduction
from scripts.player_stats import Player  # Import the Player class
from scenes.area_1 import Area1Screen
from scenes.area_2 import Area2Screen
from scenes.area_3 import Area3Screen
from scenes.gui_screen import GuiScreen
from scenes.training_screens import TrainingScreen, TrainedScreen

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Scene Switching Example")

        # Create a Player instance
        self.player = Player(name="John Doe")  # Replace "John Doe" with actual logic if needed
        
        
        # Initialize all frames (screens)
        self.frames = {}
        
        # Create the frames
        self.frames["Training AI"] = TrainingScreen(self)
        self.frames["Trained AI"] = TrainedScreen(self)
        self.frames["Area 1"] = Area1Screen(self)
        self.frames["Area 2"] = Area2Screen(self)
        self.frames["Area 3"] = Area3Screen(self)
        self.frames["gui"] = GuiScreen(self)

        # Start with the Training AI screen
        self.show_frame("Training AI")
    
    def get_player_instance(self):
        """Return the Player instance."""
        return self.player

    def show_frame(self, frame_name):
        # Hide all frames
        for frame in self.frames.values():
            frame.pack_forget()
        
        # Show the requested frame
        frame = self.frames[frame_name]
        frame.pack(fill="both", expand=True)  # Ensure the frame is packed and displayed
        
        # Map frame names to their corresponding data-fetching methods
        data_fetch_methods = {
            "gui": self.get_ecosystem_data,
            "Area 1": lambda: self.get_ecosystem_data_area("Area 1"),
            "Area 2": lambda: self.get_ecosystem_data_area("Area 2"),
            "Area 3": lambda: self.get_ecosystem_data_area("Area 3"),
        }

        # Fetch and update data if the frame requires it
        if frame_name == "gui":
            ecosystem_data = self.get_ecosystem_data()  # Fetch ecosystem data
            player_data = self.get_player_data()  # Fetch player data
            frame.update_data(ecosystem_data, player_data)  # Update both data
        elif frame_name in data_fetch_methods:
            ecosystem_data = data_fetch_methods[frame_name]()  # Call the appropriate method
            player_data = self.get_player_data()  # Fetch player data
            frame.update_data(ecosystem_data, player_data)  # Pass both arguments

    '''Fetch player data from player_stats.py.'''
    def get_player_data(self):
        from scripts.player_stats import Player  # Import the Player class
        """Fetch player data from the existing Player instance."""
        player = self.player  # Use the existing Player instance
    
        # Use the get_player_info method to fetch player stats
        player_info = player.get_player_info()
        
        # Format player stats into a string
        player_data = (
            f"Name: {player_info['name']}\n"
            f"Health: {player_info['health']}\n"
            f"Energy: {player_info['level']}\n"
            f"Actions: {player_info['actions']}\n"
            f"Inventory: {', '.join([f'{item} (x{count})' for item, count in player_info['inventory'].items()]) if player_info['inventory'] else 'Empty'}"
        )
        return player_data

    def get_ecosystem_data(self):
        """Fetch ecosystem data from species_creation.py."""
        from scripts.species_creation import ecosystem  # Import the ecosystem list
        data = ""
        for forest in ecosystem:
            # Capture the display status of each forest
            forest_status = []
            forest_status.append(f"\n{forest.name} Ecosystem:")
            for carnivore in forest.carnivores:
                forest_status.append(f"Carnivore: {carnivore.name}, Population: {carnivore.current_population}, Health: {carnivore.health}, Aggression: {carnivore.current_aggression}, Prey: {[p.name for p in carnivore.prey]}")
            for herbivore in forest.herbivores:
                forest_status.append(f"Herbivore: {herbivore.name}, Population: {herbivore.current_population}, Health: {herbivore.health}, Aggression: {herbivore.current_aggression}, Predators: {[p.name for p in herbivore.predators]}, Prey: {[p.name for p in herbivore.prey]}")
            for herb in forest.herbs:
                forest_status.append(f"Herb: {herb.name}, Population: {herb.current_population}, Health: {herb.health}, Predators: {[p.name for p in herb.predators]}")
            for resource in forest.resources:
                forest_status.append(f"Resource: {resource.name}, Population: {resource.current_population}")
            data += "\n".join(forest_status) + "\n"
        return data
        
    def get_ecosystem_data_area(self, area):
        """Fetch ecosystem data for Area from species_creation.py."""
        area_check = area
        from scripts.species_creation import ecosystem  # Import the ecosystem list
        data = ""
        for forest in ecosystem:
            if forest.name == area_check:  # Filter forests for Area name
                # Capture the display status of each forest
                forest_status = []
                forest_status.append(f"\n{forest.name} Ecosystem:")
                for carnivore in forest.carnivores:
                    forest_status.append(f"Carnivore: {carnivore.name}, Population: {carnivore.current_population}, Health: {carnivore.health}, Aggression: {carnivore.current_aggression}, Prey: {[p.name for p in carnivore.prey]}")
                for herbivore in forest.herbivores:
                    forest_status.append(f"Herbivore: {herbivore.name}, Population: {herbivore.current_population}, Health: {herbivore.health}, Aggression: {herbivore.current_aggression}, Predators: {[p.name for p in herbivore.predators]}, Prey: {[p.name for p in herbivore.prey]}")
                for herb in forest.herbs:
                    forest_status.append(f"Herb: {herb.name}, Population: {herb.current_population}, Health: {herb.health}, Predators: {[p.name for p in herb.predators]}")
                for resource in forest.resources:
                    forest_status.append(f"Resource: {resource.name}, Population: {resource.current_population}")
                data += "\n".join(forest_status) + "\n"
        return data




if __name__ == "__main__":

    # Initialize the main Tkinter window
    root = tk.Tk()
    root.geometry("900x600")  # Set the window size

    # Create the app and pass the root window to it
    app = App(root)

    # Run the Tkinter main loop
    root.mainloop()