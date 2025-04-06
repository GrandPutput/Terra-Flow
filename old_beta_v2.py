import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense  # type: ignore
from tensorflow.keras.optimizers import Adam  # type: ignore

# Training dataset (Input HP, Input Aggression, # Action)
training_data = np.array([
    [100, 0], # Nothing (2)
    [70, 0], # Nothing (2)
    [40, 0], # Nothing (2)
    [30, 0], # Warning (1)
    [50, 20], # Warning (1)
    [90, 50], # Warning (1)
    [100, 70], # Action (0)
    [60, 40], # Action (0)
    [20, 40], # Action (0)
]) / 100.0

# Keep labels match training data
labels = np.array([
    [0, 0, 1], # Nothing (2)
    [0, 0, 1], # Nothing (2)
    [0, 0, 1], # Nothing (2)
    [0, 1, 0], # Warning (1)
    [0, 1, 0], # Warning (1)
    [0, 1, 0], # Warning (1)
    [1, 0, 0], # Action (0)
    [1, 0, 0], # Action (0)
    [1, 0, 0], # Action (0)
])

# Define the model with additional hidden layers
model = Sequential([
    Dense(8, input_dim=2, activation='relu'),  # First hidden layer with 8 neurons
    Dense(4, activation='relu'),  # Second hidden layer with 4 neurons
    Dense(3, activation='softmax')  # Output layer with 3 neurons
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.1), loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(training_data, labels, epochs=200, verbose=1)

# Test data to check the AI
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

# Predict the actions for the test data
AI_choices = model.predict(test_data)
actions = ["Agressive Action", "Warning Action", "No Action"]
print("\nChoices after training:")
for i, pred in enumerate(AI_choices):
    print(f"Input {test_data[i]} -> Predicted action: {actions[np.argmax(pred)]}")
