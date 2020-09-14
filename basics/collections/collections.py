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


def customer_order():
    orders = []  # orders list to save the orders
    menu = ['Cheeky Spam', 'Borsh', 'Chicken Soup']
    order = input("What would you like to order? (Q to Quit)")
    while (True):
        if order == 'Cheeky Spam':
            print('Sorry, we\'re all out of that!')
            continue  # Stops the loop, then jumps to the beginning and continues running
        if order.upper() == 'Q':
            break
        # Find the order and add it to the list if it exists
        found = menu.get(order)
        if found:
            orders.append(order)
        else:
            print("Menu item doesn't exist")
        # See if the customer wants to order anything else
        order = input("Anything else? (Q to Quit)")
    print(orders)


def customer_order1():
    orders = []
    menu = ['Cheeky Spam', 'Borsh', 'Chicken Soup']
    order = input("What would you like to order? (Q to Quit)")
    while (order.upper() != 'Q'):
        #  Find the order and add it to the list if it exists
        found = menu.get(order)
        if found:
            orders.append(order)
        else:
            print("Menu item doesn't exist")
        #  See if the customer wants to order anything else
        order = input("Anything else? (Q to Quit)")
    print(orders)