def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

def simple_gen():
    for x in range(3):
        yield x


for number in simple_gen():
    print(number)

g = simple_gen()

print(next(g))

# Problem 1
# Create a generator that generates the squares of numbers up to some number N.


def gen_squares(N):
    for x in range(N):
        yield x**2


for x in gen_squares(10):
    print(x)