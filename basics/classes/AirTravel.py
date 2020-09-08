"""Model for aircraft flights."""


class Flight:

    # initializer does not return anything
    def __init__(self, number, aircraft):  # __init__ is an initializer, not a constructor
        if not number[:2].isalpha():  # Check if all the characters in the text are letters
            raise ValueError(f"No airline code in '{number}")
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code'{number}")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        # To single element list containing None we concat. another list containing one entry for each
        # row in the aircraft
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):  # self is analogue to this in Java
        return self._number  # getter

    def aircraft_model(self):
        return self._aircraft.model()

    def airline(self):
        return self._number[:2]

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger
        Args:
            seat: A seat designator such as '12C' or '21F'.
            passenger: The passenger name

        Raises:
            ValueError: If the seat is unavailable.
        """
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]  # Get the seat letter by using negative indexing in seat string
        if letter not in seat_letters:  # testing that seat letter is valid
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]  # extract row using string slicing using all but the last character
        try:
            row = int(row_text)  # try to convert row number into the integer using int constructor
        except ValueError: # catch ValueError and raise a new Value error with a custom message
            raise ValueError(f"Invalid seat row {row_text}")

        if row not in rows:  # Validate row number
            raise ValueError(f"Invalid row number {row}")

        if self._seating[row][letter] is not None:  # Check if requested seat is unoccupied
            raise ValueError(f"Seat{seat} already occupied")  # raise an error if occupied
        self._seating[row][letter] = passenger  # Assign a seat


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHIJK"[:self._num_seats_per_row])
