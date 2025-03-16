import numpy as np

# Activation function (Sigmoid for hidden layer and Softmax for output, both seen as is on geeks for geeks)
def sigmoid(x):  
    return 1 / (1 + np.exp(-x))

# SoftMax actiation function is for output layer. It transforms data into probabilities
def softmax(x):
    if x.ndim == 1:
        x = x.reshape(1, -1)
    exp_values = np.exp(x - np.max(x, axis=1, keepdims=True))
    return exp_values / exp_values.sum(axis=1, keepdims=True)

# backpropagation 
def sigmoid_derivative(x):
    return x * (1 - x)

# Loss Function
def cross_entropy_loss(y_true, y_pred):
    m = y_true.shape[0]
    return -np.sum(y_true * np.log(y_pred)) / m

# After training, we can test the network on new data
def predict(input_data):
    # Keep data between 0 and 100
    #input_data = np.clip(input_data, 0, 100)

    hidden_layer_input = np.dot(input_data, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)
    
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    output_layer_output = softmax(output_layer_input)
    
    return np.argmax(output_layer_output, axis=1)

# Training dataset (Input HP, Input Agression, # Action)
# Each input feature is [Input HP, Input Agression], and output is the action of the mob
# Add more training data in the future, current set is not enough. AI keeps turning into murder bot.
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

# Parameters
input_size = 2  # Input HP, Input Agression
hidden_size = 4  # Hidden layer neurons
output_size = 3  # Action, Warning, Nothing
learning_rate = 0.1
training_iterations = 20000  # Training iterations, set to 20k for extra training.

# Weights
np.random.seed(69)  # Use seed 69 lol
weights_input_hidden = np.random.randn(input_size, hidden_size)
bias_hidden = np.zeros((1, hidden_size))
weights_hidden_output = np.random.randn(hidden_size, output_size)
bias_output = np.zeros((1, output_size))

# Training loop
for n in range(training_iterations):
    # Forward Pass
    hidden_layer_input = np.dot(training_data, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)
    
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    output_layer_output = softmax(output_layer_input)  # Output probabilities
    
    loss = cross_entropy_loss(labels, output_layer_output)
    
    output_layer_error = output_layer_output - labels
    
    # Backpropagate to hidden layer
    hidden_layer_error = np.dot(output_layer_error, weights_hidden_output.T) * sigmoid_derivative(hidden_layer_output)
    
    # Update weights and biases using gradient descent
    weights_hidden_output -= learning_rate * np.dot(hidden_layer_output.T, output_layer_error)
    bias_output -= learning_rate * np.sum(output_layer_error, axis=0, keepdims=True)
    
    weights_input_hidden -= learning_rate * np.dot(training_data.T, hidden_layer_error)
    bias_hidden -= learning_rate * np.sum(hidden_layer_error, axis=0, keepdims=True)
    
    # Print the loss every 1000 training_iterations
    if n % 1000 == 0:
        print(f"Training iteration {n}, Loss: {loss:.4f}")

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
])
#test_data = np.clip(test_data, 0, 100)

AI_choices = predict(test_data)
actions = ["Agressive Action", "Passive Action", "No Action"]
print("\nChoices after training:")
for i, pred in enumerate(AI_choices):
    print(f"Input {test_data[i]} -> Predicted action: {actions[pred]}")