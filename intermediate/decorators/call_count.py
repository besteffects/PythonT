#  Class in a role of decorator
class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print("Hello {}".format(name))

# from intermediate.decorators.call_count import hello
# hello('Wilma')
