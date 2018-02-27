import re
kata1 = "1a2b3c4d5"
search = re.search(r'1a', kata1, re.I|re.M)
print(search.group())

rep = re.sub(r'\D', "", kata1, re.I | re.M)
print(rep)
rep1 = re.sub(r'\d', "", kata1, re.I | re.M)
print(rep1)