import string
letters = list(string.ascii_lowercase)


def encrypt(msg, key1, key2, key3):
    x,y,z = (0,0,0)
    encrypted = ""
    for letter in msg:
        if not letter.lower() in letters:
            encrypted += letter
        else:
            index = letters.index(letter.lower())
            index = (index + key1 + x + key2 + y + key3 + z) % 26
            encrypted += letters[index]
            x += 1
        if x == 26:
            x = 0
            y += 1
        if y == 26:
            y = 0
            z += 1
        if key3 == 26:
            key3 = 0
    return encrypted

def decrypt(msg, key1, key2, key3):
    decrypted = ""

    x, y, z = (0,0,0)

    for letter in msg:
        if not letter.lower() in letters:
            decrypted += letter
        else:
            index = letters.index(letter.lower())
            index = (index - key1 - x - key2 - y - key3 - z) % 26
            decrypted += letters[index]
            x += 1
        if x == 26:
            x = 0
            y += 1
        if y == 26:
            y = 0
            z += 1
        if z == 26:
            z = 0
    return decrypted

def test():
    msg = input("message to encrypt:")
    x, y, z = [int(n) for n in input("Keys, separated by a space").split(" ")]
    encrypted = encrypt(msg, x, y, z)
    print(encrypted)
    print(decrypt(encrypted, x, y, z))

print(letters)
#test()
