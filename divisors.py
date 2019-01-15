limit = int(input("Enter limit:"))

x = range(1, limit)

for num in x:
    if limit % num == 0:
        print(num, "is a divisor of", limit)