import tkinter as tk
import random
from scripts.species_creation import ecosystem, Species, Forest  # Import ecosystem and relevant classes
from scripts.symbolic_ai_test import RuleEngine, rule_resource_health, rule_predator_prey, rule_self_aggression, rule_reproduction  # Import RuleEngine and rules
from scripts.player_stats import Player  # Import Player class

class TrainingScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent.root)
        self.parent = parent  # Store the parent reference
        
        # Create a label for the Training AI screen
        self.label = tk.Label(self, text="Training AI, please wait...", font=("Arial", 14))
        self.label.pack(pady=30)

        # Add a button to simulate transition to the next screen
        self.next_button = tk.Button(self, text="Next", command=self.goto_gui)
        self.next_button.pack(pady=10)

    def goto_gui(self):
        # Transition to the GUI screen
        self.parent.show_frame("gui")


class TrainedScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent.root)
        self.parent = parent  # Store the parent reference
        
        # Create a label for the Training AI screen
        self.label = tk.Label(self, text="AI is trained, continue when ready!", font=("Arial", 14))
        self.label.pack(pady=30)

        # Add a button to simulate transition to the next screen
        self.next_button = tk.Button(self, text="Next", command=self.goto_gui)
        self.next_button.pack(pady=10)

    def goto_gui(self):
        # Transition to the GUI screen
        self.parent.show_frame("gui")

class GuiScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent.root)
        self.parent = parent  # Store the parent reference
        
        '''Ecosystem Data'''
        # Create a label for the GUI screen
        self.ecosystem_label = tk.Label(self, text="Ecosystem Data", font=("Arial", 14))
        self.ecosystem_label.pack(pady=10)
        # Add a text widget to display ecosystem data
        self.ecosystem_data_text = tk.Text(self, wrap="word", height=15, width=80)
        self.ecosystem_data_text.pack(pady=10)

        '''Player Data'''
        # Create a label for the GUI screen
        self.player_label = tk.Label(self, text="Player Data", font=("Arial", 14))
        self.player_label.pack(pady=10)
        # Add a text widget to display player data
        self.player_data_text = tk.Text(self, wrap="word", height=7, width=80)
        self.player_data_text.pack(pady=10)

        ''' AREA CHANGE BUTTONS '''
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        # Button to change area 1
        self.back_button = tk.Button(self, text="Explore Area 1", command=self.goto_area1)
        self.back_button.pack(side="left", padx=10)

        # Button to change area 2
        self.back_button = tk.Button(self, text="Explore Area 2", command=self.goto_area2)
        self.back_button.pack(side="left", padx=10)

        # Button to change area 3
        self.back_button = tk.Button(self, text="Explre Area 3", command=self.goto_area3)
        self.back_button.pack(side="left", padx=10)

        '''
        Add button to imporve house
        Add button to farm
        Add button to eat
        Add button to craft
        Add button to sleep
        '''

    '''Update GUI output'''
    def update_data(self, ecosystem_data, player_data):
        # Update Ecosystem data
        self.ecosystem_data_text.delete(1.0, tk.END)  # Clear existing text
        self.ecosystem_data_text.insert(tk.END, ecosystem_data)  # Insert new data
        # Update player data
        self.player_data_text.delete(1.0, tk.END)  # Clear existing text
        self.player_data_text.insert(tk.END, player_data)  # Insert new data


    def goto_area1(self):
        # Switch back to the Training AI screen
        self.parent.show_frame("Area 1")

    def goto_area2(self):
        # Switch back to the Training AI screen
        self.parent.show_frame("Area 2")

    def goto_area3(self):
        # Switch back to the Training AI screen
        self.parent.show_frame("Area 3")

