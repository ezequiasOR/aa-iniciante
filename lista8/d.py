# Runtime error on test 66

from sys import stdin, stdout
read, write = stdin.readline, stdout.write

p, size = [0]*2000000, [0]*2000000
v = [[] for _ in range(2000000)]

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
		p[a] = b

n, m = map(int, read().split())

#for i in range(m):
for i in range(1, n+1):
	p[i] = i

for i in range(1, m+1):
	x, y = map(int, read().split())
	size[x] += 1
	size[y] += 1
	union(x, y)

for i in range(1, n+1):
	v[find(i)].append(i)

f = 0

for i in range(1, n+1):
	l = len(v[i])
	k = l - 1
	for j in range(l):
		if size[v[i][j]] != k:
			f = 1
			break
if f == 1:
	print 'NO'
else:
	print 'YES'
