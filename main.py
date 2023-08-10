"""
Morse Code Converter

This script allows the user to convert text to Morse code and vice versa.
The user can also read text or Morse code from a file and save the results to another file.

Usage:
    Run the script and choose an option from the displayed menu.
"""

from file_handler import read_from_file, write_to_file
from morse_converter import convert_to_morse, convert_from_morse

# ======================
# CONSTANTS
# ======================
TEXT_TO_MORSE = "1"
MORSE_TO_TEXT = "2"
FILE_TEXT_TO_MORSE = "3"
FILE_MORSE_TO_TEXT = "4"
EXIT = "5"


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


def main():
    while True:
        display_menu()

        choice = input("> ").strip()

        # Convert text input to Morse code
        if choice == TEXT_TO_MORSE:
            user_input = input(
                "Enter a string to convert to Morse Code: ").upper()
            print(convert_to_morse(user_input))

        # Convert Morse code input to text
        elif choice == MORSE_TO_TEXT:
            user_input = input("Enter Morse Code to convert to text: ")
            print(convert_from_morse(user_input))

        # Convert text from a file to Morse code
        elif choice == FILE_TEXT_TO_MORSE:
            input_filename = input(
                "Enter the name of the file with the text: ")
            file_content = read_from_file(input_filename).upper()
            if not file_content:
                continue
            output_filename = input(
                "Enter the name of the file to save the Morse code: ")
            morse_code = convert_to_morse(file_content)
            write_to_file(output_filename, morse_code)
            print(f"Morse code saved to {output_filename}")

        # Convert Morse code from a file to text
        elif choice == FILE_MORSE_TO_TEXT:
            input_filename = input(
                "Enter the name of the file with the Morse code: ")
            morse_content = read_from_file(input_filename)
            if not morse_content:
                continue
            output_filename = input(
                "Enter the name of the file to save the text: ")
            text_content = convert_from_morse(morse_content)
            write_to_file(output_filename, text_content)
            print(f"Text saved to {output_filename}")

        # Exit the application
        elif choice == EXIT:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
