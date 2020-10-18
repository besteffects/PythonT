def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

@escape_unicode
def northern_city():
    return 'Tromsø'

# to run:
# from intermediate.decorators.first_example import northern_city
# >>> northern_city()