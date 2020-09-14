import random


def average(numbers):
    total = 0
    for price in numbers:
        total = total + price
    avg = total/len(numbers)
    return avg


def lotto_numbers():
    lotto_nums = []
    for i in range(5):
        lotto_nums.append(random.randint(1, 53))
    return lotto_nums


numbers = lotto_numbers()
print(numbers)


def get_order(menu):
    orders = []
    order = input("What would you like to order? (Q to quit)")
    while (order.upper() != 'Q'):
        #  find the order
        found = menu.get(order)
        if found:
            orders.append(order)
        else:
            print("Menu item doesn't exist")
        order = input("Anything else? (Q to Quit)")
    return orders


def print_menu(menu):
    for name, price in menu.items():
        print(name, ': $', format(price, '2f'), sep='')


def bill_total(orders, menu):
    total = 0
    for order in orders:
        total += menu[order]
    return total


def main():
    menu = {'Knackered Spam': 0.50, 'Pip pip Spam': 1.50, 'Borsh': 3.4}
    print(menu)
    orders = get_order(menu)
    total = bill_total(orders, menu)
    print("You ordered:", orders,
          "Your total is: $", format(total, '.2f'), sep='')


main()

