import pandas


def read_input():
    """
    Function reads user input text from console.

    Args:
    None

    Returns:
        str: Text from console.

    Raises:
        IOError: When there is a problem in input/output operation.
    """
    try:
        return input("Enter text: ")
    except IOError:
        raise IOError("Input/Output Error.")


def read_file_python(file_path):
    """
     Reads text data from the specified file.

     Parameters:
        file_path (str): The path to the file that is being read.

    Returns:
        str: Text from the file.

    Raises:
        FileNotFoundError: If the file given by user does not exist.
        IOError: When there is a problem in input/output operation.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}.")
    except IOError as e:
        raise IOError(f"Input/Output Error: {e}.")


def read_file_pandas(file_path):
    """
     Reads text data from the specified file using pandas library.

     Parameters:
        file_path (str): The path to the file that is being read.

    Returns:
        str: Text from the file.

    Raises:
        FileNotFoundError: If the file given by user does not exist.
        IOError: When there is a problem in input/output operation.
    """
    try:
        return pandas.read_csv(file_path).to_string(index=False)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}.")
    except IOError as e:
        raise IOError(f"Input/Output Error: {e}.")
