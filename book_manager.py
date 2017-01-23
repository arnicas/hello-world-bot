import nltk # for sentence parsing
import random
nltk.download('punkt') # we're only getting the bare minimum of what we need from nltk
book_file = 'book.txt'

class BookManager:
  def __init__(self):
    text_file = open(book_file, 'r+')
    text_string = text_file.read()
    text_file.close()
    self._text_string = text_string

  def delete_message(self, message):
    text_file = open(book_file, 'r+')
    text_file.seek(0)
    text_file.write(self.text_without_message(message))
    text_file.truncate()
    text_file.close()

  def random_sentence(self):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(self._text_string)
    upper = len(sentences)
    location = random.randrange(0, upper-140)
    return sentences[location]

  def first_sentence(self):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(self._text_string)
    return sentences[0]

  def text_without_message(self, message):
    return self._text_string[len(message):len(self._text_string)]
