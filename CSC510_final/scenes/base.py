import tkinter as tk
from scripts.player_stats import Player  # Import Player class
from scripts.house import House  # Import the House class

class BaseScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent.root)
        self.parent = parent  # Store the parent reference

        '''Player Data'''
        # Create a label for the GUI screen
        self.player_label = tk.Label(self, text="Player Data", font=("Arial", 14))
        self.player_label.pack(pady=10)
        # Add a text widget to display player data
        self.player_data_text = tk.Text(self, wrap="word", height=7, width=80)
        self.player_data_text.pack(pady=10)

        '''Base Data'''
        # Create a label for the base data
        self.base_label = tk.Label(self, text="Base Data", font=("Arial", 14))
        self.base_label.pack(pady=10)
        # Add a text widget to display base data
        self.base_data_text = tk.Text(self, wrap="word", height=7, width=80)
        self.base_data_text.pack(pady=10)

        # Button to eat meat
        self.eat_food_button = tk.Button(self, text="Eat Food", command=self.eat_meat)
        self.eat_food_button.pack(side="left", padx=10)

        # Button to heal
        self.heal_hp_button = tk.Button(self, text="Heal HP", command=self.heal_hp)
        self.heal_hp_button.pack(side="left", padx=10)

        # Button to change GUI
        self.leave_base_button = tk.Button(self, text="Leave Base", command=self.goto_gui)
        self.leave_base_button.pack(side="left", padx=10)

    def refresh_screen(self):
        """Refresh the screen with updated ecosystem and player data."""
        player_data = self.parent.get_player_data()
        base_data = self.parent.get_base_data() 

        # Update the text widgets with the new data
        self.player_data_text.delete(1.0, tk.END)
        self.player_data_text.insert(tk.END, player_data)

        self.base_data_text.delete(1.0, tk.END)
        self.base_data_text.insert(tk.END, base_data)

    def eat_meat(self):
        # Define what happens when the button is clicked
        print("Eating meat")
        # Get the player instance
        player = self.parent.get_player_instance()
        if "Meat" in player.inventory:
            player.remove_item_from_inventory("Meat")
            player.energy_change(30)
            player.action_change(-1)
        else:
            print("No meat in inventory")

    def heal_hp(self):
        # Define what happens when the button is clicked
        print("Healing")
        # Get the player instance
        player = self.parent.get_player_instance()
        if "Herb" in player.inventory:
            player.remove_item_from_inventory("Herb")
            player.update_health(30)
            player.action_change(-1)
        else:
            print("No herb in inventory")  # Corrected message

    def goto_gui(self):
        # Define what happens when the button is clicked
        print("Going Outside")
        self.parent.show_frame("gui")