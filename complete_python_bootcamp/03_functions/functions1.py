import math

# 1. Write a function that computes the volume of a sphere given its radius.
def sphere_volume(radius):
    volume = 4/3*math.pi*pow(radius, 3)
    return volume

# 2. Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    return low <= num <= high

def ran_check1(num,low,high):
    if low <= num <= high:
        return (f"{num} is in the range between {low} and {high}")
    else:
        return ("{0} is outside of the range {1} and {2}".format(num, low, high))

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
#
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
# HINT: Two string methods that might prove useful: .isupper() and .islower()
# If you feel ambitious, explore the Collections module to solve this problem!

def up_low(s):
    uppercase = 0
    lowercase = 0
    for letter in s:
        if letter.isupper():
            uppercase = uppercase + 1
        if letter.islower():
            lowercase = lowercase + 1
    print(uppercase)
    print(lowercase)

def up_low_colect(s):
    uppercase = []
    lowercase = []
    for letter in s:
        if letter.isupper():
            uppercase.append(letter)
        if letter.islower():
            lowercase.append(letter)
    print(len(uppercase))
    print(len(lowercase))


if __name__ == '__main__':
   # print(ran_check1(2, 5, 4))
   up_low("Hello Mr. Rogers, how are you this fine Tuesday?")
   up_low_colect("Hello Mr. Rogers, how are you this fine Tuesday?")