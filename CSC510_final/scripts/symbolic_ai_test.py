import random

# Rule Engine for Symbolic AI
class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        """Add a new rule to the engine."""
        self.rules.append(rule)

    def evaluate(self, context):
        """Evaluate all rules in the given context."""
        for rule in self.rules:
            rule(context)

# Rules for Symbolic AI
def rule_resource_health(context):
    """If resources are low, reduce species health."""
    for resource in context['resources']:
        if resource.current_population < 3:
            for species in context['species']:
                if species.has_prey and species.can_spawn:
                    species.health = "Diseased"
                else:
                    species.health = "Healthy"

def rule_self_aggression(context):
    """Update species' aggression based on their own population changes."""
    for species in context['species']:
        population_percentage = species.current_population / species.starting_population * 100
        if 70 <= population_percentage <= 100:
            species.aggression_x = 0
            species.current_aggression = species.starting_aggression + species.aggression_x + species.aggression_y
        elif 30 <= population_percentage < 70:
            species.aggression_x = 1
            species.current_aggression = species.starting_aggression + species.aggression_x + species.aggression_y
        elif 10 <= population_percentage < 30:
            species.aggression_x = 2
            species.current_aggression = species.starting_aggression + species.aggression_x + species.aggression_y
        else:  # Under 10%
            species.current_aggression = 10

def rule_predator_prey(context):
    """Update predator's aggression based on prey's population changes."""
    for predator in context['species']:
        for prey in predator.prey:
            population_percentage = prey.current_population / prey.starting_population * 100
            if 70 <= population_percentage <= 100:
                predator.aggression_y = 0
                predator.current_aggression = predator.starting_aggression + predator.aggression_x + predator.aggression_y
            elif 30 <= population_percentage < 70:
                predator.aggression_y = 1
                predator.current_aggression = predator.starting_aggression + predator.aggression_x + predator.aggression_y
            elif 10 <= population_percentage < 30:
                predator.aggression_y = 2
                predator.current_aggression = predator.starting_aggression + predator.aggression_x + predator.aggression_y
            else:  # Under 10%
                predator.current_aggression = 10

def rule_reproduction(context):
    for species in context['species']:
        # Calculate total resource population
        total_resource_population = sum(resource.current_population for resource in context['resources'])
        
        reproduce = random.randint(0, 10)
        if reproduce == 1:     
            if species.health == "Healthy" and species.current_population < species.starting_population and total_resource_population > 2:
                species.current_population += 1

