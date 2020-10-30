from intermediate.class_methods import iso6346


class ShippingContainer:

    next_serial = 1337

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6)) # ensuring it's 6 chars long

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial +=1
        return result

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.contents = contents
        self.bic = self._make_bic_code(  # using self. to get a polymorphic behaviour
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial()) # calling class method


class RefrigiratedShippingContainer(ShippingContainer):

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6),
                              category='R')
# from class_method import *
# c7 = ShippingContainer.create_empty("YML")
# c7.contents