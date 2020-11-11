import contextlib

@contextlib.contextmanager
def nest_test(name):
    print("Entering", name)
    yield name
    print("Exiting", name)


with nest_test('outer') as n1, nest_test('inner, nested in ' + n1):
    print('BODY')


@contextlib.contextmanager
def propagater(name, propagate):
    try:
        yield
        print(name, 'exited normally.')
    except Exception:
        print(name, 'received and exception!')
        if propagate:
            raise


with propagater('outer', True), propagater('inner', False):
    raise TypeError ('Cannot convert')
