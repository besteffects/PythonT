import math
import string


# 1. Write a function that computes the volume of a sphere given its radius.
def sphere_volume(radius):
    volume = 4 / 3 * math.pi * pow(radius, 3)
    return volume


# 2. Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num, low, high):
    return low <= num <= high


def ran_check1(num, low, high):
    if low <= num <= high:
        return (f"{num} is in the range between {low} and {high}")
    else:
        return ("{0} is outside of the range {1} and {2}".format(num, low, high))


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
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
            lowercase += 1
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


def up_low_dict(s):
    d = {'upper': 0, 'lower': 0}
    for char in s:
        if char.isupper():
            d['upper'] += 1
        elif char.islower():
            d['lower'] += 1
        else:
            pass
    print(f"Lowecase count: {d['lower']}")
    print(f"Uppercase count: {d['upper']}")

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    #  alternatively:
    # s = set()
    # for item in lst:
    #     s.add(item)
    # my_list = list(s)
    return list(set(lst))


# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    result = 1
    for i in numbers:
        result = result * i
    return result


# Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(s):
    s1 = s.replace(" ", "")
    return s1 == s1[::-1]


def palindrome1(s):
    s1 = s.replace(" ", "")
    return s1 == ''.join(reversed(s1))


# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

def ispangram(str1, alphabet=string.ascii_lowercase):
    my_set = set(str1)
    alphabet_set = set(alphabet)
    return my_set.issuperset(alphabet_set)


if __name__ == '__main__':
    # print(ran_check1(2, 5, 4))
    up_low("Hello Mr. Rogers, how are you this fine Tuesday?")
    up_low_colect("Hello Mr. Rogers, how are you this fine Tuesday?")
    print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))
    print(multiply([1, 2, 3, -4]))
    print(palindrome('hel le h'))
    print(palindrome1('hel le h'))
