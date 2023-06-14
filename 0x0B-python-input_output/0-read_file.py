def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file does not exist.

    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')
