# Instances of decorators
class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)

        return wrap

tracer = Trace()  # instances of Trace() are decorators

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

# from intermediate.decorators.tracer import rotate_list, tracer
# l = [1, 2, 3]
# l = rotate_list(l)
# l
# tracer.enabled = False  - to disabled tracing
