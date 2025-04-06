'''
Script: species_creation.py
Description: Defines the Species and Forest classes for managing the virtual ecosystem. 
             Includes methods for simulating interactions between species and applying symbolic AI rules.
Author: Patrick Davis
Date: April 5, 2025
Version: 1.0
'''

import random
from scripts.symbolic_ai_test import RuleEngine, rule_resource_health, rule_predator_prey, rule_self_aggression, rule_reproduction


class Species:
    '''
    Represents a species in the ecosystem with attributes for population, health, aggression, and relationships.
    '''

    def __init__(self, name: str, starting_population: int, prey: list = None, predators: list = None, 
                 health: str = 'Healthy', aggression: int = 0, has_prey: bool = True, can_spawn: bool = True) -> None:
        '''
        Initialize a Species instance.

        Args:
            name (str): The name of the species.
            starting_population (int): The initial population of the species.
            prey (list): A list of prey species. Defaults to None.
            predators (list): A list of predator species. Defaults to None.
            health (str): The health status of the species. Defaults to 'Healthy'.
            aggression (int): The aggression level of the species. Defaults to 0.
            has_prey (bool): Whether the species can eat prey. Defaults to True.
            can_spawn (bool): Whether the species can reproduce. Defaults to True.
        '''
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
        self.has_prey = has_prey
        self.can_spawn = can_spawn

    def __str__(self) -> str:
        '''
        Return a string representation of the species.

        Returns:
            str: The name of the species.
        '''
        return self.name


class Forest:
    '''
    Represents a forest ecosystem containing species and resources.
    Manages interactions between species and applies symbolic AI rules.
    '''

    def __init__(self, name: str, carnivore: Species, herbivore: Species, herbs: Species, resources: Species) -> None:
        '''
        Initialize a Forest instance.

        Args:
            name (str): The name of the forest.
            carnivore (Species): A carnivore species in the forest.
            herbivore (Species): A herbivore species in the forest.
            herbs (Species): A herb species in the forest.
            resources (Species): A resource species in the forest.
        '''
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

    def display_status(self) -> None:
        '''
        Display the current status of the forest ecosystem.
        '''
        print(f'\n{self.name} Ecosystem:')
        for carnivore in self.carnivores:
            print(f'Carnivore: {carnivore.name}, Population: {carnivore.current_population}, '
                  f'Health: {carnivore.health}, Aggression: {carnivore.current_aggression}, '
                  f'Prey: {[p.name for p in carnivore.prey]}')
        for herbivore in self.herbivores:
            print(f'Herbivore: {herbivore.name}, Population: {herbivore.current_population}, '
                  f'Health: {herbivore.health}, Aggression: {herbivore.current_aggression}, '
                  f'Predators: {[p.name for p in herbivore.predators]}, '
                  f'Prey: {[p.name for p in herbivore.prey]}')
        for herb in self.herbs:
            print(f'Herb: {herb.name}, Population: {herb.current_population}, '
                  f'Health: {herb.health}, Predators: {[p.name for p in herb.predators]}')
        for resource in self.resources:
            print(f'Resource: {resource.name}, Population: {resource.current_population}')


def initialize_ecosystem() -> list[Forest]:
    '''
    Initialize the ecosystem with predefined areas and species.

    Returns:
        list[Forest]: A list of Forest instances representing the ecosystem.
    '''
    ecosystem_areas = ['Area 1', 'Area 2', 'Area 3']
    ecosystem = []
    for area in ecosystem_areas:
        # Creating species classes
        carnivore_species = Species(random.choice(['Wolf', 'Fox', 'Bear']), starting_population=10, aggression=40)
        herbivore_species = Species(random.choice(['Boar', 'Deer', 'Rabbit']), starting_population=10, 
                                    predators=[carnivore_species], aggression=10)
        herbs_species = Species(random.choice(['Basil', 'Corn', 'Blueberry']), starting_population=10, 
                                predators=[herbivore_species], aggression=0)
        resources = Species(random.choice(['Oak Trees', 'Bamboo', 'Elder Trees']), starting_population=10, 
                            aggression=0, has_prey=False)

        # Assigning prey to species
        carnivore_species.prey.append(herbivore_species)  # Carnivores eat herbivores
        herbivore_species.prey.append(herbs_species)  # Herbivores eat herbs
        ecosystem.append(Forest(area, carnivore_species, herbivore_species, herbs_species, resources))
    return ecosystem


# Initialize the ecosystem globally
ecosystem = initialize_ecosystem()


def main() -> None:
    '''
    Main simulation loop for the ecosystem.
    '''
    for forest in ecosystem:
        forest.display_status()

    while True:
        input('Press Enter to simulate the next turn...\n\n\n')
        for forest in ecosystem:
            # Simulate herbivores eating herbs
            for herbivore in forest.herbivores:
                if forest.herbs and any(h.current_population > 0 for h in forest.herbs):
                    food = random.choice([h for h in forest.herbs if h.current_population > 0])
                    print(f'{herbivore.name} eats {food.name}.')
                    food.current_population = max(0, food.current_population - 1)
                    herbivore.health = 'Healthy'
                else:
                    print(f'No food left in {forest.name}, {herbivore.name} is starving!')
                    herbivore.health = 'Starved'
                    herbivore.current_population = max(0, herbivore.current_population - 1)

            # Simulate carnivores hunting herbivores
            for carnivore in forest.carnivores:
                if forest.herbivores and any(h.current_population > 0 for h in forest.herbivores):
                    prey = random.choice([h for h in forest.herbivores if h.current_population > 0])
                    print(f'{carnivore.name} hunts {prey.name}.')
                    prey.current_population = max(0, prey.current_population - 1)
                    carnivore.health = 'Healthy'
                else:
                    print(f'No herbivores left in {forest.name}, {carnivore.name} is starving!')
                    carnivore.health = 'Starved'
                    carnivore.current_population = max(0, carnivore.current_population - 1)

            # Apply symbolic AI rules
            context = {
                'species': forest.carnivores + forest.herbivores + forest.herbs,
                'resources': forest.resources
            }
            forest.rule_engine.evaluate(context)

            # Display the updated status
            forest.display_status()


if __name__ == '__main__':
    main()