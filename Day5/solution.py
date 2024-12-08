import pathlib

curdir = pathlib.Path(__file__).parent.resolve()
rule_list = []
priority_map = {} # will be key:priority. high priority items will have lower numbers, starting with 0
priority_list = []
sum_vals = 0

def process_rules(rule_list):
    rule_list.sort()
    
    for rule in rule_list:
        x, y = rule.split("|")
        x = int(x)
        y = int(y)
        pri_x = priority_map.get(x, -1)
        pri_y = priority_map.get(y, -1)

        if pri_x < 0: # number isn't in list yet
            if pri_y < 0: # number is also not in list yet
                # put both numbers at the end.
                priority_list.append(x) #since x is always before y because of rules
                priority_list.append(y)

                priority_map[x] = len(priority_list) - 2 #the indices of the values in the list
                priority_map[y] = len(priority_list) - 1
            
            else:
                priority_list.insert(pri_y, x)
                priority_map[x] = pri_y
                for i in range(pri_y + 1, len(priority_list)):
                    priority_map[priority_list[i]] = i #update all priorities afterwads
        else: # number is already in list, we need to check for a rule violation
            if pri_x < pri_y:
                continue
            elif pri_y < 0: #y is not yet in the list, so put it at the end
                priority_list.append(y)
                priority_map[y] = len(priority_list) - 1  
            else: #x needs to be moved before y
                priority_list.pop(pri_x)
                priority_list.insert(pri_y, x)
                priority_map[x] = pri_y
                for i in range(pri_y + 1, len(priority_list)):
                    priority_map[priority_list[i]] = i #update all priorities afterwads

def validate_rule(line):
    to_check = [priority_map.get(int(x)) for x in line.split(",") if priority_map.get(int(x), -1) != -1]
    if(sorted(to_check) == to_check):
        orig_list = [int(x) for x in line.split(",")]
        return orig_list[(len(orig_list) - 1) // 2]
    else:
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