mod = 1000000007
qb = 0
jogadas = 0

s = raw_input()

for i in xrange(len(s)-1, -1, -1):
	if s[i] == 'b':
		qb = (qb + 1) % mod
	else:
		jogadas = (jogadas + qb) % mod
		qb = (2 * qb) % mod

print jogadas
