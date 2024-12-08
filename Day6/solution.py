import pathlib

curdir = pathlib.Path(__file__).parent.resolve()
point_map = {}
num_visited = 1
num_loops = 0
cur_direction = 0 # 0 = up, 1 = right, 2 = down, 3 = left
cur_location = None

def direction_change():
    global cur_direction
    cur_direction = (cur_direction + 1) % 4

class Point:
    def __init__(self, x, y, has_visited=False, has_obstacle=False):
        self.x = x
        self.y = y
        self.visited = has_visited
        self.obstacle = has_obstacle

with open(f"{curdir}/input.txt", "r") as fp:
    i = 0
    for line in fp:
        char_array = line.strip()
        for j in range(0, len(char_array)):
            c = char_array[j]
            if c == "#":
                point_map[(i, j)] = Point(i, j, has_obstacle=True)
            elif c == "^":
                point_map[(i, j)] = Point(i, j, has_visited=True)
                cur_location = point_map[(i, j)]
            else:
                point_map[(i, j)] = Point(i, j)
        i += 1

while cur_location:
    if cur_direction == 0:
        if cur_location.obstacle == True:
            direction_change()
            cur_location = point_map[(cur_location.x + 1,cur_location.y)]
        else:
            if not cur_location.visited:
                num_visited += 1
            cur_location.visited = True
            cur_location = point_map.get((cur_location.x - 1,cur_location.y), None)
    
    elif cur_direction == 1: # right
        if cur_location.obstacle == True:
            direction_change()
            cur_location = point_map[(cur_location.x,cur_location.y - 1)]
        else:
            if not cur_location.visited:
                num_visited += 1
            cur_location.visited = True
            cur_location = point_map.get((cur_location.x,cur_location.y + 1), None)
    
    elif cur_direction == 2: # down
        if cur_location.obstacle == True:
            direction_change()
            cur_location = point_map[(cur_location.x - 1,cur_location.y)]
        else:
            if not cur_location.visited:
                num_visited += 1
            cur_location.visited = True
            cur_location = point_map.get((cur_location.x + 1,cur_location.y), None)
    
    elif cur_direction == 3: # left
        if cur_location.obstacle == True:
            direction_change()
            cur_location = point_map[(cur_location.x,cur_location.y + 1)]
        else:
            if not cur_location.visited:
                num_visited += 1
            cur_location.visited = True
            cur_location = point_map.get((cur_location.x,cur_location.y - 1), None)

print(f"visited: {num_visited}")