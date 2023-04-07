#!/usr/bin/python3
"""Python function for adding new lines based on the (.), (?) and  (:)
and ensuring there is no identation before or after a newline
"""


def text_indentation(text):
    """function for adding a new line and checking
    the type of input
    to be a string otherwise raising a TypeError
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    char = 0
    while char < len(text) and text[char] == ' ':
        char += 1

    while char < len(text):
        print(text[char], end="")
        if text[char] == "\n" or text[char] in ".?:":
            if text[char] in ".?:":
                print("\n")
            char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
            continue
        char += 1
