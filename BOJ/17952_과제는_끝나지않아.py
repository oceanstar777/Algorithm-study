import sys
from collections import deque
n = int(sys.stdin.readline())

assignment = [
    list(map(int,sys.stdin.readline().split()))
    for _ in range(n)
]

score = 0

working_stk = deque()

for idx in range(n):
    if(assignment[idx][0] == 1):
        working_stk.append(assignment[idx][1:])
        working_stk[-1][-1]-=1
        if (working_stk[-1][-1]==0):
            score+=working_stk[-1][0]
            working_stk.pop()
    else:
        if(working_stk):
            working_stk[-1][-1]-=1
            if (working_stk[-1][-1]==0):
                score+=working_stk[-1][0]
                working_stk.pop()

print(score)
