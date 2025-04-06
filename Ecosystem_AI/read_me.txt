# Ecosystem Simulation Game
This project is a ecosystem simulation that combines symbolic AI, neural networks, and a graphical user interface (GUI) to simulate an ecosystem.
Players can interact with the ecosystem, manage resources, and make decisions that affect the environment and their survival.

# Features
- Ecosystem Simulation: Simulates interactions between species, resources, and the environment.
- Symbolic AI: Uses rules to model species behavior and ecosystem dynamics.
- Neural Networks: Predicts actions based on player and species attributes.
- Graphical User Interface: Provides an interactive interface for players to explore areas, manage resources, and make decisions.

# Prerequisites
- Python 3.10 or higher
- Required Python libraries:
    - 'numpy'
    - 'tensorflow'
    - 'tkinter'
    - 'threading'
    - 'random'
    - 'datetime'
    - 'tensorboard'

# Structure
-Main Folder
    - project.py (main executable)
    - logs       (contains tensorboard data)
    - pdfs       (contains game flow charts)
    - scenes     (contains frame data)
    - scripts    (contains AI methods and classification scripts)

# Gameplay Instructions
1. Training AI: The game starts with training the AI. Wait for the training to complete.
	Option to move to next is in bypass mode to skip training the ANN.
	This is so you can interact with the GUI without training the ANN.
	While the GUI will still change screens, the functions will not work.
	This is only to view the GUI only.
	Train the AI for the full experience!
2. Exploring Areas: Use the GUI to explore different areas ('Area 1', 'Area 2', 'Area 3', 'Base') and interact with the ecosystem.
   - Hunt predators or prey.
	This triggers the ANN to determine NPC behavior.
   - Collect herbs or resources.
   - Plant trees to restore resources to fix your damage.
3. Base Management: Return to the base to manage your resources and craft items.
   - Build a farm.
   - Craft tools like spears, shields, and axes.
   - Heal or sleep to restore energy and health.
	This triggers the AI to adjust behaviors and recover populations.
	This triggers the ANN to determine NPC behavior.


# Key Classes and Functions
- Player Management**:
  - [`Player`](scripts/player_stats.py): Manages player attributes and inventory.
- Ecosystem Simulation**:
  - [`Species`](scripts/species_creation.py): Represents species in the ecosystem.
  - [`Forest`](scripts/species_creation.py): Represents an ecosystem area.
- AI**:
  - 'train_neural'(scripts/neuralnetwork.py): Trains the neural network.
  - 'AI_test'(scripts/neuralnetwork.py): Tests the neural network.
  - 'RuleEngine'(scripts/symbolic_ai_test.py): Evaluates symbolic AI rules.
- GUI**:
  - 'App'(scripts/gui.py): Main GUI application.
  - Area screens: 'Area1Screen', 'Area2Screen', 'Area3Screen' in 'scenes/'.

# Notes

- The game uses TensorFlow for neural network training. Ensure your system supports TensorFlow.
- TensorBoard logs are stored in the 'logs/' directory for debugging and visualization.

*****ENJOY*****
