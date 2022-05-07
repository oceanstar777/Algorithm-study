# stack
# input()으로 받으면 시간초과
# sys.stdin.readline()
import sys


class Stack:
    def __init__(self):
        self.lst = []

    def push(self, val):
        self.lst.append(val)

    def pop(self):
        try:
            print(self.lst.pop())
        except IndexError:
            print(-1)

    def size(self):
        print(len(self.lst))

    def empty(self):
        if len(self.lst) == 0:
            print(1)
        else:
            print(0)

    def top(self):
        try:
            print(self.lst[-1])
        except IndexError:
            print(-1)


s = Stack()

n = int(sys.stdin.readline())

for _ in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        s.push(int(command[-1]))
    elif command[0] == 'pop':
        s.pop()
    elif command[0] == 'size':
        s.size()
    elif command[0] == 'empty':
        s.empty()
    elif command[0] == 'top':
        s.top()
