def reverse(text):
  result = ""
  l = len(text) - 1
  while l >= 0:
    result += text[l]
    l -= 1
  return result

print(reverse("python"))