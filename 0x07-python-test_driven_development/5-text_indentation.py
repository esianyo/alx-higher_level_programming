#!/usr/bin/python3
"""
Indentation function
Esianyo Dzisenu
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?' and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> text_indentation("Hello. How are you? I'm fine.")
        Hello

        How are you

        I'm fine

        >>> text_indentation("This is a test.")
        This is a test

        >>> text_indentation("")

        >>> text_indentation(123)
        Traceback (most recent call last):
            ...
        TypeError: text must be a string
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text by '.', '?' and ':' characters
    sentences = text.split('.') + text.split('?') + text.split(':')
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    # Print each sentence with 2 new lines
    for sentence in sentences:
        print(sentence)
        print()
