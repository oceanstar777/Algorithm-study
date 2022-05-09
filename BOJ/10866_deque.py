# 덱
import sys


class Deque:
    def __init__(self):
        self.lst = []
        self.front_idx = 0

    def pop_front(self):
        if len(self.lst) == 0 or len(self.lst) == self.front_idx:
            print(-1)
        else:
            print(self.lst[self.front_idx])
            self.front_idx += 1

    def pop_back(self):
        if len(self.lst) == 0 or len(self.lst) == self.front_idx:
            print(-1)
        else:
            print(self.lst.pop())

    def push_front(self, val):
        self.lst = [val]+self.lst[self.front_idx:]
        self.front_idx = 0

    def push_back(self, val):
        self.lst.append(val)

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


dq = Deque()
n = int(sys.stdin.readline())
for _ in range(n):
    command = list(sys.stdin.readline().split())

    if command[0] == 'push_front':
        dq.push_front(int(command[-1]))
    elif command[0] == 'push_back':
        dq.push_back(int(command[-1]))
    elif command[0] == 'pop_front':
        dq.pop_front()
    elif command[0] == 'pop_back':
        dq.pop_back()
    elif command[0] == 'size':
        dq.size()
    elif command[0] == 'empty':
        dq.empty()
    elif command[0] == 'front':
        dq.front()
    elif command[0] == 'back':
        dq.back()
