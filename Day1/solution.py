import pathlib
curdir = pathlib.Path(__file__).parent.resolve()

l1 = []
l2 = []

with open(f"{curdir}/input.txt", "r") as fp:
    for line in fp:
        x, y = line.split()
        l1.append(int(x))
        l2.append(int(y))

l1.sort()
l2.sort()

l3 = [abs(x-y) for x, y in zip(l1, l2)]
print(f"sum: {sum(l3)}")

l4 = {}
for num in l2:
    l4[num] = l4.get(num, 0) + 1

l5 = [(l4.get(x, 0) * x) for x in l1]
print(f"similarity score {sum(l5)}")