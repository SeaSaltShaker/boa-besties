import pathlib
curdir = pathlib.Path(__file__).parent.resolve()

count = 0

def validate(array):
    increasing = None
    if array[1] - array[0] > 0:
        increasing = True
    elif array[1] - array[0] < 0:
        increasing = False
    else:
        return False
    for i in range(0, len(array) - 1):
        diff = array[i+1] - array[i]
        if increasing and (1 <= diff <= 3):
            continue
        elif increasing:
            return False
        elif not increasing and (-3 <= diff <= -1):
            continue
        else:
            return False
    return True

with open(f"{curdir}/input.txt", "r") as fp:
    for line in fp:
        array = list(map(int, line.split()))
        if(validate(array)):
            count += 1
        else:
            for i in range(0, len(array)):
                popped_element = array.pop(i)
                if(validate(array)):
                    count +=1
                    break
                array.insert(i, popped_element)

print(count)
