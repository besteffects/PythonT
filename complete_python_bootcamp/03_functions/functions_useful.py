from random import shuffle

work_hours = [('Abby', 100), ('Billy', 4000), ('Cassie', 800)]


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

        return (employee_of_month, current_max)


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number 0,1, or 2")


myindex = player_guess()


def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)


# INITIAL LIST
mylist = [' ', ' ', ' ']

# SHUFFLE LIST
mixedup_list = shuffle_list(mylist)

# USER GUESS
guess = player_guess()

# CHECK GUESS
check_guess(mixedup_list, guess)

def myfunc(*args):
    mylist =[]
    for arg in args:
        if arg % 2 == 0:
            mylist.append(arg)
    return mylist

def convert_case1(x):
    out = []
    for i in range(len(x)):
        if i % 2 == 0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)

def convert_case(my_string): # To be fixed :)
    result_list = []
    index = 0
    for letter in my_string:
        if my_string[index] % 2 == 0:
            result_list.append(letter.upper())
        else:
            result_list.append(letter.lower())
        index = index + 1
    print(''.join(result_list))
    return ''.join(result_list)

#  Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
    mylist = []
    for i in range(0, len(text)):
        mylist.append(text[i]*3)
    return ''.join(mylist)

def paper_doll1(text):
    result = ''
    for char in text:
        result += char * 3
    return result

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19
def blackjack(a, b, c):
    if sum((a, b, c)) <= 21:
        return sum((a,b,c))
    elif sum((a, b, c)) > 21 and a == 11 or b == 11 or c == 11:
        newsum = sum((a, b, c)) - 10
        return newsum
    else:
        return 'BUST'

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)  # code.remove(num) also works

    return len(code) == 1

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number¶
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

if __name__ == '__main__':
    # result = employee_check(work_hours)
    # print(result)
    # name, hours = employee_check(work_hours)
    # print(name)
    # convert_case()
    mystring = 'AcfgfsfgAbVFa'
    convert_case1(mystring)
