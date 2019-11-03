from heapq import heapify, heappop

N, X, Y = map(int, input().split())
*A, = map(lambda x: -int(x), input().split())
*B, = map(lambda x: -int(x), input().split())

all_tips = A + B
heapify(all_tips)
print(-sum([heappop(all_tips) for _ in range(N)]))
