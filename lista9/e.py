n, m = map(int, raw_input().split())
a = map(int,raw_input().split())

resp = a[0]-1
for i in xrange(1, m):
	x = a[i-1]
	if a[i] >= x:
		resp += a[i] - x
	else:
		resp += n - x + a[i]

print resp
