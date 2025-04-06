'''
Script: symbolic_ai_test.py
Description: Implements a symbolic AI rule engine and defines rules for managing species interactions 
             and ecosystem dynamics in the virtual ecosystem.
Author: Patrick Davis
Date: April 5, 2025
Version: 1.0
'''

import random
from typing import Callable, Dict, List, Any


class RuleEngine:
    '''
    A rule engine for symbolic AI that evaluates a set of rules in a given context.
    '''

    def __init__(self) -> None:
        '''
        Initialize the RuleEngine with an empty list of rules.
        '''
        self.rules: List[Callable[[Dict[str, Any]], None]] = []

    def add_rule(self, rule: Callable[[Dict[str, Any]], None]) -> None:
        '''
        Add a new rule to the engine.

        Args:
            rule (Callable[[Dict[str, Any]], None]): A function representing the rule to add.
        '''
        self.rules.append(rule)

    def evaluate(self, context: Dict[str, Any]) -> None:
        '''
        Evaluate all rules in the given context.

        Args:
            context (Dict[str, Any]): The context in which to evaluate the rules.
        '''
        for rule in self.rules:
            rule(context)


# Rules for Symbolic AI
def rule_resource_health(context: Dict[str, Any]) -> None:
    '''
    If resources are low, reduce species health.

    Args:
        context (Dict[str, Any]): The context containing species and resources.
    '''
    for resource in context['resources']:
        if resource.current_population < 3:
            for species in context['species']:
                if species.has_prey and species.can_spawn:
                    species.health = 'Diseased'
                else:
                    species.health = 'Healthy'


def rule_self_aggression(context: Dict[str, Any]) -> None:
    '''
    Update species' aggression based on their own population changes.

    Args:
        context (Dict[str, Any]): The context containing species and their attributes.
    '''
    for species in context['species']:
        population_percentage = species.current_population / species.starting_population * 100
        if 70 <= population_percentage <= 100:
            species.aggression_x = 0
        elif 30 <= population_percentage < 70:
            species.aggression_x = 10
        elif 10 <= population_percentage < 30:
            species.aggression_x = 20
        else:  # Under 10%
            species.aggression_x = 10
        species.current_aggression = species.starting_aggression + species.aggression_x + species.aggression_y


def rule_predator_prey(context: Dict[str, Any]) -> None:
    '''
    Update predator's aggression based on prey's population changes.

    Args:
        context (Dict[str, Any]): The context containing species and their relationships.
    '''
    for predator in context['species']:
        for prey in predator.prey:
            population_percentage = prey.current_population / prey.starting_population * 100
            if 70 <= population_percentage <= 100:
                predator.aggression_y = 0
            elif 30 <= population_percentage < 70:
                predator.aggression_y = 10
            elif 10 <= population_percentage < 30:
                predator.aggression_y = 20
            else:  # Under 10%
                predator.aggression_y = 10
            predator.current_aggression = predator.starting_aggression + predator.aggression_x + predator.aggression_y


def rule_reproduction(context: Dict[str, Any]) -> None:
    '''
    Allow species to reproduce if conditions are met.

    Args:
        context (Dict[str, Any]): The context containing species and resources.
    '''
    for species in context['species']:
        # Calculate total resource population
        total_resource_population = sum(resource.current_population for resource in context['resources'])

        reproduce = random.randint(0, 1)
        if reproduce == 1:
            if (species.health == 'Healthy' and 
                species.current_population < species.starting_population and 
                species.current_population > 1 and 
                total_resource_population > 2):
                species.current_population += 1