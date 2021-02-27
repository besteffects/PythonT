import math
# Advanced Numbers
# Problem 1: Convert 1024 to binary and hexadecimal representation
def convert_to_binary(num):
    binary_num = bin(num)
    hexadecimal = hex(num)

# Problem 2: Round 5.23222 to two decimal places
def round_to_decimal(num):
    round(num, 2)

# Problem 3: Check if every letter in the string s is lower case
def check_if_lowercase(my_string):
    my_string.islower()


# Problem 4: How many times does the letter 'w' show up in the string below?
def count_times(my_string):
    my_string = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
    my_string.count('w')

# Problem 5: Find the elements in set1 that are not in set2:


def find_not_in_set(s1, s2):
    print(s1.difference(s2))

#Problem 6: Find all elements that are in either set:
def find_not_in_either_sets(s1, s2):
    print(s1.union(s2))


# Problem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension.
def dict_comprenhension():
    print({x: x**3 for x in range(5)})


# Problem 8: Reverse the list below:
def reverse_list():
    list1 = [1, 2, 3, 4]
    list1.reverse()
    print(list1)

# Problem 9: Sort the list below:
def sort_list():
    list1 = [1, 2, 3, 4]
    list1.sort()
    print(list1)

if __name__ == "__main__":
    set1 = {2, 3, 1, 5, 6, 8}
    set2 = {3, 1, 7, 5, 6, 8}
    find_not_in_set(set1, set2)
    find_not_in_either_sets(set1, set2)
    dict_comprenhension()
    reverse_list()
    sort_list()