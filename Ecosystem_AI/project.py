'''
Project: Neural Network GUI Application
Description: Virtual Ecosystem Managed by AI systems.
Author: Patrick Davis
Date: April 5, 2025
Version: 1.0
'''

# Import necessary modules
from scripts.neuralnetwork import train_neural, AI_test
import numpy as np
import tkinter as tk
from scripts.gui import App  # Import the App class from gui.py

# Initialize the Tkinter window
root = tk.Tk()
root.geometry("900x600") 

# Create the app
app = App(root)

# Run the Tkinter main loop
root.mainloop()