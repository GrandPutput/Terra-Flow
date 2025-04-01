import tkinter as tk
import random
from species_creation import ecosystem, Species, Forest  # Import ecosystem and relevant classes
from symbolic_ai_test import RuleEngine, rule_resource_health, rule_predator_prey, rule_self_aggression, rule_reproduction  # Import RuleEngine and rules

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
        
        # Create a label for the GUI screen
        self.label = tk.Label(self, text="Ecosystem Data", font=("Arial", 14))
        self.label.pack(pady=10)

        # Add a text widget to display ecosystem data
        self.data_text = tk.Text(self, wrap="word", height=30, width=80)
        self.data_text.pack(pady=10)

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


    def update_data(self, data):
        """Update the text widget with ecosystem data."""
        self.data_text.delete(1.0, tk.END)  # Clear existing text
        self.data_text.insert(tk.END, data)  # Insert new data

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
        
        # Create a label for the GUI screen
        self.label = tk.Label(self, text="Area 1", font=("Arial", 14))
        self.label.pack(pady=10)

        # Add a text widget to display ecosystem data
        self.data_text = tk.Text(self, wrap="word", height=30, width=80)
        self.data_text.pack(pady=10)

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

    def update_data(self, data):
        """Update the text widget with ecosystem data."""
        self.data_text.delete(1.0, tk.END)  # Clear existing text
        self.data_text.insert(tk.END, data)  # Insert new data

    def goto_gui(self):
        # Switch back to the Training AI screen
        self.parent.show_frame("gui")

    def refresh_screen(self):
        # Switch back to the Training AI screen
        self.parent.show_frame("Area 1")

    def hunt_predator(self):
        """Simulate hunting a predator."""
        forest = self.get_forest("Area 1")
        if forest.carnivores and any(c.current_population > 0 for c in forest.carnivores):
            predator = random.choice([c for c in forest.carnivores if c.current_population > 0])
            predator.current_population = max(0, predator.current_population - 1)
            self.update_data(f"You hunted a {predator.name}! Remaining population: {predator.current_population}.")
        else:
            self.update_data("No predators left to hunt!")
        # Refresh Screen
        self.after(3000, self.refresh_screen)





