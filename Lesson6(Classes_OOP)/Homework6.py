class Word:
    def __init__(self, text, part):
        self.text = text
        self.part = part

class Sentence:
    def __init__(self, content):
        self.content = content

    def show(self):
        sentense = []
        for word in self.content:
            sentense.append(words[word].text)
        print(' '.join(sentense))

    def show_parts(self):
        sentense_parts = []
        for part in self.content:
            sentense_parts.append(words[part].part_method())
        print(set(sentense_parts))


class Noun(Word):
    def __init__(self, text):
        self.text = text
        self.__grammar = 'сущ'

    def part_method(self):
        return 'существиетльное'

class Verb(Word):
    def __init__(self, text):
        self.text = text
        self.__grammar = 'гл'

    def part_method(self):
        return 'глагол'


word_dog = Noun('собака')
word_eat = Verb('ела')
word_meet = Noun('мясо')
word_evening = Verb('и бегала')

words = [word_dog, word_eat, word_meet, word_evening]

new_sentence = Sentence([0, 1, 2, 3])
new_sentence.show()
new_sentence.show_parts()