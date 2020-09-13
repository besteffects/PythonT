import random


def simple_list():
    performances = ['Ventriloquism', 'Amazing Acrobatics', 'Enchanted Elephants', 'Bearded Lady', 'Tiniest Man']
    performances.append('Snake Charmer')
    print(performances)
    performances.remove('Bearded Lady')
    performances.remove('Tiniest Man')
    print(performances)


def simple_dictionary():
    performances = {'Ventriloquism': '9:00am', 'Snake Charmer': '12:00pm'}
    performances['Amazing Acrobatics'] = '2:00pm'
    performances['Enchanted Elephants'] = '5:00pm'
    performances['Bearded Lady']='5:00pm'
    print(performances)
    showtime = performances.get('Bearded Lady')
    if showtime is None:
        print("Performance doesn't exist")
    else:
        print("The time of the Bearded Lady show is " + showtime)


def random_test():
    for i in range(5):
        ticket = random.randint(1, 53)
        print(ticket)


def dict_loop():
    performances = {'Ventriloquism': '9:00am',
                    'Snake Charmer': '12:00pm',
                    'Amazing Acrobatics': '2:00pm',
                    'Enchanted Elephants': '5:00pm'}
    for name, time in performances.items():
        print(name, ':', time, sep='')
