n, t = map(int, raw_input().split())

cells = raw_input().split()

i = 1
g = False

while i < n:
	i = i + int(cells[i-1])
	
	if i == t:
		g = True
		break
	elif i > t:
		break

if g:
	print 'YES'
else:
	print 'NO'
