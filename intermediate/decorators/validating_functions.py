def check_non_negative(index):
    def validator(f):
        def wrap(*args):
            if args[index] < 0:
                raise  ValueError(
                    "Argument {} must be non-negative.".format(index))
            return f(*args)
        return wrap
    return validator

#  Use a decorator to validate a function
@check_non_negative(1)
def create_list(value, size):
    return [value] * size

# from validating_functions import create_list
# create_list ['a', 3]