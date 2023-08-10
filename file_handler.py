def read_from_file(filename):
    """
    Read and return content from a specified file.

    Parameters:
    - filename (str): The path to the file to be read.

    Returns:
    - str: The content of the file.
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{filename}'.")
    except IOError:
        print(f"Error: An I/O error occurred while reading '{filename}'.")
    return ""


def write_to_file(filename, content):
    """
    Write the given content to a specified file. If the file doesn't exist, it will be created.
    If it does exist, the content will overwrite the existing content.

    Parameters:
    - filename (str): The path to the file where content will be written.
    - content (str): The content to be written to the file.
    """
    try:
        with open(filename, 'w') as file:
            file.write(content)
    except PermissionError:
        print(
            f"Error: Permission denied when trying to write to '{filename}'.")
    except IOError:
        print(f"Error: An I/O error occurred while writing to '{filename}'.")
