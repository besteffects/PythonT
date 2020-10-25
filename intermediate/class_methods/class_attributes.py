class ShippingContainer:
    next_serial = None
    #  Accessing class attributes

    def __init__(self, owner_code, contents):

        next_serial = 1337

        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
