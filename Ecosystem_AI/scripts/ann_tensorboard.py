'''
Script: ann_tensorboard.py
Description: Implements a neural network using TensorFlow/Keras for training and testing AI actions 
             with TensorBoard integration for visualization.
Author: Patrick Davis
Date: April 5, 2025
Version: 1.0
'''

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential  # type: ignore
from tensorflow.keras.layers import Dense, Input  # type: ignore
from tensorflow.keras.optimizers import Adam  # type: ignore
from tensorflow.keras.callbacks import TensorBoard  # type: ignore
import datetime

# Constants
INPUT_SHAPE = (2,)  # Input features: HP and Aggression
OUTPUT_CLASSES = 3  # Output classes: Action, Warning, Nothing
EPOCHS = 200  # Number of training epochs, can be changed to 50: not reccomended
LEARNING_RATE = 0.01  # Learning rate for the optimizer, do not set to 0.1: too high


def train_neural() -> Sequential:
    # Training dataset (Input HP, Input Aggression)
    training_data = np.array([
        [100, 0],  # Nothing (2)
        [70, 0],  # Nothing (2)
        [40, 0],  # Nothing (2)
        [30, 0],  # Warning (1)
        [50, 20],  # Warning (1)
        [90, 50],  # Warning (1)
        [100, 70],  # Action (0)
        [60, 40],  # Action (0)
        [20, 40],  # Action (0),
    ]) / 100.0

    # Labels for the training dataset
    labels = np.array([
        [0, 0, 1],  # Nothing (2)
        [0, 0, 1],  # Nothing (2)
        [0, 0, 1],  # Nothing (2)
        [0, 1, 0],  # Warning (1)
        [0, 1, 0],  # Warning (1)
        [0, 1, 0],  # Warning (1)
        [1, 0, 0],  # Action (0)
        [1, 0, 0],  # Action (0)
        [1, 0, 0],  # Action (0),
    ])

    # Define the model
    model = Sequential([
        Input(shape=INPUT_SHAPE),
        Dense(16, activation='relu'),
        Dense(8, activation='relu'),
        Dense(OUTPUT_CLASSES, activation='softmax')
    ])

    # Compile the model
    model.compile(optimizer=Adam(learning_rate=LEARNING_RATE), 
                  loss='categorical_crossentropy', 
                  metrics=['accuracy'])

    # Create a log directory with a timestamp for TensorBoard
    log_dir = 'logs/fit/' + datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)

    # Train the model
    model.fit(
        training_data,
        labels,
        epochs=EPOCHS,
        verbose=1,
        callbacks=[tensorboard_callback]
    )

    return model


def AI_test(data_model: Sequential, test_data: np.ndarray) -> list[tuple[np.ndarray, str]]:
    '''
    Tests the trained neural network model on test data.

    Args:
        data_model (Sequential): The trained neural network model.
        test_data: The test dataset.

    Returns:
        list[tuple[np.ndarray, str]]: A list of tuples containing input data and predicted actions.
    '''
    # Predict the actions for the test data
    AI_choices = data_model.predict(test_data)

    actions = ['Action', 'Warning', 'Nothing']
    results = []
    for i, pred in enumerate(AI_choices):
        results.append((test_data[i], actions[np.argmax(pred)]))
    return results


def main() -> None:
    '''
    Main function to train the neural network and test it on example data.
    Not called when ran from project.py.
    '''
    # Train the neural network
    trained_AI = train_neural()

    # Example test data (Input HP, Input Aggression)
    test_data = np.array([
        [95, 80],  # Action  
        [50, 15],  # Warning
        [69, 22],  # Nothing
        [100, 100],  # Action
        [20, 30],  # Action  
        [35, 5],  # Warning 
        [80, 49],  # Warning
        [100, 60],  # Nothing  
        [42, 1],  # Nothing
        [50, 9],  # Nothing
    ]) / 100.0

    # Test the AI
    results = AI_test(trained_AI, test_data)

    # Display the results
    print('\nChoices after training:')
    for input_data, action in results:
        print(f'Input {input_data} -> Predicted action: {action}')


if __name__ == '__main__':
    main()