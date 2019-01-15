from collections import Counter
fhand = open("aoc2.txt")

lines = [x.strip() for x in fhand] #removes the new lines from the input file aoc2.txt

def part1():
    has2 = 0
    has3 = 0
    for line in lines:
        c = Counter(line).values() #Counter counts like elements in a string (returns as dict key value pair, adding the .values just returns the value not the key)
        if 2 in c:
            has2 = has2 + 1
        if 3 in c:
            has3 = has3 + 1
        else: continue
    return has2 * has3

print(part1())