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

REVERSE_MORSE_CODE_DICT = {value: key for key,
                           value in MORSE_CODE_DICT.items()}


def convert_to_morse(input_string):
    """Converts text to Morse Code."""
    morse_code = ''
    for char in input_string:
        if char in MORSE_CODE_DICT:
            # Add space between Morse Code characters
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += '? '  # For unknown characters
    return morse_code


def convert_from_morse(morse_code):
    """Converts Morse Code to text."""
    words = morse_code.split('  ')  # Assumes two spaces between words
    decoded_message = ''

    for word in words:
        letters = word.split()
        for symbol in letters:
            if symbol in REVERSE_MORSE_CODE_DICT:
                decoded_message += REVERSE_MORSE_CODE_DICT[symbol]
            else:
                decoded_message += '?'
        decoded_message += ' '
    return decoded_message.strip()


while True:
    print("\nChoose an option:")
    print("1. Convert text to Morse code")
    print("2. Convert Morse code to text")
    print("3. Exit")

    choice = input("> ").strip()

    if choice == "1":
        user_input = input("Enter a string to convert to Morse Code: ").upper()
        print(convert_to_morse(user_input))
    elif choice == "2":
        user_input = input("Enter Morse Code to convert to text: ")
        print(convert_from_morse(user_input))
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
