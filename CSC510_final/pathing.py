from simpleai.search import SearchProblem, astar
import copy


# Pathfinder Class 
class PathFinder(SearchProblem):
    def __init__(self, maze, start, goal):
        self.maze = maze
        self.goal = goal
        super(PathFinder, self).__init__(initial_state=start)

    def actions(self, state):
        actions = []
        # Directions (down, up, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direction in directions:
            future_state = (state[0] + direction[0], state[1] + direction[1])
            if 0 <= future_state[0] < len(self.maze) and 0 <= future_state[1] < len(self.maze[0]) and self.maze[future_state[0]][future_state[1]] == " " or "!":
                actions.append(future_state)
        #print(f"Actions from state {state}: {actions}")
        return actions

    def result(self, state, action):
        #print(f"Result of action {action} from state {state}: {action}")
        return action

    def is_goal(self, state):
        is_goal = state == self.goal
        #print(f"Checking if state {state} is goal: {is_goal}")
        return is_goal

    def heuristic(self, state):
        heuristic_value = abs(state[0] - self.goal[0]) + abs(state[1] - self.goal[1])
        #print(f"Heuristic value for state {state}: {heuristic_value}") # Can also modify cost function to output cost
        return heuristic_value

def print_maze(maze, path):
    for position in path:
        maze[position[0]][position[1]] = '*'
    for row in maze:
        print(" ".join(str(cell) for cell in row))



if __name__ == "__main__":

    start = input('Would you like to play?: Y/N ') 
    if start.capitalize == 'N':
        print('Goodbye!')
        exit()
    
    while start.capitalize() == 'Y':
        print("Starting Pathfinder!!!")

        # Scene 1 Data
        scene_1_npc = False
        scene_1_door_N = (0, 3)
        scene_1 = [
            ['X', 'X', 'X', ' ', 'X', 'X', 'X'],
            ['X', ' ', ' ', ' ', ' ', ' ', 'X'],
            ['X', ' ', 'M', ' ', 'M', ' ', 'X'],
            ['X', ' ', 'M', ' ', 'M', ' ', 'X'],
            ['X', ' ', ' ', ' ', ' ', ' ', 'X'],
            ['X', ' ', 'M', ' ', 'M', ' ', 'X'],
            ['X', ' ', 'M', ' ', 'M', ' ', 'X'],
            ['X', ' ', ' ', ' ', ' ', ' ', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X']
        ]

        # Starting Data
        game_over = False
        player_start = (7, 5) # Scene 1
        starting_scene = scene_1

        # Start Game Data, Will Update as Game Progresses
        npc_position = ''
        player_position = player_start
        player_scene = starting_scene

        # Mobs
        player_mob = '&'

        player_move = False

        if player_move == False:
            try:
                maze = copy.deepcopy(player_scene)

                


                problem = PathFinder(maze, npc_position, player_position)
                result = astar(problem)

                if result is None or not result.path():
                    print("No path could be found from start to goal.")
                else:
                    path = [step[1] for step in result.path()]
                    print("Path from start to goal:")
                    print(path)
                    print("\nMaze with path:")
                    print_maze(maze, path)
                    print("\n")
            except Exception as e:
                print(f"An error occurred during pathfinding: {e}")