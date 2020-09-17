def write_sales_log(order):
    """Function for writing data to a file"""
    file = open('sales.txt', 'a')
    total = 0
    for item, price in order.items():
        file.write(item + ' ' + format(price, '.2f') + '\n')
        total += price

    file.write('total = ' + format(total, '.2f') + '\n')
    file.close()


# Writing data to a file
def read_data_from_file():
    performances1 = {}
    # performances = {'Ventriloquism': '9:00am',
    #                 'Snake Charmer': '12:00pm',
    #                 'Amazing Acrobatics': '2:00pm',
    #                 'Enchanted Elephants': '5:00pm'}
    try:
        schedule_file = open('schedule.txt', 'r')
    except FileNotFoundError as err:
        print(err, "File doesn't exist")
        for line in schedule_file:
            (show, time) = line.split(' - ')
            performances1[show] = time
            time = time.strip()
            print(show, time)
        schedule_file.close()
        print(performances1)


# Reading data
def read_dollar_menu():
    dollar_spam = open('dollar_menu.txt', 'r')
    dollar_menu = []
    for line in dollar_spam:
        line = line.strip()
        dollar_menu.append(line)
    print(dollar_menu)
    dollar_spam.close()


def main():
    order = {'Cheeky Spam': 1.0, 'Yonks Spam': 4.0}
    write_sales_log(order)
    order = {'Cheerio Spam': 1.0, 'Smashing Spam': 3.0}
    write_sales_log(order)
