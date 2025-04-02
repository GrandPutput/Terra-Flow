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