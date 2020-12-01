u = [[] for x in range(2)]
d = [[0,-1],[0,1],[-1,0],[1,0]]
s = []
c = 0

n = int(raw_input())
r1, c1 = map(int, raw_input().split())
r2, c2 = map(int, raw_input().split())

r1, c1 = r1-1, c1-1
r2, c2 = r2-1, c2-1


for x in range(n):
    s.append(list(raw_input()))

def bfs(x, y):
    q = [[x,y]]
    while len(q):
        i,j = q.pop()
        s[i][j] = '1'
        u[c].append([i,j])
        for a, b in d:
            k = i+a
            w = j+b
            if k < n and w < n and k >= 0 and w >= 0:
                if s[k][w] == '0':
					q.append([k, w])

bfs(r1,c1)

if s[r2][c2] == 1:
    print 0
else:
    c += 1
    resp = 5000
    bfs(r2, c2)
    
    for x1, y1 in u[0]:
        for x2, y2 in u[1]:
                resp = min(resp, (x1 - x2) ** 2 + (y1 - y2) ** 2)
    print resp
