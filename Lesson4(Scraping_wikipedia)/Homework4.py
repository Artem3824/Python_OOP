from wiki_requests import get_wiki_page
import re
import requests
from bs4 import BeautifulSoup


def get_topic_words(topic):
    html_content = get_wiki_page(topic)
    words = re.findall('[а-яА-я\-\']{3,}', html_content)
    return words


def get_common_words(topic):
    words_list = get_topic_words(topic)
    rate = {}
    for word in words_list:
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1
    rate_list = list(rate.items())
    rate_list.sort(key=lambda x: x[1], reverse=True)
    return rate_list

common_words_list = []

def visualize_common_words(topic):
    words = get_common_words(topic)
    for word in words[0:10]:
        common_words_list.append(word[0])


def main():
    topic = input('Введите поисковое слово: ')
    visualize_common_words(topic) # Common topic words
    neighboor_words(topic) # Topic neighbour words
    print(sorted(set(common_words_list))) # Sorted list of all common words
    print(f'Общее число уникальных слов - {len(common_words_list)}')


def neighboor_words(topic):
    main_link = get_wiki_page(topic)
    soup = BeautifulSoup(main_link, 'lxml')
    links_to_pages = soup.find_all('a', limit=20) # Search of neighbour words (limit - 20 links)
    list_links = []
    for i in links_to_pages:
        list_links.append(i.get('href', ''))
    unique_links = set(list_links) # Find unique links due to set
    pattern = '\/wiki\/([%\w\d,]+)' # Choose only links with pattern /wiki/
    unique_links_text = ' '.join(unique_links)
    wiki_links = re.findall(pattern, unique_links_text) # Get list of neighbour pages
    for topic in wiki_links:
        visualize_common_words(topic) # Get list of common words for each link

main()



















