"""
Morse Code Converter

This script allows the user to convert text to Morse code and vice versa.
The user can also read text or Morse code from a file and save the results to another file.

Usage:
    Run the script and choose an option from the displayed menu.
"""


# ======================
# CONSTANTS
# ======================
TEXT_TO_MORSE = "1"
MORSE_TO_TEXT = "2"
FILE_TEXT_TO_MORSE = "3"
FILE_MORSE_TO_TEXT = "4"
EXIT = "5"

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


def display_menu():
    """
    Display the main menu options to the user.
    """
    print("\nChoose an option:")
    print(f"{TEXT_TO_MORSE}. Convert text to Morse code")
    print(f"{MORSE_TO_TEXT}. Convert Morse code to text")
    print(f"{FILE_TEXT_TO_MORSE}. Convert text from a file to Morse code and save to another file")
    print(f"{FILE_MORSE_TO_TEXT}. Convert Morse code from a file to text and save to another file")
    print(f"{EXIT}. Exit")


def read_from_file(filename):
    """
    Read and return content from a specified file.

    Parameters:
    - filename (str): The path to the file to be read.

    Returns:
    - str: The content of the file.
    """
    with open(filename, 'r') as file:
        return file.read()


def write_to_file(filename, content):
    """
    Write the given content to a specified file. If the file doesn't exist, it will be created.
    If it does exist, the content will overwrite the existing content.

    Parameters:
    - filename (str): The path to the file where content will be written.
    - content (str): The content to be written to the file.
    """
    with open(filename, 'w') as file:
        file.write(content)


def main():
    while True:
        display_menu()  # Displaying the main menu

        choice = input("> ").strip()

        if choice == TEXT_TO_MORSE:
            # Handle text to Morse code conversion
            user_input = input(
                "Enter a string to convert to Morse Code: ").upper()
            print(convert_to_morse(user_input))

        elif choice == MORSE_TO_TEXT:
            # Handle text to Morse code conversion from file
            user_input = input("Enter Morse Code to convert to text: ")
            print(convert_from_morse(user_input))

        elif choice == FILE_TEXT_TO_MORSE:  # Reading text from file
            input_filename = input(
                "Enter the name of the file with the text: ")
            output_filename = input(
                "Enter the name of the file to save the Morse code: ")
            file_content = read_from_file(input_filename).upper()
            morse_code = convert_to_morse(file_content)
            write_to_file(output_filename, morse_code)
            print(f"Morse code saved to {output_filename}")

        elif choice == FILE_MORSE_TO_TEXT:  # Reading Morse code from file
            input_filename = input(
                "Enter the name of the file with the Morse code: ")
            output_filename = input(
                "Enter the name of the file to save the text: ")
            morse_content = read_from_file(input_filename)
            text_content = convert_from_morse(morse_content)
            write_to_file(output_filename, text_content)
            print(f"Text saved to {output_filename}")

        elif choice == EXIT:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
