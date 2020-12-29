import random


def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def simple_gen():
    for y in range(3):
        yield y


for number in simple_gen():
    print(number)

g = simple_gen()

print(next(g))


# Problem 1
# Create a generator that generates the squares of numbers up to some number N.


def gen_squares(n):
    for a in range(n):
        yield a ** 2


for x in gen_squares(10):
    print(x)

# Problem 2
# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
# Note: Use the random library. For example:


def rand_num(low, high, n):
    for z in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)

# s_iter = iter(s) # Iterate through string
# Use the iter() function to convert the string below into an iterator:

s = 'hello'
s_iter = iter(s)

#  Can you explain what gencomp is in the code below? (Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)