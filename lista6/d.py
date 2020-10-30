from math import sqrt
t = int(raw_input())

for i in range(t):
	n, k = map(int, raw_input().split())
	
	k1 = int(sqrt(2*k))
	if k1 * (k1+1) < 2 * k:
		k1 += 1
	k2 = k1 * (k1 - 1) / 2
	
	b1 = n - 1 - k1
	b2 = n + k2 - k
	'''
	s = ''
	for j in xrange(n):
		if b1 == j or b2 == j:
			s += 'b'
		else:
			s += 'a'
	'''
	s = (b1)*'a' + 'b' + (b2-b1-1)*'a' + 'b' + (n-b2-1)*'a'
	print s
