import pathlib

curdir = pathlib.Path(__file__).parent.resolve()

search_str = "MAS"
search_set = {"S", "M"}
sum_strings = 0
end_matrix = [(-3, 0), (0, -3), (-3, -3), (3, 0), (0, 3), (3, 3), (-3, 3), (3, -3)]

def move_to_0(x, y):
    if y != 0:
        y = y-1 if y > 0 else y+1
    if x != 0:
        x = x-1 if x > 0 else x+1
    return x, y

def look_around_X(full_table, row, col):
    strings = 0
    for (x, y) in end_matrix:
        end_idx = len("MAS") - 1
        while not(x == 0 and y == 0):
            if (row + x < 0) or (col + y < 0): #forgot python allows for negative list access
                break
            try:
                char = full_table[row + x][col + y]
                if char != search_str[end_idx]:
                    break
                x, y = move_to_0(x, y)
                end_idx -= 1
            except:
                #print("Oops! Out of bounds")
                break
        if end_idx < 0:
            strings += 1
    return strings

# part 2
def look_around_A(full_table, row, col):
    try:
        if row == 0 or col == 0:
            return 0
        left_diag = set([full_table[row - 1][col -1], full_table[row + 1][col + 1]])
        right_diag = set([full_table[row + 1][col - 1], full_table[row - 1][col + 1]])
        if left_diag == right_diag == search_set:
            return 1
    except:
        pass
    return 0

rows = []

with open(f"{curdir}/input.txt", "r") as fp:
    for line in fp:
        rows.append(line.strip())

lower_bound = 0
upper_bound = len(rows[0])

for row in range(0,len(rows)):
    for col in range(lower_bound, upper_bound):
        #if 'X' == rows[row][col]: <--- part 1
        #    sum_strings += look_around_X(rows, row, col)
        if 'A' == rows[row][col]:
            sum_strings += look_around_A(rows, row, col)

print(f"{sum_strings}")