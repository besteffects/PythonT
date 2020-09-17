import requests


def get_data():
    my_request = requests.get('http://go.codeschool.com/spamvanmenu')

    menu_list = my_request.json()

    print("Today's Menu: ")
    for item in menu_list:
        print(item['name'], ': ', item['desc'].title(), ', $',
              item['price'], sep='')


if __name__ == '__main__':
    get_data()