class Area1Screen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent.root)
        self.parent = parent  # Store the parent reference
        
        '''Ecosystem Data'''
        # Create a label for the GUI screen
        self.ecosystem_label = tk.Label(self, text="Area 1", font=("Arial", 14))
        self.ecosystem_label.pack(pady=10)
        # Add a text widget to display ecosystem data
        self.ecosystem_data_text = tk.Text(self, wrap="word", height=15, width=80)
        self.ecosystem_data_text.pack(pady=10)

        '''Player Data'''
        # Create a label for the GUI screen
        self.player_label = tk.Label(self, text="Player Data", font=("Arial", 14))
        self.player_label.pack(pady=10)
        # Add a text widget to display player data
        self.player_data_text = tk.Text(self, wrap="word", height=7, width=80)
        self.player_data_text.pack(pady=10)

        ''' AREA CHANGE BUTTONS '''
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        # Button to Hunt Predator
        self.back_button = tk.Button(self, text="Hunt Predator | -3 energy", command=self.hunt_predator)
        self.back_button.pack(side="left", padx=10)

        # Button to Hunt Prey
        self.back_button = tk.Button(self, text="Hunt Prey | -2 energy", command=self.hunt_prey)
        self.back_button.pack(side="left", padx=10)

        # Button to Collect Herb
        self.back_button = tk.Button(self, text="Collect Herb | -1 energy", command=self.collect_herb)
        self.back_button.pack(side="left", padx=10)
        
        # Button to Collect Resource
        self.back_button = tk.Button(self, text="Collect Resource | -2 energy", command=self.collect_resource)
        self.back_button.pack(side="left", padx=10)

        # Button to Areas
        self.back_button = tk.Button(self, text="Return to Main Area", command=self.goto_gui)
        self.back_button.pack(side="left", padx=10)

    '''Update GUI output'''
    def update_data(self, ecosystem_data, player_data):
        # Update Ecosystem data
        self.ecosystem_data_text.delete(1.0, tk.END)  # Clear existing text
        self.ecosystem_data_text.insert(tk.END, ecosystem_data)  # Insert new data
        # Update player data
        self.player_data_text.delete(1.0, tk.END)  # Clear existing text
        self.player_data_text.insert(tk.END, player_data)  # Insert new data

    def goto_gui(self):
        # Switch back to the Training AI screen
        self.parent.show_frame("gui")

    def refresh_screen(self):
        """Refresh the screen with updated ecosystem and player data."""
        # Fetch updated ecosystem and player data
        ecosystem_data = self.parent.get_ecosystem_data_area("Area 1")
        player_data = self.parent.get_player_data()

        # Update the screen with both ecosystem and player data
        self.update_data(ecosystem_data, player_data)

        # Switch back to the current screen
        self.parent.show_frame("Area 1")

    def hunt_predator(self):
        """Simulate hunting a predator."""
        forest = self.get_forest("Area 1")
        if forest.carnivores and any(c.current_population > 0 for c in forest.carnivores):
            predator = random.choice([c for c in forest.carnivores if c.current_population > 0])
            predator.current_population = max(0, predator.current_population - 1)
            message = f"You hunted a {predator.name}! Remaining population: {predator.current_population}."
        else:
            message = "No predators left to hunt!"

        '''Update Player action/energy'''
        # Get the player instance
        player = self.parent.get_player_instance()
        # Update player data (energy, actions)
        player.energy_change(-3)  # Decrease energy by 3
        player.action_change(-1)  # Decrease actions by 1

        # Fetch updated ecosystem and player data
        ecosystem_data = self.parent.get_ecosystem_data_area("Area 1")
        player_data = self.parent.get_player_data()

        # Update the screen with both ecosystem and player data
        self.update_data(ecosystem_data, player_data)

        # Display the hunt message
        self.ecosystem_data_text.insert(tk.END, f"\n{message}")

        # Refresh Screen
        self.after(3000, self.refresh_screen)

    def hunt_prey(self):
        """Simulate hunting prey."""
        forest = self.get_forest("Area 1")
        if forest.herbivores and any(h.current_population > 0 for h in forest.herbivores):
            prey = random.choice([h for h in forest.herbivores if h.current_population > 0])
            prey.current_population = max(0, prey.current_population - 1)
            message = (f"You hunted a {prey.name}! Remaining population: {prey.current_population}.")
        else:
            message = ("No prey left to hunt!")

        '''Update Player action/energy'''
        # Get the player instance
        player = self.parent.get_player_instance()
        player.energy_change(-2) # Decrease energy by 2
        player.action_change(-1) # Decrease actions by 1

        # Fetch updated ecosystem and player data
        ecosystem_data = self.parent.get_ecosystem_data_area("Area 1")
        player_data = self.parent.get_player_data()

        # Update the screen with both ecosystem and player data
        self.update_data(ecosystem_data, player_data)

        # Display the hunt message
        self.ecosystem_data_text.insert(tk.END, f"\n{message}")

        # Refresh Screen
        self.after(3000, self.refresh_screen)

    def collect_herb(self):
        """Simulate collecting herbs."""
        forest = self.get_forest("Area 1")
        if forest.herbs and any(h.current_population > 0 for h in forest.herbs):
            herb = random.choice([h for h in forest.herbs if h.current_population > 0])
            herb.current_population = max(0, herb.current_population - 1)
            message = (f"You collected {herb.name}! Remaining population: {herb.current_population}.")
        else:
            message = ("No herbs left to collect!")

        '''Update player data (energy, actions)'''
        # Get the player instance
        player = self.parent.get_player_instance()
        player.energy_change(-1)  # Decrease energy by 1
        player.action_change(-1)  # Decrease actions by 1

        # Fetch updated ecosystem and player data
        ecosystem_data = self.parent.get_ecosystem_data_area("Area 1")
        player_data = self.parent.get_player_data()

        # Update the screen with both ecosystem and player data
        self.update_data(ecosystem_data, player_data)

        # Display the hunt message
        self.ecosystem_data_text.insert(tk.END, f"\n{message}")

        # Refresh Screen
        self.after(3000, self.refresh_screen)

    def collect_resource(self):
        """Simulate collecting resources."""
        forest = self.get_forest("Area 1")
        if forest.resources and any(r.current_population > 0 for r in forest.resources):
            resource = random.choice([r for r in forest.resources if r.current_population > 0])
            resource.current_population = max(0, resource.current_population - 1)
            message = (f"You collected {resource.name}! Remaining population: {resource.current_population}.")
        else:
            message = ("No resources left to collect!")

        '''Update Player action/energy'''
        # Get the player instance
        player = self.parent.get_player_instance()
        # Update player data (energy, actions)
        player.energy_change(-3)  # Decrease energy by 3
        player.action_change(-1)  # Decrease actions by 1

        # Fetch updated ecosystem and player data
        ecosystem_data = self.parent.get_ecosystem_data_area("Area 1")
        player_data = self.parent.get_player_data()

        # Update the screen with both ecosystem and player data
        self.update_data(ecosystem_data, player_data)

        # Display the hunt message
        self.ecosystem_data_text.insert(tk.END, f"\n{message}")

        # Refresh Screen
        self.after(3000, self.refresh_screen)

    def get_forest(self, area_name):
        """Retrieve the forest object for the given area."""
        for forest in ecosystem:
            if forest.name == area_name:
                return forest
        return None

