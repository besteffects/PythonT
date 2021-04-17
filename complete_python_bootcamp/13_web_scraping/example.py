import requests
import bs4

def example():
    result = requests.get("http://example.com/")
    print(type(result))
    #print(result.text)
    soup = bs4.BeautifulSoup(result.text, "lxml")
    print(soup)
    print(soup.select("title"))
    
    # to get the text get the first item from the list
    title_text = soup.select('title')[0].getText()
    print(title_text)


if __name__ == '__main__':
    example()
