import sys
import heapq

N = int(sys.stdin.readline())
Dasom = int(sys.stdin.readline())
vote_heap = []

for _ in range(N-1):
    candidate = int(sys.stdin.readline())
    heapq.heappush(vote_heap, (-candidate, candidate))

cnt = 0
while vote_heap:
    vote = heapq.heappop(vote_heap)[1]
    if vote >= Dasom:
        vote -= 1
        Dasom += 1
        cnt += 1
        heapq.heappush(vote_heap, (-vote, vote))

print(cnt)
