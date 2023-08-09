# Morse Code Dictionary (Expanded to include some punctuation marks)
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


def string_to_morse(input_string):
    """Converts a string to Morse Code."""
    morse_code = ''
    for char in input_string:
        if char in MORSE_CODE_DICT:
            # Add space between Morse Code characters
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += '? '  # For unknown characters
    return morse_code


# Get User Input
user_input = input("Enter a string to convert to Morse Code: ").upper()

# Conversion and Display
print(string_to_morse(user_input))
