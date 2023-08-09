# Constants for menu options
TEXT_TO_MORSE = "1"
MORSE_TO_TEXT = "2"
EXIT = "3"

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
    return ' '.join(MORSE_CODE_DICT.get(char, '?') for char in input_string)


def convert_from_morse(morse_code):
    words = morse_code.split('  ')
    return ' '.join(''.join(REVERSE_MORSE_CODE_DICT.get(symbol, '?') for symbol in word.split()) for word in words)


def display_menu():
    print("\nChoose an option:")
    print(f"{TEXT_TO_MORSE}. Convert text to Morse code")
    print(f"{MORSE_TO_TEXT}. Convert Morse code to text")
    print(f"{EXIT}. Exit")


def main():
    while True:
        display_menu()

        choice = input("> ").strip()

        if choice == TEXT_TO_MORSE:
            user_input = input(
                "Enter a string to convert to Morse Code: ").upper()
            print(convert_to_morse(user_input))
        elif choice == MORSE_TO_TEXT:
            user_input = input("Enter Morse Code to convert to text: ")
            print(convert_from_morse(user_input))
        elif choice == EXIT:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
