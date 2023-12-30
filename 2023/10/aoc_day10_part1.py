from pathlib import Path
import math

# ***** IMPORT INPUT FILE *****
# obtaining the proper relative path
script_location = Path(__file__).absolute().parent
# file_name = 'loop1.txt'
# file_name = 'loop2.txt'
file_name = 'input.txt'
myfile = script_location / file_name

# read the file into a list, split by the newline characters
# note:  read_text() automatically closes file when done 
pipes = myfile.read_text().split('\n')
# *****************************

# return a valid next pipe
# map    : map as a list
# pipe   : the pipe to look around
# exclude: string of direction to exclude
# return : return a direction to travel
def findNextPipe(map: list, pipe: dict, exclude: str = "") -> str:
    map_y_max = len(map)-1
    map_x_max = len(map[0])-1
    directions = set([x for x in ['north', 'east', 'south', 'west'] if x != exclude])

    x = pipe['x']
    y = pipe['y']

    # discard direction if near a map edge
    if x == 0:
        directions.discard('west')
    if x == map_x_max:
        directions.discard('east')
    if y == 0:
        directions.discard('north')
    if y == map_y_max:
        directions.discard('south')

    for direction in directions:
        if direction == 'north':
            if map[y-1][x] in ['|', '7', 'F', 'S']:
                return 'north'
            
        elif direction == 'east':
            if map[y][x+1] in ['-', 'J', '7', 'S']:
                return 'east'
            
        elif direction == 'south':
            if map[y+1][x] in ['|', 'L', 'J', 'S']:
                return 'south'
            
        elif direction == 'west':
            if map[y][x-1] in ['-', 'L', 'F', 'S']:
                return 'west'




# (x,y)=(0,0) at top left
# (x,y)=(x_max-1,0) at top right
# (x,y)=(0,y_max-1) at bot left
# (x,y)=(x_max-1,y_max-1) at bot right
y_max = len(pipes)-1
x_max = len(pipes[0])-1
y_start = [i for i in range(0, y_max) if 'S' in pipes[i]][0]
x_start = [i for i in range(0, x_max) if 'S' == pipes[y_start][i]][0]

start_coords   = {'x': x_start, 'y': y_start}
current_coords = {'x': x_start, 'y': y_start}
exclude_dir = 'S' # making sure we dont go backwards
visited_pipes = []
step_count = 0
while (current_coords != start_coords or step_count < 1) and (step_count < (y_max*x_max)):
    step_count += 1

    move_dir = findNextPipe(pipes, current_coords, exclude_dir)
    
    if move_dir == 'north':
        current_coords['y'] = current_coords['y'] - 1
        exclude_dir = 'south'
    elif move_dir == 'east':
        current_coords['x'] = current_coords['x'] + 1
        exclude_dir = 'west'
    elif move_dir == 'south':
        current_coords['y'] = current_coords['y'] + 1
        exclude_dir = 'north'
    elif move_dir == 'west':
        current_coords['x'] = current_coords['x'] - 1
        exclude_dir = 'east'
    
    if current_coords in visited_pipes:
        print("steps to duplicate: " + str(step_count))
        break

    visited_pipes.append({'x': current_coords['x'], 'y': current_coords['y']})




farthest_point = math.ceil(step_count/2)


print("steps to farthest point: " + str(farthest_point))









