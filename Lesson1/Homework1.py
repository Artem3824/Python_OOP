# В этом упражнении необходимо выполнить задание из нескольких шагов для практики использования регулярных выражений и реализации нескольких полезных функций. Следуйте алгоритму:

print('\n 1. Get text from the file.\n')
import re

with open('text.txt', 'r', encoding='utf-8') as f:
    content = f.read()

print(content)

print('\n 2. Divide the text into sentences.\n')

# 2. Разбейте полученные текст на предложения.
# Примечание: Напоминаем, что в русском языке предложения заканчиваются на ., ! или ?.

pattern_sent = '\.[ ,\n,]|\![ ,\n,]|\?[ ,\n,]'
sentenses = re.split(pattern_sent, content)

# Result by list
print(sentenses)

# получение всех предложений столбиком
# for i in sentenses:
#     print(i)

print('\n 3. Find words containing 4 letters or more. Display top 10 often used words.\n')
# 3. Найдите слова, состоящие из 4 букв и более. Выведите на экран 10 самых часто используемых слов.
# Пример вывода: [(“привет”, 3), (“люди”, 3), (“город”, 2)].

pattern_words = '[а-яА-я]{4,}'
words_4 = re.findall(pattern_words, content)
unique_words = set(words_4) # все уникальные значения слов
sorted_words = sorted(unique_words, key=lambda word: words_4.count(word), reverse=True) # сортировка слов по количеству повторений
sorted_amount = sorted([words_4.count(i) for i in unique_words], reverse=True) # количество повторений слов

sorted_result = list(zip(sorted_words, sorted_amount)) # список слов и их количество повторений
top_10 = [sorted_result[i] for i in range(10)] # 10 самых часто используемых слов
print(sorted_result)
print(top_10)


print('\n 4. Find all links.\n')
# 4. Отберите все ссылки.
# Примечание: Для поиска воспользуйтесь методом compile, в который вы вставите свой шаблон для поиска ссылок в тексте.

pat_link = '\).(\w+\.?[a-z]+\.ru\/?\w*)'
pattern_links = re.compile(pat_link)
print(pattern_links.findall(content))


print('\n 5. Find a domain to which there are more links\n')
# 5. Ссылки на страницы какого домена встречаются чаще всего?
# Напоминаем, что доменное имя — часть ссылки до первого символа «слеш». Например в ссылке вида travel.mail.ru/travel?id=5 доменным именем является travel.mail.ru.
# Подсчет частоты сделайте по аналогии с заданием 3, но верните только одну самую частую ссылку.

pattern_domen = re.compile('\).((\w+\.?[a-z]+\.ru)\/?\w*)')
links_domens = pattern_domen.findall(content) # находим все значения доменов и отдельно цельные домены
# print(links_domens)

new_domens = [links_domens[i][1] for i in range(len(links_domens))] # выбираем все домены
# print(new_domens)
unique_domens = set(new_domens) # выделяем уникальные домены
max_domen = sorted(unique_domens, key=lambda word: new_domens.count(word), reverse=True) # сортируем по количеству повторений от большего к меньшему

print(f'Чаще всего встречаются ссылка на домен {max_domen[0]}')


print('\n 6. Replace all of the links to the text: «Link will be displayed after registration».\n')
# 6. Замените все ссылки на текст «Ссылка отобразится после регистрации».

new_content = pattern_links.sub(') Ссылка отобразится после регистрации', content)
print(new_content)