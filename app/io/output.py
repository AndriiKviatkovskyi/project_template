def print_output(text):
    """
    Function prints text in console.

    Args:
        text (str): Text that is being printed.

    Returns:
    None

    Raises:
        IOError: When there is a problem in input/output operation.
    """
    try:
        print(text)
    except IOError:
        raise IOError("Input/Output Error.")


def write_file(text, file_path):
    """
     Writes text data into the specified file.

     Parameters:
        text (str): Text that is being written into the file.
        file_path (str): The path to the file that is being read.

    Returns:
    None

    Raises:
        FileNotFoundError: If the file given by user does not exist.
        IOError: When there is a problem in input/output operation.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(text)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}.")
    except IOError as e:
        raise IOError(f"Input/Output Error: {e}.")
