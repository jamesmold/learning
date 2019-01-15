a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

if len(a) < len(b):
    x = b
    y = a
else:
    x = a
    y = b

for num in x:
    if num in y:
        print(num, "is in both")