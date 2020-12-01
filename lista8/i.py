from collections import deque

n, m = map(int, raw_input().split())

visited = set()
t = [[] for i in xrange(n)]
b = [[] for i in xrange(n)]

for i in xrange(m):
	u, v = map(int,raw_input().split())
	u, v = min(u,v), max(u,v)
	u, v = u - 1, v - 1
	visited.add((u,v))
	t[v].append(u)
	t[u].append(v)

for u in xrange(n-1):
	for v in xrange(u+1,n):
		if not (u,v) in visited:
			b[u].append(v); b[v].append(u)

e = 0
if (0,n-1) in visited:
	e = b
else:
	e = t

q = deque([0])
d = [-1]*n
d[0] = 0

while q:
	v = q.popleft()
	for i in e[v]:
		if d[i] == -1:
			d[i] = d[v] + 1
			q.append(i)
		
print d[n-1]
