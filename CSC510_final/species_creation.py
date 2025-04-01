import random
from symbolic_ai_test import RuleEngine, rule_resource_health, rule_predator_prey, rule_self_aggression, rule_reproduction

# Species class
class Species:
    def __init__(self, name, starting_population, prey=None, predators=None, health="Healthy", aggression=int, has_prey=True, can_spawn=True):
        self.name = name
        self.starting_population = starting_population
        self.current_population = starting_population
        self.prey = prey if prey else []
        self.predators = predators if predators else []
        self.health = health  # Possible values: "Healthy" or "Diseased"
        self.starting_aggression = aggression
        self.aggression_x = 0
        self.aggression_y = 0
        self.current_aggression = aggression + self.aggression_x + self.aggression_y
        self.has_prey = has_prey  # True if species can eat prey
        self.can_spawn = can_spawn # True if species can reproduce

    def __str__(self):
        return f"{self.name}"

# Forest class
class Forest:
    def __init__(self, name, carnivore, herbivore, herbs, resources):
        self.name = name
        self.carnivores = [carnivore]
        self.herbivores = [herbivore]
        self.herbs = [herbs]
        self.resources = [resources]
        self.rule_engine = RuleEngine()

        # Add rules to the engine
        self.rule_engine.add_rule(rule_resource_health)
        self.rule_engine.add_rule(rule_predator_prey)
        self.rule_engine.add_rule(rule_self_aggression)
        self.rule_engine.add_rule(rule_reproduction)

    def display_status(self):
        print(f"\n{self.name} Ecosystem:")
        for carnivore in self.carnivores:
            print(f"Carnivore: {carnivore.name}, Population: {carnivore.current_population}, Health: {carnivore.health}, Aggression: {carnivore.current_aggression}, Prey: {[p.name for p in carnivore.prey]}")
        for herbivore in self.herbivores:
            print(f"Herbivore: {herbivore.name}, Population: {herbivore.current_population}, Health: {herbivore.health}, Aggression: {herbivore.current_aggression}, Predators: {[p.name for p in herbivore.predators]}, Prey: {[p.name for p in herbivore.prey]}")
        for herb in self.herbs:
            print(f"Herb: {herb.name}, Population: {herb.current_population}, Health: {herb.health}, Predators: {[p.name for p in herb.predators]}")
        for resource in self.resources:
            print(f"Resource: {resource}, Population: {resource.current_population}")

# Addition begins here
def initialize_ecosystem():
    """Initialize the ecosystem and return it."""
    ecosystem_areas = ["Area 1", "Area 2", "Area 3"]
    ecosystem = []
    for area in ecosystem_areas:
        # Creating species classes
        carnivore_species = Species(random.choice(["Wolf", "Fox", "Bear"]), starting_population=10, aggression=4)
        herbivore_species = Species(random.choice(["Boar", "Deer", "Rabbit"]), starting_population=10, predators=[carnivore_species], aggression=0)
        herbs_species = Species(random.choice(["Apples", "Corn", "Blueberry"]), starting_population=10, predators=[herbivore_species], aggression=0)
        resources = Species(random.choice(["Trees", "Vines", "Clay"]), starting_population=10, aggression=0, has_prey=False)

        # Assigning prey to species
        carnivore_species.prey.append(herbivore_species)  # Carnivores eat herbivores
        herbivore_species.prey.extend([herbs_species])  # Herbivores eat herbs
        ecosystem.append(Forest(area, carnivore_species, herbivore_species, herbs_species, resources))
    return ecosystem

# Initialize the ecosystem globally
ecosystem = initialize_ecosystem()

