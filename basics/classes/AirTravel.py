"""Model for aircraft flights."""


class Flight:

    # initializer does not return anything
    def __init__(self, number):  # __init__ is an initializer, not a constructor
        if not number[:2].isalpha():  # Check if all the characters in the text are letters
            raise ValueError(f"No airline code in '{number}")
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code'{number}")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")
        self._number = number

    def number(self):  # self is analogue to this in Java
        return self._number  # getter

    def airline(self):
        return self._number[:2]
