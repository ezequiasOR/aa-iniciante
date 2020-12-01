# erro

import sys
sys.setrecursionlimit(10**5)
from collections import deque

n, m = map(int, raw_input().split())
s = []
pre = {}
l = [[]]*107
aux = [0]*107

def bfs(x, y):
	resp = 0
	for i in range(1, 101):
		fila = deque([])
		aux = [0]*107
		aux[x] = 1
		for t in range(len(l[x])):
			if l[x][t][1] == i and aux[l[x][t][0]]==0:
				fila.append(l[x][t]);
				aux[l[x][t][0]] = 1
		
		while fila:
			value = fila.popleft()
			if value[0]==y:
				resp += 1
			for t in range(len(l[value[0]])):
				if n not in pre and n <= b:
					aux[l[value[0]][t][0]] = 1
					fila.append(l[value[0][t]])

		

for i in range(m):
	a, b, c = map(int, raw_input().split())
	if c not in s:
		s.append(c)
	pre[b] = c
	l[a].append((b, c))
	pre[a] = c
	l[b].append((a, c))
	
q = int(raw_input())

for i in range(q):
	u, v = map(int, raw_input().split())
	resp = 0
	bfs(u, v)
	print resp

'''
def dfs(u, v, j):
	aux[u] = True
	if u == v:
		return True
	for i in range(len(l[u])):
		a = l[u][i][0]
		b = l[u][i][1]
		if not aux[a] and b == j:
			if dfs(a, v, j):
				return True
	return False


n, m = map(int, raw_input().split())
l = [[]]*107
aux = [False]*107

for i in range(1, m+1):
	a, b, c = map(int, raw_input().split())
	l[a].append((b, c))
	l[b].append((a, c))

q = int(raw_input())

for i in range(1, q+1):
	resp = 0
	u, v = map(int, raw_input().split())
	
	for j in (1, 101):
		aux = [False]*107
		if dfs(u, v, i):
			resp += 1
	print resp
'''