# Main simulation
if __name__ == "__main__":
    def main():
        for forest in ecosystem:
            forest.display_status()
        
        while True:
            input("Press Enter to simulate next turn...\n\n\n")
            for forest in ecosystem:
                # Simulate herbivores eating herbs
                for herbivore in forest.herbivores:
                    if forest.herbs and any(h.current_population > 0 for h in forest.herbs):
                        food = random.choice([h for h in forest.herbs if h.current_population > 0])
                        print(f"{herbivore.name} eats {food.name}.")
                        food.current_population = max(0, food.current_population - 1)
                        herbivore.health = "Healthy"
                    else:
                        print(f"No food left in {forest.name}, {herbivore.name} is starving!")
                        herbivore.health = "Starved"
                        herbivore.current_population = max(0, herbivore.current_population - 1)

                # Simulate carnivores hunting herbivores
                for carnivore in forest.carnivores:
                    if forest.herbivores and any(h.current_population > 0 for h in forest.herbivores):
                        prey = random.choice([h for h in forest.herbivores if h.current_population > 0])
                        print(f"{carnivore.name} hunts {prey.name}.")
                        prey.current_population = max(0, prey.current_population - 1)
                        carnivore.health = "Healthy"
                    else:
                        print(f"No herbivores left in {forest.name}, {carnivore.name} is starving!")
                        carnivore.health = "Starved"
                        carnivore.current_population = max(0, carnivore.current_population - 1)

                # Apply symbolic AI rules
                context = {
                    'species': forest.carnivores + forest.herbivores + forest.herbs,
                    'resources': forest.resources
                }
                forest.rule_engine.evaluate(context)

                # Display the updated status
                forest.display_status()

    main()

'''
# Main simulation
if __name__ == "__main__":
    # Define ecosystem areas
    ecosystem_areas = ["ForestA", "ForestB", "ForestC"]
    
    # Initialize forest assignments
    ecosystem = []
    for area in ecosystem_areas:
        # Creating species classes
        carnivore_species = Species(random.choice(["Wolf", "Fox", "Bear"]), starting_population=10, aggression=4)
        herbivore_species = Species(random.choice(["Boar", "Deer", "Rabbit"]), starting_population=10, predators=[carnivore_species], aggression=0)
        herbs_species = Species(random.choice(["Apples", "Corn", "Blueberry"]), starting_population=10, predators=[herbivore_species], aggression=0)
        resources = Species(random.choice(["Trees", "Vines", "Clay"]), starting_population=10, aggression=0, has_prey=False)

        # Assigning prey to species
        carnivore_species.prey.append(herbivore_species)  # Carnivores eat herbivores
        herbivore_species.prey.extend([herbs_species])  # Herbivores eat herbs
        ecosystem.append(Forest(area, carnivore_species, herbivore_species, herbs_species, resources))

    def main():
        for forest in ecosystem:
            forest.display_status()
        
        while True:
            input("Press Enter to simulate next turn...\n\n\n")
            for forest in ecosystem:
                # Simulate herbivores eating herbs
                for herbivore in forest.herbivores:
                    if forest.herbs and any(h.current_population > 0 for h in forest.herbs):
                        food = random.choice([h for h in forest.herbs if h.current_population > 0])
                        print(f"{herbivore.name} eats {food.name}.")
                        food.current_population = max(0, food.current_population - 1)
                        herbivore.health = "Healthy"
                    else:
                        print(f"No food left in {forest.name}, {herbivore.name} is starving!")
                        herbivore.health = "Starved"
                        herbivore.current_population = max(0, herbivore.current_population - 1)

                # Simulate carnivores hunting herbivores
                for carnivore in forest.carnivores:
                    if forest.herbivores and any(h.current_population > 0 for h in forest.herbivores):
                        prey = random.choice([h for h in forest.herbivores if h.current_population > 0])
                        print(f"{carnivore.name} hunts {prey.name}.")
                        prey.current_population = max(0, prey.current_population - 1)
                        carnivore.health = "Healthy"
                    else:
                        print(f"No herbivores left in {forest.name}, {carnivore.name} is starving!")
                        carnivore.health = "Starved"
                        carnivore.current_population = max(0, carnivore.current_population - 1)

                # Apply symbolic AI rules
                context = {
                    'species': forest.carnivores + forest.herbivores + forest.herbs,
                    'resources': forest.resources
                }
                forest.rule_engine.evaluate(context)

                # Display the updated status
                forest.display_status()

    main()'''