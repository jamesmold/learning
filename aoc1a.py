fhand = open("aoc1.txt")

lines = list(fhand)

def loop():
    sum = 0
    a = {sum}
    
    while True:
        for num in lines:
            sum = sum + int(num)
            if sum in a:
                return sum
            else:
                a.add(sum)

print(loop())