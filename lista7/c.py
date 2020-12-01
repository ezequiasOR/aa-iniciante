def confere(a, b):
	if a[0] == '0':
		return (True, 'NO')
	if a[s-1] == '1':
		return (True, 'YES')
	elif b[s-1] == '0':
		return (True, 'NO')
	return (False, '')


n, s = map(int, raw_input().split())
a = raw_input().split()
b = raw_input().split()

con = confere(a, b)
if con[0]:
	print con[1]
else:
	aux = False
	for i in range(s-1, n):
		if a[i] == '1' and b[i] == '1':
			aux = True

	if aux:
		print 'YES'
	else:
		print 'NO'
