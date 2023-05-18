str = "aaaaa aaa aaaaaaa"
list = str.split(" ")
c = []

for word in list:
    if word:
        c.append(word.capitalize())
    else:
        c.append(word)
answer = " ".join(c)
print(answer)
