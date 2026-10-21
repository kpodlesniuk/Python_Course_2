#!/usr/bin/env python3

"""Exercise 1: File Operations.

Create a function that performs operations with files.

The function accepts three arguments: the file operation type, the file
path, and optional content. It performs the requested operation with the
file and displays the file content when reading.

The function includes error handling for common input and file errors.
"""


def file_operations(operation, file_path, content=None):
    """Perform the requested operation with a file.

    Args:
        operation: Type of file operation to perform.
        file_path: Path to the file.
        content: Content to write or append to the file.
    """
    try:
        if operation in ("write", "append") and content is None:
            raise ValueError("Content is required!")
        if operation == "read":
            with open(file_path, "r") as file:
                print(file.read())
        elif operation == "write":
            with open(file_path, "w") as file:
                file.write(content)
        elif operation == "append":
            with open(file_path, "a") as file:
                file.write(content)
        else:
            raise ValueError("Operation not supported!")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    except IsADirectoryError:
        print("The specified path is a directory, not a file!")
    except TypeError:
        print("Content must be a string!")
    except ValueError as error:
        print(error)


file_operations("write", "test.txt", "I am learning Python!")
file_operations("append", "test.txt", "\nAnd file operations!")
file_operations("read", "test.txt")

file_operations("read", "potato.txt")
file_operations("write", "does_not_exist/potato.txt", "I am learning Python!")
file_operations("potato", "test.txt")
file_operations("write", "test.txt")
file_operations("read", "")
file_operations("write", "test.txt", 123)
