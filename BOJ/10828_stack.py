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
