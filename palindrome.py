inp = input("Enter string: ")

def reverse(inp): #this function reverses a string
    if len(inp) == 0: 
        return inp
    else: 
        return reverse(inp[1:]) + inp[0]

revinp = reverse(inp)

print("Original input: ", inp)
print("Reversed input: ", revinp)

if inp == revinp:
    print(inp, "is a palindrome")
else:
    print(inp, "is not a palindrome")

#to iterate through a string or list backwards use this
for i in reversed(inp):
    print(i)
