'''
TLEEEEEEE
n, m = map(int, raw_input().split())
rows = set()
columns = set()
ans = ''

for i in range(m):
	x, y = map(int, raw_input().split())
	rows.add(x)
	columns.add(y)
	ans += str((n-len(rows)) * (n-len(columns))) + ' '

print ans.lstrip()
'''

n, m = map(int, raw_input().split())
rows = [False] * (n+1)
col = [False] * (n+1)
notUnderAttack = n*n
r = 0
c = 0
ans = ''

for i in range(m):
	x, y = map(int, raw_input().split())
	if rows[x] == False:
		rows[x] = True
		r += 1
		notUnderAttack -= (n-c)
	if col[y] == False:
		col[y] = True
		c += 1
		notUnderAttack -= (n-r)
	ans += str(notUnderAttack) + ' '

print ans.lstrip()
