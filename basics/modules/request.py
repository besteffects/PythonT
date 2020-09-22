import requests


def get_data():
    my_request = requests.get('http://go.codeschool.com/spamvanmenu')
    menu_list = my_request.json()
    print("Today's Menu: ")
    for item in menu_list:
        print(item['name'], ': ', item['desc'].title(), ', $',
              item['price'], sep='')


def get_spam_data():
    first_item = {'name': 'Spam n Eggs', 'desc': 'Two eggs with Spam', 'price': 2.50}
    second_item = {'name': 'Spam n Jam', 'desc': 'Biscuit with Jam with Spam', 'price': 3.50}
    third_item = {'name': 'Spam n Ham', 'desc': 'Spam n Ham', 'price': 4.50}
    print(first_item['name'], first_item['price'])
    print(second_item['name'], second_item['price'])
    menu_items = [first_item, second_item, third_item]  # the same as json with 3 elements
    print(menu_items[0]['name'], menu_items[0]['price'], menu_items[0]['desc'])
    print(menu_items[1]['name'], menu_items[1]['price'], menu_items[1]['desc'])

    my_request = requests.get('http://go.codeschool.com/spamvanmenu')
    menu_list = my_request.json()

    print("Today's Menu:")
    for item in menu_list:
        print(item['name'], ': ', item['desc'].title(), ', $',
              item['price'], sep='')


if __name__ == '__main__':
    get_data()
    get_spam_data()
