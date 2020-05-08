

def encrypt(text, shift=10):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.isspace():
            result += char
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result


def decrypt(text, shift=10):
    return encrypt(text, -shift)


if __name__ == "__main__":
    tekst = "na straganie w dzien targowy takie slyszy sie rozmowy"

    print(decrypt(encrypt(tekst)))
