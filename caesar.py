def alphabet_position(character):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower = character.lower()
    return alphabet.index(lower)

def rotate_string_13(caesar_text):

    rotated = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in caesar_text:
        rotated_idx = (alphabet_position(char) + 13) % 26
        if char.isupper():
            rotated = rotated + alphabet[rotated_idx].upper()
        else:
            rotated = rotated + alphabet[rotated_idx]

    return rotated

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_idx = (alphabet_position(char) + rot) % 26

    if char.isupper():
        return alphabet[rotated_idx].upper()
    else:
        return alphabet[rotated_idx]

def rotate_string(caesar_text, rot):

    rotated = ''

    for char in caesar_text:
        if (char.isalpha()):
            rotated = rotated + rotate_character(char, rot)
        else:
            rotated = rotated + char

    return rotated