import sys
n = int(sys.stdin.readline())

for i in range(n):
    str = sys.stdin.readline().rstrip()
    words = list(str.split())
    revers_name = []

    for word in words:
        revers_name.append(word[::-1])
        
    print(' '.join(revers_name))