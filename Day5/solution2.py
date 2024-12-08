import pathlib

curdir = pathlib.Path(__file__).parent.resolve()
rule_list = []
rule_map = {} # will be key:priority. high priority items will have lower numbers, starting with 0
priority_list = []
sum_vals = 0

def process_rules(rule_list):
    for rule in rule_list:
        x, y = rule.split("|")
        x = int(x)
        y = int(y)

        x_set = rule_map.get(x, set())
        x_set.add(y)
        rule_map[x] = x_set

def reorder_recursive(num_list, idx):
    if idx == len(num_list) - 1:
        return

    reorder_recursive(num_list, idx + 1)
    
    for i in range(len(num_list) - 1, idx, -1):
        if num_list[idx] in rule_map.get(num_list[i], set()):
            num_list.insert(i + 1, num_list[idx])
            num_list.pop(idx)
            return

def validate_rule(line):
    num_list = [int(x) for x in line.split(",")]

    if len(num_list) == 1:
        return num_list[0]

    for i in range (1, len(num_list)):
        num = num_list[i]
        i_set = rule_map.get(num, None)
        if i_set:
            for j in range(i, -1, -1):
                if i_set and num_list[j] in rule_map.get(num):
                    # instead of returning 0, order this line correctly
                    reorder_recursive(num_list, 0)
                    return num_list[(len(num_list) - 1) // 2]
            
    #return print_line[(len(print_line) - 1) // 2]
    return 0

with open(f"{curdir}/input.txt", "r") as fp:
    while True:
        rule = fp.readline().strip()
        if not rule:
            break
        rule_list.append(rule)
    process_rules(rule_list)

    for line in fp:
        # validate rule
        sum_vals += validate_rule(line.strip())

print(f"sum: {sum_vals}")