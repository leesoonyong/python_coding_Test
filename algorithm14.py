import sys
#백준 10866번
num = int(sys.stdin.readline())
deque_list = []
for i in range(num):
    command = sys.stdin.readline().split()
    if(command[0] == 'push_back'):
        deque_list.append(command[1])
    elif(command[0] == 'push_front'):
        deque_list.insert(0,command[1])
    elif(command[0] == 'pop_back'):
        if(deque_list):
            print(deque_list.pop())
        else:
            print(-1)
    elif(command[0] == 'pop_front'):
        if(deque_list):
            print(deque_list.pop(0))
        else:
            print(-1)
    elif(command[0] == 'size'):
        print(len(deque_list))
    elif(command[0] == 'empty'):
        if(deque_list):
            print(0)
        else:
            print(1)
    elif(command[0] == 'front'):
        if(deque_list):
            print(deque_list[0])
        else:
            print(-1)
    elif(command[0] == 'back'):
        if(deque_list):
            print(deque_list[-1])
        else:
            print(-1)
