t = int(raw_input())

for i in range(t):
	aux = True
	n = int(raw_input())
	
	if n % 2 == 0:
		print n/2, n/2
	else:
		j = 2
		while j * j <= n:
			if n % j == 0:
				print (n/j), (n-(n/j))
				aux = False
				break
			j += 1
		if aux:
			print 1, n-1
