alfabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

encrypt = input("Enter a clear message: ")
key = int(input("Please enter a key(numder from 1-25): "))
encrypt = encrypt.lower()
encrypted = ""

for letter in encrypt:
    position = alfabet.find(letter)
    newPosition = position + key
    if letter in alfabet:
        encrypted = encrypted + alfabet[newPosition]
    else:
        encrypted = encrypted + letter
print("Your cipher is: ", encrypted)
