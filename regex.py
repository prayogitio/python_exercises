import re

def anti_vowel(text):
  #replace every vowel with empty
  regex = r"([aiueoAIUEO]+)"
  text = re.sub(regex,'',text)
  return text

print (anti_vowel("Hey What's up guyss!"))

def censor(text, word):
  #censor every 'hey word in the text/first argument'
  regex = r"(" + word +")"
  text = re.sub(regex, '*' * len(word), text)
  return text

print (censor("hey hey tey hey is hey hey", "hey"))