'''
Script: training_screens.py
Description: Implements the TrainingScreen and TrainedScreen classes.
Author: Patrick Davis
Date: April 5, 2025
Version: 1.0
'''

import tkinter as tk
import threading
from scripts.neuralnetwork import train_neural  # Import the training function


class TrainingScreen(tk.Frame):
    '''
    Represents the GUI screen for training the AI in the virtual ecosystem.
    Allows the user to start the training process and transition to the next screen upon completion.
    '''

    def __init__(self, parent) -> None:
        '''
        Initialize the TrainingScreen with GUI components.

        Args:
            parent: The parent object (usually the main application).
        '''
        super().__init__(parent.root)
        self.parent = parent  # Store the parent reference

        # Create a label for the Training AI screen
        self.label = tk.Label(self, text='Training AI, please wait...', font=('Arial', 14))
        self.label.pack(pady=30)

        # Add a button to start training
        self.train_button = tk.Button(self, text='Start Training', command=self.start_training)
        self.train_button.pack(pady=10)

        # Add a button to simulate transition to the next screen
        self.next_button = tk.Button(self, text='Next', command=self.goto_trained_screen, state='normal') # Set to normal for GUI testing
        self.next_button.pack(pady=10)

    def start_training(self) -> None:
        '''
        Start the AI training process in a separate thread.
        '''
        self.train_button.config(state='disabled')  # Disable the button to prevent multiple clicks
        threading.Thread(target=self.train_ai).start()

    def train_ai(self) -> None:
        '''
        Train the AI and enable the 'Next' button after completion.
        '''
        trained_model = train_neural()  # Train the neural network and store the model as an instance attribute
        self.parent.trained_model = trained_model  # Store the trained model in the parent object
        self.label.config(text='Training complete!')  # Update the label
        self.next_button.config(state='normal')  # Enable the 'Next' button

    @staticmethod
    def get_model(parent) -> object:
        '''
        Return the trained model from the parent object.

        Args:
            parent: The parent object (usually the main application).

        Returns:
            object: The trained model.
        '''
        return parent.trained_model  # Return the stored trained model

    def goto_trained_screen(self) -> None:
        '''
        Transition to the Trained AI screen.
        '''
        self.parent.show_frame('Trained AI')


class TrainedScreen(tk.Frame):
    '''
    Represents the GUI screen for the trained AI state in the virtual ecosystem.
    Allows the user to transition to the main GUI screen after training is complete.
    '''

    def __init__(self, parent) -> None:
        '''
        Initialize the TrainedScreen with GUI components.

        Args:
            parent: The parent object (usually the main application).
        '''
        super().__init__(parent.root)
        self.parent = parent  # Store the parent reference

        # Create a label for the Trained AI screen
        self.label = tk.Label(self, text='AI is trained, continue when ready!', font=('Arial', 14))
        self.label.pack(pady=30)

        # Add a button to transition to the main GUI screen
        self.next_button = tk.Button(self, text='Next', command=self.goto_gui)
        self.next_button.pack(pady=10)

    def goto_gui(self) -> None:
        '''
        Transition to the main GUI screen.
        '''
        self.parent.show_frame('gui')