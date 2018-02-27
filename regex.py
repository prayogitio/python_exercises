import re

def anti_vowel(text):
  regex = r"([aiueoAIUEO]+)"
  text = re.sub(regex,'',text)
  return text

print (anti_vowel("Hey What's up guys!"))