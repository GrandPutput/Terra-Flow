class House:
    def __init__(self, health=100):
        # Player attributes
        self.health = health
        self.walls = False
        self.farm = False


    def update_health(self, amount):
        self.health += amount
        if self.health < 0:
            self.health = 0


    # Update the player's walls.
    def set_walls(self):
        if self.walls == False:
            self.walls = True
            self.health += 50
        else:
            self.walls = False 
            self.health -= 50

    def set_farm(self):
        if self.farm == False:
            self.farm = True
        else:
            self.farm = False


    def get_house_info(self):
        # Return a dictionary of the player's current stats.
        return {
            "Base Status": self.health,
            "Walls Status": self.walls,
            "Farm Status": self.farm
        }

