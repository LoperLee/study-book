import sys
n = int(sys.stdin.readline())
deque = []
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push_front":
        deque.insert(0, command[1])
    elif command[0] == "push_back":
        deque.append(command[1])
    elif command[0] == "pop_front":
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    elif command[0] == "pop_back":
        if deque:
            print(deque.pop(-1))
        else:
            print(-1)
    elif command[0] == "size":
        print(len(deque))
    elif command[0] == "empty":
        print(not deque and 1 or 0)
    elif command[0] == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif command[0] == "back":
        if deque:
            print(deque[-1])
        else:
            print(-1)