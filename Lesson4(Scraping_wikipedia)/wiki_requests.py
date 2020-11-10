# https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0
import requests

def get_wiki_page(topic):
    link = f'https://ru.wikipedia.org/wiki/{topic}'
    wiki_page = requests.get(link).text
    return wiki_page

if __name__ == '__main__':
    print(get_wiki_page('Бендеры'))