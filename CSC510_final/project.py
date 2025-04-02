#from neuralnetwork import train_neural, AI_test
import numpy as np
import tkinter as tk
from scripts.gui import App  # Import the App class from gui.py


'''
# Train the neural network
model = train_neural()

# Test the model with new data
test_data = np.array([
    [95, 80], # Action  
    [50, 15], # Warning
    [69, 22], # Nothing
    [100, 100], # Action
    [20, 30], # Action  
    [35, 5], # Warning 
    [80, 49], # Warning
    [100, 60], # Nothing  
    [42, 1], # Nothing
    [50, 9], # Nothing
]) / 100.0

results = AI_test(model, test_data)
print("Predictions:")
for input_data, action in results:
    print(f"Input {input_data} -> Predicted action: {action}")
'''

root = tk.Tk()
root.geometry("900x600")  # Set the window size

# Create the app and pass the root window to it
app = App(root)

# Run the Tkinter main loop
root.mainloop()