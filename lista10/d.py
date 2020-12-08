n, m = map(int, raw_input().split())
a = map(int, raw_input().split())

aux = 0

for _ in range(m):
	t = map(int, raw_input().split())
	if t[0] == 1:
		v, x = t[1]-1, t[2]
		a[v] = x - aux
	elif t[0] == 2:
		y = t[1]
		aux += y
	elif t[0] == 3:
		v = t[1] - 1
		print a[v] + aux
