from sys import stdin, stdout
read, write = stdin.readline, stdout.write

p, size = [0]*200000, [0]*200000

def init(m):
	for i in xrange(m):
		p[i] = i
		size[i] = 1

def find(a):
	if p[a] == a:
		return a
	p[a] = find(p[a])
	return p[a]

def union(a, b):
	a, b = find(a), find(b)
	if a != b:
		if size[a] < size[b]:
			a, b = b, a
		p[b] = a
	size[a] += size[b]

m, n = map(int, read().split())

while(m != 0):
	init(m)
	edges = []
	somaMST = 0
	somaTotal = 0
	for i in xrange(n):
		u, v, w = map(int, read().split())
		edges.append((w, u, v))
	edges.sort()
	for w, u, v in edges:
		u, v = find(u), find(v)
		somaTotal += w
		if u != v:
			somaMST += w
			union(u, v)
	print(somaTotal-somaMST)
	m, n = map(int, read().split())
