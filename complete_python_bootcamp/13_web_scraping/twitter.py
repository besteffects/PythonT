import requests
import bs4


def example():
    result = requests.get("https://twitter.com/childrightscnct")
    soup = bs4.BeautifulSoup(result.text, "lxml")
    print(soup)
    # to get the text get the first item from the list
    my_text = soup.select('.css-1dbjc4n.r-zl2h9q')
    print(my_text)

if __name__ == '__main__':
    example()
