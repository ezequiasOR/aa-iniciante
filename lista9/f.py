n, m = map(int, raw_input().split())
a = map(int, raw_input().split())

conj = set()
memo = []

for i in xrange(1, n+1):
	#print a
	#print a[-i]
	x = a[-i]
	conj.add(x)			# a[-i] -> percorrendo a ao contrario
	memo.append(len(conj))

for i in xrange(m):
	l = int(raw_input())
	print memo[n-l]
