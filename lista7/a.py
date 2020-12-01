r, c = map(int, raw_input().split())
matriz = []
aux = 0

for i in xrange(r):
	linha = list(raw_input())
	matriz.append(linha)

for i in xrange(r):
	for j in xrange(c):
		if matriz[i][j] == 'S':	
			if i and matriz[i-1][j] == '.':
				matriz[i-1][j] = 'D'
			if j and matriz[i][j-1] == '.':
				matriz[i][j-1] = 'D'
			if i < r-1 and matriz[i+1][j] == '.':
				matriz[i+1][j] = 'D'
			if j < c-1 and matriz[i][j+1] == '.':
				matriz[i][j+1] = 'D'
			
			if i and matriz[i-1][j] == 'W':
				aux = 1
				break
			if j and matriz[i][j-1] == 'W':
				aux = 1
				break
			if i < r-1 and matriz[i+1][j] == 'W':
				aux = 1
				break
			if j < c-1 and matriz[i][j+1] == 'W':
				aux = 1
				break

if aux:
	print 'No'
else:
	print 'Yes'
	for i in xrange(r):
		s = ''
		for j in xrange(c):
			s += matriz[i][j]
		print s