class Area2Screen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent.root)
        self.parent = parent  # Store the parent reference
        
        '''Ecosystem Data'''
        # Create a label for the GUI screen
        self.ecosystem_label = tk.Label(self, text="Area 2", font=("Arial", 14))
        self.ecosystem_label.pack(pady=10)
        # Add a text widget to display ecosystem data
        self.ecosystem_data_text = tk.Text(self, wrap="word", height=15, width=80)
        self.ecosystem_data_text.pack(pady=10)

        '''Player Data'''
        # Create a label for the GUI screen
        self.player_label = tk.Label(self, text="Player Data", font=("Arial", 14))
        self.player_label.pack(pady=10)
        # Add a text widget to display player data
        self.player_data_text = tk.Text(self, wrap="word", height=7, width=80)
        self.player_data_text.pack(pady=10)

        ''' AREA CHANGE BUTTONS '''
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        # Button to Hunt Predator
        self.back_button = tk.Button(self, text="Hunt Predator | -3 energy", command=self.hunt_predator)
        self.back_button.pack(side="left", padx=10)

        # Button to Hunt Prey
        self.back_button = tk.Button(self, text="Hunt Prey | -2 energy", command=self.hunt_prey)
        self.back_button.pack(side="left", padx=10)

        # Button to Collect Herb
        self.back_button = tk.Button(self, text="Collect Herb | -1 energy", command=self.collect_herb)
        self.back_button.pack(side="left", padx=10)
        
        # Button to Collect Resource
        self.back_button = tk.Button(self, text="Collect Resource | -2 energy", command=self.collect_resource)
        self.back_button.pack(side="left", padx=10)

        # Button to Areas
        self.back_button = tk.Button(self, text="Return to Main Area", command=self.goto_gui)
        self.back_button.pack(side="left", padx=10)

    '''Update GUI output'''
    def update_data(self, ecosystem_data, player_data):
        # Update Ecosystem data
        self.ecosystem_data_text.delete(1.0, tk.END)  # Clear existing text
        self.ecosystem_data_text.insert(tk.END, ecosystem_data)  # Insert new data
        # Update player data
        self.player_data_text.delete(1.0, tk.END)  # Clear existing text
        self.player_data_text.insert(tk.END, player_data)  # Insert new data

    def goto_gui(self):
        # Switch back to the Training AI screen
        self.parent.show_frame("gui")

    def refresh_screen(self):
        """Refresh the screen with updated ecosystem and player data."""
        # Fetch updated ecosystem and player data
        ecosystem_data = self.parent.get_ecosystem_data_area("Area 2")
        player_data = self.parent.get_player_data()

        # Update the screen with both ecosystem and player data
        self.update_data(ecosystem_data, player_data)

        # Switch back to the current screen
        self.parent.show_frame("Area 2")

    def hunt_predator(self):
            """Simulate hunting a predator."""
            forest = self.get_forest("Area 2")
            if forest.carnivores and any(c.current_population > 0 for c in forest.carnivores):
                predator = random.choice([c for c in forest.carnivores if c.current_population > 0])
                predator.current_population = max(0, predator.current_population - 1)
                message = f"You hunted a {predator.name}! Remaining population: {predator.current_population}."
            else:
                message = "No predators left to hunt!"

            '''Update Player action/energy'''
            # Get the player instance
            player = self.parent.get_player_instance()
            # Update player data (energy, actions)
            player.energy_change(-3)  # Decrease energy by 3
            player.action_change(-1)  # Decrease actions by 1

            # Fetch updated ecosystem and player data
            ecosystem_data = self.parent.get_ecosystem_data_area("Area 2")
            player_data = self.parent.get_player_data()

            # Update the screen with both ecosystem and player data
            self.update_data(ecosystem_data, player_data)

            # Display the hunt message
            self.ecosystem_data_text.insert(tk.END, f"\n{message}")

            # Refresh Screen
            self.after(3000, self.refresh_screen)

    def hunt_prey(self):
        """Simulate hunting prey."""
        forest = self.get_forest("Area 2")
        if forest.herbivores and any(h.current_population > 0 for h in forest.herbivores):
            prey = random.choice([h for h in forest.herbivores if h.current_population > 0])
            prey.current_population = max(0, prey.current_population - 1)
            message = (f"You hunted a {prey.name}! Remaining population: {prey.current_population}.")
        else:
            message = ("No prey left to hunt!")

        '''Update Player action/energy'''
        # Get the player instance
        player = self.parent.get_player_instance()
        player.energy_change(-2) # Decrease energy by 2
        player.action_change(-1) # Decrease actions by 1

        # Fetch updated ecosystem and player data
        ecosystem_data = self.parent.get_ecosystem_data_area("Area 2")
        player_data = self.parent.get_player_data()

        # Update the screen with both ecosystem and player data
        self.update_data(ecosystem_data, player_data)

        # Display the hunt message
        self.ecosystem_data_text.insert(tk.END, f"\n{message}")

        # Refresh Screen
        self.after(3000, self.refresh_screen)

    def collect_herb(self):
        """Simulate collecting herbs."""
        forest = self.get_forest("Area 2")
        if forest.herbs and any(h.current_population > 0 for h in forest.herbs):
            herb = random.choice([h for h in forest.herbs if h.current_population > 0])
            herb.current_population = max(0, herb.current_population - 1)
            message = (f"You collected {herb.name}! Remaining population: {herb.current_population}.")
        else:
            message = ("No herbs left to collect!")

        '''Update player data (energy, actions)'''
        # Get the player instance
        player = self.parent.get_player_instance()
        player.energy_change(-1)  # Decrease energy by 1
        player.action_change(-1)  # Decrease actions by 1

        # Fetch updated ecosystem and player data
        ecosystem_data = self.parent.get_ecosystem_data_area("Area 2")
        player_data = self.parent.get_player_data()

        # Update the screen with both ecosystem and player data
        self.update_data(ecosystem_data, player_data)

        # Display the hunt message
        self.ecosystem_data_text.insert(tk.END, f"\n{message}")

        # Refresh Screen
        self.after(3000, self.refresh_screen)

    def collect_resource(self):
        """Simulate collecting resources."""
        forest = self.get_forest("Area 2")
        if forest.resources and any(r.current_population > 0 for r in forest.resources):
            resource = random.choice([r for r in forest.resources if r.current_population > 0])
            resource.current_population = max(0, resource.current_population - 1)
            message = (f"You collected {resource.name}! Remaining population: {resource.current_population}.")
        else:
            message = ("No resources left to collect!")

        '''Update Player action/energy'''
        # Get the player instance
        player = self.parent.get_player_instance()
        # Update player data (energy, actions)
        player.energy_change(-3)  # Decrease energy by 3
        player.action_change(-1)  # Decrease actions by 1

        # Fetch updated ecosystem and player data
        ecosystem_data = self.parent.get_ecosystem_data_area("Area 2")
        player_data = self.parent.get_player_data()

        # Update the screen with both ecosystem and player data
        self.update_data(ecosystem_data, player_data)

        # Display the hunt message
        self.ecosystem_data_text.insert(tk.END, f"\n{message}")

        # Refresh Screen
        self.after(3000, self.refresh_screen)

    def get_forest(self, area_name):
        """Retrieve the forest object for the given area."""
        for forest in ecosystem:
            if forest.name == area_name:
                return forest
        return None

