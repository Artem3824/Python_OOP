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
            sentense_parts.append(words[part].part)
        print(set(sentense_parts))


word_dog = Word('собака', 'сущ')
word_eat = Word('ела', 'глагол')
word_meet = Word('мясо', 'сущ')
word_evening = Word('вечером', 'наречие')

words = [word_dog, word_eat, word_meet, word_evening]

new_sentence = Sentence([0, 1, 2, 3])
new_sentence.show()
new_sentence.show_parts()
