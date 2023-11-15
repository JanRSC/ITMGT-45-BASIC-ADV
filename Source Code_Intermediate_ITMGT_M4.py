def shift_letter(letter, shift):
    if letter == " ":
        return " "
    else:
        ascii_offset = ord("A") if letter.isupper() else ord("a")
        shifted_letter = chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)
        return shifted_letter

def caesar_cipher(message, shift):
    result = ""
    for char in message:
        result += shift_letter(char, shift)
    return result

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    else:
        shift = ord(letter_shift) - ord("A")
        return shift_letter(letter, shift)

def vigenere_cipher(message, key):
    result = ""
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]
    for i in range(len(message)):
        result += shift_by_letter(message[i], key[i])
    return result
