from math import sqrt
r = int(raw_input())
k = r -1
root = int(sqrt(k))
ok = False

for x in range(1, root + 2):
	if k % x == 0:
		temp = (k/x)-x-1
		if temp > 0 and temp % 2 == 0:
			ok = True
			y = temp / 2
			print x, y
			break

if not ok:
	print 'NO'
