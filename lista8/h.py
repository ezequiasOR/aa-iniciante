n = int(raw_input())
numbers = list(raw_input())
m = int(raw_input())

q = [-1] * n

for i in xrange(m):
    a, b, c = map(int,raw_input().split())
    a, b = a - 1, b - 1
    
    if q[b] == -1:
		q[b] = c
    else:
		q[b] = min(c, q[b])

if q.count(-1) > 1:
	print -1
else:
	print sum(q)+1
