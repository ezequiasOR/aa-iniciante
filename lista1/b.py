q = int(input())

for i in range(q):
	l,r,d = str(input()).split(' ')
	l = int(l)
	r = int(r)
	d = int(d)
	if (d > r or d < l):
		print(d)
	else:
		x = (int(r/d)+1)*d
		print(x)
