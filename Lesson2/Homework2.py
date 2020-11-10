import re
from bs4 import BeautifulSoup

with open('index.html', encoding='utf-8') as f:
    s = f.read()

print('1. Using regular expressions:')
amount = re.compile('<span class=\"total-users\">(.*?)</span>', re.DOTALL)
print(amount.findall(s)[0])

print('\n2. Using library BeautifulSoup4:')
soup = BeautifulSoup(s, 'html.parser')
students = soup.find(attrs={'class': ['total-users']})
print(students.text)
