import tweepy # for tweeting
import secrets # shhhh
from book_manager import BookManager # for getting sentences out of our book file

def fix_sentence(sentence):
  while len(sentence) > 140:
    words = sentence.split(" ")
    sentence = " ".join(words[:-1])
  return sentence

def get_next_chunk():
  # open text file
  book = BookManager()
  sentence = book.random_sentence()
  chunk = fix_sentence(sentence)
  #print(chunk)
  return chunk

def tweet(message):
  auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
  auth.set_access_token(secrets.access_token, secrets.access_token_secret)
  api = tweepy.API(auth)
  auth.secure = True
  print("Posting message {}".format(message))
  api.update_status(status=message)

if __name__ == '__main__':
  tweet(get_next_chunk())
