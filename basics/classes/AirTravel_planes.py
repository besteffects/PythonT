"""Model for aircraft flights.
In this file relocate_passenger() method was added and some code improvements
were done"""


class Flight:
    """A flight with a particular passenger aircraft"""

    # initializer does not return anything
    def __init__(self, number, aircraft):  # __init__ is an initializer, not a constructor
        #  Purpose of __init__ - to configure an object that already exists once __init__ is called
        if not number[:2].isalpha():  # Check if all the characters in the text are letters
            raise ValueError(f"No airline code in '{number}")
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code'{number}")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")
        #  For accepting aircraft object when it is being constructed
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()  # initialize seating plan
        # To single element list containing None we concat. another list containing one entry for each
        # row in the aircraft
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):  # self is analogue to this in Java
        return self._number  # getter

    #  delegates aircraft on behalf of the client rather than interrogate aircraft object directly
    def aircraft_model(self):
        return self._aircraft.model()

    def airline(self):  # Return the airline code
        return self._number[:2]

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger
        Args:
            seat: A seat designator such as '12C' or '21F'.
            passenger: The passenger name

        Raises:
            ValueError: If the seat is unavailable.
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:  # Check if requested seat is unoccupied
            raise ValueError(f"Seat{seat} already occupied")  # raise an error if occupied
        self._seating[row][letter] = passenger  # Assign a seat

        # Refactored version

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]  # Get the seat letter by using negative indexing in seat string
        if letter not in seat_letters:  # testing that seat letter is valid
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]  # extract row using string slicing using all but the last character
        try:
            row = int(row_text)  # try to convert row number into the integer using int constructor
        except ValueError:  # catch ValueError and raise a new Value error with a custom message
            raise ValueError(f"Invalid seat row {row_text}")

        if row not in rows:  # Validate row number
            raise ValueError(f"Invalid row number {row}")
        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat
        Args:
            from_seat: The existing seat designator for the passenger to be moved
            to_seat: The new seat designator"""
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat{from_seat}")
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        """Defines how many seats are available"""
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """An iterable series of passenger seating locations"""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield passenger, f"{row}{letter}"


class Aircraft:
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):
    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        # For simplicity's sake, we ignore comple
        # seating arrangement for first-class
        return range(1, 56), "ABCDEF"


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f"| Name: {passenger}" \
             f" Flight: {flight_number}" \
             f" Seat: {seat}" \
             f" Aircraft: {aircraft}" \
             " |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()


def make_flights():
    f = Flight("BA758", AirbusA319("G-EUPT"))
    f.allocate_seat("12A", "Guido van Rossum")
    f.allocate_seat("15F", "Bjarne Stroustrup")
    f.allocate_seat("15E", "Anders Hejlsberg")
    f.allocate_seat("1C", "John McCarthy")
    f.allocate_seat("1D", "Rich Hickey")

    g = Flight("AF72", Boeing777("F-GSPS"))
    g.allocate_seat("55K", "Guido van Rossum")
    g.allocate_seat("133G", "Bjarne Stroustrup")
    g.allocate_seat("4B", "Anders Hejlsberg")
    g.allocate_seat("4A", "John McCarthy")
    g.allocate_seat("5C", "Random Name")
    return f, g  # Return both flights as a tuple
