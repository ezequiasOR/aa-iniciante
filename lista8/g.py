import heapq 
n, m = map(int, raw_input().split())

e = {i: [] for i in range(1, n+1)}
p = [0]*(n+1)
d = [-1]*(n+1)
visited = [False]*(n+1)

for i in range(m):
	u, v, s = map(int, raw_input().split())
	e[u].append((v, s))
	e[v].append((u, s))
 
v = [(0, 1, 0)]
while len(v) > 0:
	a, b, w = heapq.heappop(v)
	if visited[b]:
		continue
	p[b] = w
	d[b] = a
	visited[b] = True

	if b == n:
		break
	for i, j in e[b]:
		if not visited[i]:
			heapq.heappush(v, (a + j, i, b))
 
if not visited[n]:
	print -1
else:
	way = []
	c = n
	while c != 0:
		way.append(c)
		c = p[c]
	s = ''
	for i in range(len(way)-1, -1, -1):
		s += str(way[i]) + ' '
	print s.strip()
