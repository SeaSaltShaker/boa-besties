import pathlib
import re

curdir = pathlib.Path(__file__).parent.resolve()

def process_rule(rule_string):
    return int(rule_string[0]) * int(rule_string[1])

sum_rules = 0
with open(f"{curdir}/input.txt", "r") as fp:
    line_orig = fp.read()
    line = re.sub(r"don't\(\).*?(do\(\)|$)", "X", line_orig, flags=re.DOTALL) #added for part 2. deleting all disabled functions
    matches = re.findall(r"mul\((\d+),(\d+)\)", line)
    for match in matches:
        sum_rules += process_rule(match)

print(f"Sum {sum_rules}")