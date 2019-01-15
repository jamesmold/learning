fhand = open("subsciphertext.txt")
from string import ascii_letters

coded_letters = fhand.read()
cipher_letters = 'yzabcdefghijklmnopqrstuvwxYZABCDEFGHIJKLMNOPQRSTUVWX'
trans = str.maketrans(cipher_letters, ascii_letters) #this decodes
#trans = str.maketrans(cipher_letters, ascii_letters) use this to encode

decoded = coded_letters.translate(trans)
print(decoded)