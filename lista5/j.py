a, b = map(int, raw_input().split())

resp = 0

if a < b:
	print 0
elif a == b:
	print 'infinity'
else:
	k = a-b
	i = 1
	while i*i <= k:
		if k % i == 0 and i > b:
			resp += 1
		if k % i == 0 and k/i > b and k/i != i:
			resp += 1
		i += 1
	print resp
