import Enigma


def crack(message, possible_words):
    for x in range(10):
        for y in range(10):
            for z in range(10):
                if Enigma.decrypt(message, x, y, z) in possible_words:
                    return x, y, z
