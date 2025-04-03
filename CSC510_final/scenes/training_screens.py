import tkinter as tk
import random
from scripts.species_creation import ecosystem, Species, Forest  # Import ecosystem and relevant classes
from scripts.symbolic_ai_test import RuleEngine, rule_resource_health, rule_predator_prey, rule_self_aggression, rule_reproduction  # Import RuleEngine and rules
from scripts.player_stats import Player  # Import Player class
import threading


class TrainingScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent.root)
        self.parent = parent  # Store the parent reference
        
        # Create a label for the Training AI screen
        self.label = tk.Label(self, text="Training AI, please wait...", font=("Arial", 14))
        self.label.pack(pady=30)

        # Add a button to start training
        self.train_button = tk.Button(self, text="Start Training", command=self.start_training)
        self.train_button.pack(pady=10)

        # Add a button to simulate transition to the next screen
        self.next_button = tk.Button(self, text="Next", command=self.goto_trained_screen, state="normal")
        self.next_button.pack(pady=10)

    def start_training(self):
        """Start the AI training process in a separate thread."""
        self.train_button.config(state="disabled")  # Disable the button to prevent multiple clicks
        threading.Thread(target=self.train_ai).start()

    def train_ai(self):
        """Train the AI and enable the 'Next' button after completion."""
        from scripts.neuralnetwork import train_neural  # Import the training function
        self.model = train_neural()  # Train the neural network and store the model as an instance attribute
        self.label.config(text="Training complete!")  # Update the label
        self.next_button.config(state="normal")  # Enable the 'Next' button

    def goto_trained_screen(self):
        """Transition to the Trained AI screen."""
        self.parent.show_frame("Trained AI")


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