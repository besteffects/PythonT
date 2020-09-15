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
performances = {'Ventriloquism': '9:00am',
                'Snake Charmer': '12:00pm',
                'Amazing Acrobatics': '2:00pm',
                'Enchanted Elephants': '5:00pm'}
schedule_file = open('schedule.txt', 'w')  # w - write, r - read, a - append
for key, val in performances.items():
    schedule_file.write((key + ' - ' + val) + '\n')
schedule_file.close()


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
