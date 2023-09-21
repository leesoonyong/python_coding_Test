string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"

# find함수는 해당 단어의위치출력 없으면 -1출력
for i in alphabet:
    print(string.find(i), end = ' ')