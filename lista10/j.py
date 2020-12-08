n, m = map(int, raw_input().split())

a = m

if m <= n/2:
	a += 1
else:
	a -= 1

if a != 0:
	print a
else:
	print 1
