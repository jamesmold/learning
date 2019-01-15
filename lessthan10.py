a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

limit = int(input("Enter limit: "))

for num in a:
    if num < limit:
        b.append(num)

print(b)
