import sys

from collections import deque



def vps_check(string):

    stack = deque()

    for s in string:

        if s == '(':

            stack.append(s)

        elif s == ')':

            try:

                s_pop = stack.pop()

            except IndexError:

                return False

            else:

                if s_pop != '(':

                    return False

    if stack:

        return False

    return True





t = int(sys.stdin.readline())



for _ in range(t):

    string = sys.stdin.readline().rstrip()

    if vps_check(string):

        print('YES')

    else:

        print('NO')
