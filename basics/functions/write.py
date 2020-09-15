def write_sales_log(order):
    """Function for writing data to a file"""
    file = open('sales.txt', 'a')
    total = 0
    for item, price in order.items():
        file.write(item + ' ' + format(price, '.2f') + '\n')
        total += price

    file.write('total = ' + format(total, '.2f') + '\n')
    file.close()


def main():
    order = {'Cheeky Spam': 1.0, 'Yonks Spam': 4.0}
    write_sales_log(order)
    order = {'Cheerio Spam': 1.0, 'Smashing Spam': 3.0}
    write_sales_log(order)
