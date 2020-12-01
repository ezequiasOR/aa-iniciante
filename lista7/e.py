n, m = map(int, raw_input().split())
resp = 0

if n > m:
	print n-m
else:
	while 0 != m - n:
		if m > n and m % 2 == 0:
			m = m / 2
			resp += 1
		else:
			if n >= m:
				resp += (n - m)
				break
			m = (m + 1) / 2
			resp += 2

	print resp
