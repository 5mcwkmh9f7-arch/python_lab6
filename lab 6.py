alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def vigenere_sq():
    header = "|   |"
    for letter in alphabet:
        header += f" {letter} |"
    print(header)
    separator = "|---|"
    for letter in alphabet:
        separator += "---|"
    print(separator)
    for row in range(len(alphabet)):
        line = f"| {alphabet[row]} |"
        for col in range(len(alphabet)):
            line += f" {alphabet[(row + col) % len(alphabet)]} |"
        print(line)


def letter_to_index(letter, alphabet):
    return alphabet.index(letter)


def index_to_letter(index, alphabet):
    return alphabet[index]


def vigenere_index(key_letter, plaintext_letter, alphabet):
    index = (letter_to_index(plaintext_letter, alphabet) + letter_to_index(key_letter, alphabet)) % len(alphabet)
    return index_to_letter(index, alphabet)


def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = ""
    count = 0
    for letter in plaintext.upper():
        if letter in alphabet:
            cipher_text += vigenere_index(key[count % len(key)], letter, alphabet)
            count += 1
        else:
            cipher_text += letter
    return cipher_text


def undo_vigenere_index(key_letter, cypher_letter, alphabet):
    index = (letter_to_index(cypher_letter, alphabet) - letter_to_index(key_letter, alphabet)) % len(alphabet)
    return index_to_letter(index, alphabet)


def decrypt_vignere(key, cipher_text, alphabet):
    plaintext = ""
    count = 0
    for letter in cipher_text.upper():
        if letter in alphabet:
            plaintext += undo_vigenere_index(key[count % len(key)], letter, alphabet)
            count += 1
        else:
            plaintext += letter
    return plaintext


key = "GABRIEL"
vigenere_sq()
while True:
    choice = input("1). Encrypt or 2). Decrypt: ")
    if choice == "1":
        plaintext = input("Enter plain text: ")
        print(encrypt_vigenere(key, plaintext, alphabet))
    elif choice == "2":
        cipher_text = input("Enter cipher text: ")
        print(decrypt_vignere(key, cipher_text, alphabet))