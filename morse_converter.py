# ===========================
# MORSE CODE DICTIONARY (INCLUDES PUNCTUATIONS)
# ===========================
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '(': '-.--.', ')': '-.--.-',
    '/': '-..-.', '_': '..--.-', '+': '.-.-.', '-': '-....-', '=': '-...-',
    '$': '...-..-', '@': '.--.-.', ' ': '/',
}

# Reverse the dictionary for Morse-to-text conversion
REVERSE_MORSE_CODE_DICT = {value: key for key,
                           value in MORSE_CODE_DICT.items()}


def convert_to_morse(input_string):
    """
    Convert a given text string to its Morse code representation.

    Parameters:
    - input_string (str): The text string to be converted.

    Returns:
    - str: The Morse code representation of the input string.
    """
    return ' '.join(MORSE_CODE_DICT.get(char, '?') for char in input_string)


def convert_from_morse(morse_code):
    """
    Convert a given Morse code string to its text representation.

    Parameters:
    - morse_code (str): The Morse code string to be converted.

    Returns:
    - str: The text representation of the input Morse code.
    """
    words = morse_code.split('  ')
    return ' '.join(''.join(REVERSE_MORSE_CODE_DICT.get(symbol, '?') for symbol in word.split()) for word in words)
