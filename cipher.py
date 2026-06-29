def encrypt(text, shift):
    encrypted = ""

    for ch in text:

        if ch.isupper():
            encrypted += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))

        elif ch.islower():
            encrypted += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))

        else:
            encrypted += ch

    return encrypted


def decrypt(text, shift):

    decrypted = ""

    for ch in text:

        if ch.isupper():
            decrypted += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))

        elif ch.islower():
            decrypted += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))

        else:
            decrypted += ch

    return decrypted