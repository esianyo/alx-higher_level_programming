#!/usr/bin/python3
"""
Matrix Division function
Esianyo Dzisenu
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list of lists: The new matrix with elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> div = 2
        >>> matrix_divided(matrix, div)
        [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]

        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> div = 0
        >>> matrix_divided(matrix, div)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: division by zero

        >>> matrix = [[1, 2, 3], [4, 5]]
        >>> div = 2
        >>> matrix_divided(matrix, div)
        Traceback (most recent call last):
            ...
        TypeError: Each row of the matrix must have the same size

        >>> matrix = [[1, 2, 3], [4, 5, "6"]]
        >>> div = 2
        >>> matrix_divided(matrix, div)
        Traceback (most recent call last):
            ...
        TypeError: Matrix must be a matrix (list of lists) of integers/floats
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row has the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("Div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("Division by zero")

    # Divide the matrix elements by div and round to 2 decimal places
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
