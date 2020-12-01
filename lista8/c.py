from collections import deque
from sys import stdin, stdout
read, write = stdin.readline, stdout.write
g = [[] for i in xrange(300000)]
visited = [False]*300000

def dfs(i):
	pilha = deque()
	pilha.append(i)
	visited[i] = 1
	while(pilha):
		i = pilha.pop()
		for v in g[i]:
			if not(visited[v]):
				visited[v] = True
				pilha.append(v)

n = int(read())
for i in xrange(n):
	word = read().strip()
	for j in word:
		g[i].append(n+ord(j))
		g[n+ord(j)].append(i)

resp = 0
for i in xrange(n):
	if not(visited[i]):
		dfs(i)
		resp+=1
	
print(resp)
