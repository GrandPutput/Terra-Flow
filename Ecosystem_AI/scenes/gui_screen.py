'''
Script: gui_screen.py
Description: Implements the GuiScreen class, which represents the main GUI screen for the virtual ecosystem.
             Includes methods for displaying ecosystem and player data, and navigating to different areas.
Author: Patrick Davis
Date: April 5, 2025
Version: 1.0
'''

import tkinter as tk
from scripts.species_creation import ecosystem  # Import ecosystem and relevant classes
from scripts.player_stats import Player  # Import Player class


class GuiScreen(tk.Frame):
    '''
    Represents the main GUI screen for the virtual ecosystem.
    Displays ecosystem and player data, and provides navigation to different areas.
    '''

    def __init__(self, parent) -> None:
        '''
        Initialize the GuiScreen with GUI components and navigation buttons.

        Args:
            parent: The parent object (usually the main application).
        '''
        super().__init__(parent.root)
        self.parent = parent  # Store the parent reference

        # Ecosystem Data Section
        self.ecosystem_label = tk.Label(self, text='Ecosystem Data', font=('Arial', 14))
        self.ecosystem_label.pack(pady=10)

        self.ecosystem_data_text = tk.Text(self, wrap='word', height=15, width=80)
        self.ecosystem_data_text.pack(pady=10)

        # Player Data Section
        self.player_label = tk.Label(self, text='Player Data', font=('Arial', 14))
        self.player_label.pack(pady=10)

        self.player_data_text = tk.Text(self, wrap='word', height=7, width=80)
        self.player_data_text.pack(pady=10)

        # Navigation Buttons Section
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        self.create_navigation_buttons(button_frame)

    def create_navigation_buttons(self, button_frame: tk.Frame) -> None:
        '''
        Create navigation buttons for exploring different areas and returning to the base.

        Args:
            button_frame (tk.Frame): The frame to hold the buttons.
        '''
        buttons = [
            ('Explore Area 1', self.goto_area1),
            ('Explore Area 2', self.goto_area2),
            ('Explore Area 3', self.goto_area3),
            ('Go To Base', self.goto_base),
        ]

        for text, command in buttons:
            tk.Button(button_frame, text=text, command=command).pack(side='left', padx=10)

    def update_data(self, ecosystem_data: str, player_data: str) -> None:
        '''
        Update the GUI with the latest ecosystem and player data.

        Args:
            ecosystem_data (str): The updated ecosystem data.
            player_data (str): The updated player data.
        '''
        # Update ecosystem data
        self.ecosystem_data_text.delete(1.0, tk.END)
        self.ecosystem_data_text.insert(tk.END, ecosystem_data)

        # Update player data
        self.player_data_text.delete(1.0, tk.END)
        self.player_data_text.insert(tk.END, player_data)

    def goto_area1(self) -> None:
        '''
        Navigate to Area 1.
        '''
        self.parent.show_frame('Area 1')

    def goto_area2(self) -> None:
        '''
        Navigate to Area 2.
        '''
        self.parent.show_frame('Area 2')

    def goto_area3(self) -> None:
        '''
        Navigate to Area 3.
        '''
        self.parent.show_frame('Area 3')

    def goto_base(self) -> None:
        '''
        Navigate to the player's base.
        '''
        self.parent.show_frame('Base')