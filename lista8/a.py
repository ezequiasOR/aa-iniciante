xa, ya = map(int, raw_input().split())
xb, yb = map(int, raw_input().split())
xc, yc = map(int, raw_input().split())

v = (xb - xa)*(yc - yb) - (xc - xb) * (yb - ya)

if v > 0:
	print 'LEFT'
elif v < 0:
	print 'RIGHT'
else:
	print 'TOWARDS'
