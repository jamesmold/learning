from collections import Counter
fhand = open("aoc2.txt")

lines = [x.strip() for x in fhand] #removes the new lines from the input file aoc2.txt

def part2():
    for line1 in lines: #nested for loop - takes the first line...
        for line2 in lines: #then the first line again, followed by the 2nd, 3rd etc - then restarts by taking the 2nd line and the first 
            x = ''.join(a for a, b in zip(line1, line2) if a == b)
            if len(x) == len(line1) - 1:
                return x

print(part2())