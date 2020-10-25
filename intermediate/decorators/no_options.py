import functools

def noop(f):
    @functools.wraps(f)  # using fanctools to get metadata from decorator
    def noop_wrapper():
        return f()

    # noop_wrapper.__name__ = f.__name__
    # noop_wrapper.__doc__ = f.__doc__
    return noop_wrapper

# When using decorators we can use docs data
@noop
def hello():
    "Print a well-known message."
    print("Hello, world!")
