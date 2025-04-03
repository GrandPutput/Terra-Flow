import tkinter as tk
import random
from scripts.species_creation import ecosystem, Species, Forest  # Import ecosystem and relevant classes
from scripts.symbolic_ai_test import RuleEngine, rule_resource_health, rule_predator_prey, rule_self_aggression, rule_reproduction  # Import RuleEngine and rules
from scripts.player_stats import Player  # Import Player class

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

        # Button Enter Home
        self.back_button = tk.Button(self, text="Go To Base", command=self.goto_base)
        self.back_button.pack(side="left", padx=10)


    '''Update GUI output'''
    def update_data(self, ecosystem_data, player_data):
        # Update Ecosystem data
        self.ecosystem_data_text.delete(1.0, tk.END)  # Clear existing text
        self.ecosystem_data_text.insert(tk.END, ecosystem_data)  # Insert new data
        # Update player data
        self.player_data_text.delete(1.0, tk.END)  # Clear existing text
        self.player_data_text.insert(tk.END, player_data)  # Insert new data


    def goto_area1(self):
        self.parent.show_frame("Area 1")

    def goto_area2(self):
        self.parent.show_frame("Area 2")

    def goto_area3(self):
        self.parent.show_frame("Area 3")

    def goto_base(self):
        self.parent.show_frame("Base")