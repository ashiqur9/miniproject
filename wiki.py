import requests
from bs4 import BeautifulSoup
import webbrowser
def wikisearch(word):
    word = word.split()

    search_link = 'https://en.wikipedia.org/w/index.php?cirrusUserTesting=glent_m0&sort=relevance&search='
    search_link = search_link + '+'.join(word)
    print(search_link)
    search_result = requests.get(search_link).text
    soup = BeautifulSoup(search_result, 'html.parser')
    wikis = soup.select('.mw-search-result-heading')

    try:
        final_link = wikis[0]
        result = final_link.a

        search = 'https://en.wikipedia.org/' + result['href']
    except IndexError:
        final_link=wikis
        search=search_link
    return search


    #webbrowser.open(search)
def wikis_summury(search_link):
    search_result=requests.get(search_link).text
    file=open('summury.txt','w')
    file.write(search_result)
    file.close()

text=wikisearch('donald trump')
wikis_summury(text)