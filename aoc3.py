from collections import defaultdict
import re
fhand = open("aoc3.txt")

ids = defaultdict(set)
for line in fhand:
    id, x, y, w, h = map(int, re.findall(r'\d+', line))

    for j in range(y, y+h):
        for i in range(x, x+w):
            ids[(i, j)].add(id)

print(sum(len(x) > 1 for x in ids.values()))