# Add refresf to each function!!!!!!!!!!!!!!!!





    def hunt_prey(self):
        """Simulate hunting prey."""
        forest = self.get_forest("Area 1")
        if forest.herbivores and any(h.current_population > 0 for h in forest.herbivores):
            prey = random.choice([h for h in forest.herbivores if h.current_population > 0])
            prey.current_population = max(0, prey.current_population - 1)
            self.update_data(f"You hunted a {prey.name}! Remaining population: {prey.current_population}.")
        else:
            self.update_data("No prey left to hunt!")

    def collect_herb(self):
        """Simulate collecting herbs."""
        forest = self.get_forest("Area 1")
        if forest.herbs and any(h.current_population > 0 for h in forest.herbs):
            herb = random.choice([h for h in forest.herbs if h.current_population > 0])
            herb.current_population = max(0, herb.current_population - 1)
            self.update_data(f"You collected {herb.name}! Remaining population: {herb.current_population}.")
        else:
            self.update_data("No herbs left to collect!")

    def collect_resource(self):
        """Simulate collecting resources."""
        forest = self.get_forest("Area 1")
        if forest.resources and any(r.current_population > 0 for r in forest.resources):
            resource = random.choice([r for r in forest.resources if r.current_population > 0])
            resource.current_population = max(0, resource.current_population - 1)
            self.update_data(f"You collected {resource.name}! Remaining population: {resource.current_population}.")
        else:
            self.update_data("No resources left to collect!")

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
        
        # Create a label for the GUI screen
        self.label = tk.Label(self, text="Area 2", font=("Arial", 14))
        self.label.pack(pady=10)

        # Add a text widget to display ecosystem data
        self.data_text = tk.Text(self, wrap="word", height=30, width=80)
        self.data_text.pack(pady=10)

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

    def update_data(self, data):
        """Update the text widget with ecosystem data."""
        self.data_text.delete(1.0, tk.END)  # Clear existing text
        self.data_text.insert(tk.END, data)  # Insert new data

    def goto_gui(self):
        # Switch back to the Training AI screen
        self.parent.show_frame("gui")

    def hunt_predator(self):
        """Simulate hunting a predator."""
        forest = self.get_forest("Area 2")
        if forest.carnivores and any(c.current_population > 0 for c in forest.carnivores):
            predator = random.choice([c for c in forest.carnivores if c.current_population > 0])
            predator.current_population = max(0, predator.current_population - 1)
            self.update_data(f"You hunted a {predator.name}! Remaining population: {predator.current_population}.")
        else:
            self.update_data("No predators left to hunt!")

    def hunt_prey(self):
        """Simulate hunting prey."""
        forest = self.get_forest("Area 2")
        if forest.herbivores and any(h.current_population > 0 for h in forest.herbivores):
            prey = random.choice([h for h in forest.herbivores if h.current_population > 0])
            prey.current_population = max(0, prey.current_population - 1)
            self.update_data(f"You hunted a {prey.name}! Remaining population: {prey.current_population}.")
        else:
            self.update_data("No prey left to hunt!")

    def collect_herb(self):
        """Simulate collecting herbs."""
        forest = self.get_forest("Area 2")
        if forest.herbs and any(h.current_population > 0 for h in forest.herbs):
            herb = random.choice([h for h in forest.herbs if h.current_population > 0])
            herb.current_population = max(0, herb.current_population - 1)
            self.update_data(f"You collected {herb.name}! Remaining population: {herb.current_population}.")
        else:
            self.update_data("No herbs left to collect!")

    def collect_resource(self):
        """Simulate collecting resources."""
        forest = self.get_forest("Area 2")
        if forest.resources and any(r.current_population > 0 for r in forest.resources):
            resource = random.choice([r for r in forest.resources if r.current_population > 0])
            resource.current_population = max(0, resource.current_population - 1)
            self.update_data(f"You collected {resource.name}! Remaining population: {resource.current_population}.")
        else:
            self.update_data("No resources left to collect!")

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
        
        # Create a label for the GUI screen
        self.label = tk.Label(self, text="Area 3", font=("Arial", 14))
        self.label.pack(pady=10)

        # Add a text widget to display ecosystem data
        self.data_text = tk.Text(self, wrap="word", height=30, width=80)
        self.data_text.pack(pady=10)

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

    def update_data(self, data):
        """Update the text widget with ecosystem data."""
        self.data_text.delete(1.0, tk.END)  # Clear existing text
        self.data_text.insert(tk.END, data)  # Insert new data

    def goto_gui(self):
        # Switch back to the Training AI screen
        self.parent.show_frame("gui")

    def hunt_predator(self):
        """Simulate hunting a predator."""
        forest = self.get_forest("Area 3")
        if forest.carnivores and any(c.current_population > 0 for c in forest.carnivores):
            predator = random.choice([c for c in forest.carnivores if c.current_population > 0])
            predator.current_population = max(0, predator.current_population - 1)
            self.update_data(f"You hunted a {predator.name}! Remaining population: {predator.current_population}.")
        else:
            self.update_data("No predators left to hunt!")

    def hunt_prey(self):
        """Simulate hunting prey."""
        forest = self.get_forest("Area 3")
        if forest.herbivores and any(h.current_population > 0 for h in forest.herbivores):
            prey = random.choice([h for h in forest.herbivores if h.current_population > 0])
            prey.current_population = max(0, prey.current_population - 1)
            self.update_data(f"You hunted a {prey.name}! Remaining population: {prey.current_population}.")
        else:
            self.update_data("No prey left to hunt!")

    def collect_herb(self):
        """Simulate collecting herbs."""
        forest = self.get_forest("Area 3")
        if forest.herbs and any(h.current_population > 0 for h in forest.herbs):
            herb = random.choice([h for h in forest.herbs if h.current_population > 0])
            herb.current_population = max(0, herb.current_population - 1)
            self.update_data(f"You collected {herb.name}! Remaining population: {herb.current_population}.")
        else:
            self.update_data("No herbs left to collect!")

    def collect_resource(self):
        """Simulate collecting resources."""
        forest = self.get_forest("Area 3")
        if forest.resources and any(r.current_population > 0 for r in forest.resources):
            resource = random.choice([r for r in forest.resources if r.current_population > 0])
            resource.current_population = max(0, resource.current_population - 1)
            self.update_data(f"You collected {resource.name}! Remaining population: {resource.current_population}.")
        else:
            self.update_data("No resources left to collect!")

    def get_forest(self, area_name):
        """Retrieve the forest object for the given area."""
        for forest in ecosystem:
            if forest.name == area_name:
                return forest
        return None
