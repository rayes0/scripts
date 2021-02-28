# Grabs anime quotes from www.less-real.com

import requests
from bs4 import BeautifulSoup
from writeJson import write_to_json

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) "
                                 "Chrome/22.0.1207.1 Safari/537.1"}

base_url = "http://www.less-real.com/?p="

python_list = []
index = 1
def increment():
    global index
    index += 1

def get_quotes( url ):
    try:
        start_url = requests.get(url, headers=headers)
        soup = BeautifulSoup(start_url.text, 'html.parser')

        quotes_div = soup.findAll("div", {"class": "quote"})

        for quote_div in quotes_div:
            author = quote_div.findAll('a', href=True)[0].text
            title = quote_div.findAll('a', href=True)[-1].text
            text = quote_div.find('span', {'class': 'quoteText'}).text

            python_dic = {
                "author": author,
                "title": title.strip("()"),
                "text": text.strip("\n\r").replace(u"\u2018", "'").replace(u"\u2019", "'"),
                "id": index
            }

            python_list.append(python_dic)
            increment()
    except:
        print("{} is not working".format(url))


if __name__ == '__main__':
    print("Connection established. Grabbing quotes...")
    for i in range(1, 432):
        get_quotes(base_url + str(i))
        print("Done page "+str(i)+"/431")

    print("\nFinished grabbing",len(python_list),"quotes")

    write_to_json(python_list)