class Area3Screen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent.root)
        self.parent = parent  # Store the parent reference
        
        '''Ecosystem Data'''
        # Create a label for the GUI screen
        self.ecosystem_label = tk.Label(self, text="Area 3", font=("Arial", 14))
        self.ecosystem_label.pack(pady=10)
        # Add a text widget to display ecosystem data
        self.ecosystem_data_text = tk.Text(self, wrap="word", height=15, width=80)
        self.ecosystem_data_text.pack(pady=10)

        '''Player Data'''
        # Create a label for the GUI screen
        self.player_label = tk.Label(self, text="Player Data", font=("Arial", 14))
        self.player_label.pack(pady=10)
        # Add a text widget to display player data
        self.player_data_text = tk.Text(self, wrap="word", height=7, width=80)
        self.player_data_text.pack(pady=10)

        ''' AREA CHANGE BUTTONS '''
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        # Button to Hunt Predator
        self.back_button = tk.Button(self, text="Hunt Predator", command=self.hunt_predator)
        self.back_button.pack(side="left", padx=10)

        # Button to Hunt Prey
        self.back_button = tk.Button(self, text="Hunt Prey", command=self.hunt_prey)
        self.back_button.pack(side="left", padx=10)

        # Button to Collect Herb
        self.back_button = tk.Button(self, text="Collect Herb", command=self.collect_herb)
        self.back_button.pack(side="left", padx=10)
        
        # Button to Collect Resource
        self.back_button = tk.Button(self, text="Collect Resource", command=self.collect_resource)
        self.back_button.pack(side="left", padx=10)

        # Button to Areas
        self.back_button = tk.Button(self, text="Return to Main Area", command=self.goto_gui)
        self.back_button.pack(side="left", padx=10)

    '''Update GUI output'''
    def update_data(self, ecosystem_data, player_data):
        # Update Ecosystem data
        self.ecosystem_data_text.delete(1.0, tk.END)  # Clear existing text
        self.ecosystem_data_text.insert(tk.END, ecosystem_data)  # Insert new data
        # Update player data
        self.player_data_text.delete(1.0, tk.END)  # Clear existing text
        self.player_data_text.insert(tk.END, player_data)  # Insert new data


    def goto_gui(self):
        # Switch back to the Training AI screen
        self.parent.show_frame("gui")

    def refresh_screen(self):
        # Switch back to the Training AI screen
        self.parent.show_frame("Area 3")

    def hunt_predator(self):
        """Simulate hunting a predator."""
        forest = self.get_forest("Area 3")
        if forest.carnivores and any(c.current_population > 0 for c in forest.carnivores):
            predator = random.choice([c for c in forest.carnivores if c.current_population > 0])
            predator.current_population = max(0, predator.current_population - 1)
            message = f"You hunted a {predator.name}! Remaining population: {predator.current_population}."
        else:
            message = "No predators left to hunt!"

        '''Update Player action/energy'''
        # Get the player instance
        player = self.parent.get_player_instance()
        # Update player data (energy, actions)
        player.energy_change(-3)  # Decrease energy by 3
        player.action_change(-1)  # Decrease actions by 1

        # Fetch updated ecosystem and player data
        ecosystem_data = self.parent.get_ecosystem_data_area("Area 3")
        player_data = self.parent.get_player_data()

        # Update the screen with both ecosystem and player data
        self.update_data(ecosystem_data, player_data)

        # Display the hunt message
        self.ecosystem_data_text.insert(tk.END, f"\n{message}")

        # Refresh Screen
        self.after(3000, self.refresh_screen)

    def hunt_prey(self):
        """Simulate hunting prey."""
        forest = self.get_forest("Area 3")
        if forest.herbivores and any(h.current_population > 0 for h in forest.herbivores):
            prey = random.choice([h for h in forest.herbivores if h.current_population > 0])
            prey.current_population = max(0, prey.current_population - 1)
            message = (f"You hunted a {prey.name}! Remaining population: {prey.current_population}.")
        else:
            message = ("No prey left to hunt!")

        '''Update Player action/energy'''
        # Get the player instance
        player = self.parent.get_player_instance()
        player.energy_change(-2) # Decrease energy by 2
        player.action_change(-1) # Decrease actions by 1

        # Fetch updated ecosystem and player data
        ecosystem_data = self.parent.get_ecosystem_data_area("Area 3")
        player_data = self.parent.get_player_data()

        # Update the screen with both ecosystem and player data
        self.update_data(ecosystem_data, player_data)

        # Display the hunt message
        self.ecosystem_data_text.insert(tk.END, f"\n{message}")

        # Refresh Screen
        self.after(3000, self.refresh_screen)

    def collect_herb(self):
        """Simulate collecting herbs."""
        forest = self.get_forest("Area 3")
        if forest.herbs and any(h.current_population > 0 for h in forest.herbs):
            herb = random.choice([h for h in forest.herbs if h.current_population > 0])
            herb.current_population = max(0, herb.current_population - 1)
            message = (f"You collected {herb.name}! Remaining population: {herb.current_population}.")
        else:
            message = ("No herbs left to collect!")

        '''Update player data (energy, actions)'''
        # Get the player instance
        player = self.parent.get_player_instance()
        player.energy_change(-1)  # Decrease energy by 1
        player.action_change(-1)  # Decrease actions by 1

        # Fetch updated ecosystem and player data
        ecosystem_data = self.parent.get_ecosystem_data_area("Area 3")
        player_data = self.parent.get_player_data()

        # Update the screen with both ecosystem and player data
        self.update_data(ecosystem_data, player_data)

        # Display the hunt message
        self.ecosystem_data_text.insert(tk.END, f"\n{message}")

        # Refresh Screen
        self.after(3000, self.refresh_screen)

    def collect_resource(self):
        """Simulate collecting resources."""
        forest = self.get_forest("Area 3")
        if forest.resources and any(r.current_population > 0 for r in forest.resources):
            resource = random.choice([r for r in forest.resources if r.current_population > 0])
            resource.current_population = max(0, resource.current_population - 1)
            message = (f"You collected {resource.name}! Remaining population: {resource.current_population}.")
        else:
            message = ("No resources left to collect!")

        '''Update Player action/energy'''
        # Get the player instance
        player = self.parent.get_player_instance()
        # Update player data (energy, actions)
        player.energy_change(-3)  # Decrease energy by 3
        player.action_change(-1)  # Decrease actions by 1

        # Fetch updated ecosystem and player data
        ecosystem_data = self.parent.get_ecosystem_data_area("Area 3")
        player_data = self.parent.get_player_data()

        # Update the screen with both ecosystem and player data
        self.update_data(ecosystem_data, player_data)

        # Display the hunt message
        self.ecosystem_data_text.insert(tk.END, f"\n{message}")

        # Refresh Screen
        self.after(3000, self.refresh_screen)

    def get_forest(self, area_name):
        """Retrieve the forest object for the given area."""
        for forest in ecosystem:
            if forest.name == area_name:
                return forest
        return None
