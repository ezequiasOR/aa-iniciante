def modpow(a, b):
	if b == 0:
		return 1
	elif b % 2 == 1:
		return (a * modpow(a, b-1)) % mod
	else:
		tmp = modpow(a, b/2)
		return (tmp * tmp) % mod


mod = 10
t = int(raw_input())

for i in range(t):
	a, b = map(int, raw_input().split())
	print str(modpow(a, b))[-1]
