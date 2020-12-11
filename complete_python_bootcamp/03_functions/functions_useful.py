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

if __name__ == '__main__':
    # result = employee_check(work_hours)
    # print(result)
    # name, hours = employee_check(work_hours)
    # print(name)
    # convert_case()
    mystring = 'AcfgfsfgAbVFa'
    convert_case1(mystring)
