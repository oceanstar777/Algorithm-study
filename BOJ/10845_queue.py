# 큐
# try except?
import sys


class Queue:
    def __init__(self):
        self.lst = []
        self.front_idx = 0

    def push(self, val):
        self.lst.append(val)

    def pop(self):
        if len(self.lst) == 0 or len(self.lst) == self.front_idx:
            print(-1)
        else:
            print(self.lst[self.front_idx])
            self.front_idx += 1

    def size(self):
        if len(self.lst) == 0 or len(self.lst) == self.front_idx:
            print(0)
        else:
            print(len(self.lst[self.front_idx:]))

    def empty(self):
        if len(self.lst) == 0 or len(self.lst) == self.front_idx:
            print(1)
        else:
            print(0)

    def front(self):
        if len(self.lst) == 0 or len(self.lst) == self.front_idx:
            print(-1)
        else:
            print(self.lst[self.front_idx])

    def back(self):
        if len(self.lst) == 0 or len(self.lst) == self.front_idx:
            print(-1)
        else:
            print(self.lst[-1])


q = Queue()
n = int(sys.stdin.readline())

for _ in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        q.push(int(command[-1]))
    elif command[0] == 'pop':
        q.pop()
    elif command[0] == 'size':
        q.size()
    elif command[0] == 'empty':
        q.empty()
    elif command[0] == 'front':
        q.front()
    elif command[0] == 'back':
        q.back()
