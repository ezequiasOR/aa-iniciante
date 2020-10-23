def modpow(a, b):
	if b == 0:
		return 1
	elif b % 2 == 1:
		return (a * modpow(a, b-1)) % mod
	else:
		tmp = modpow(a, b/2)
		return (tmp * tmp) % mod


mod = 10000007

while True:
	n, k = map(int, raw_input().split())
	if n == 0:
		break
	resp = (2 * (modpow(n-1, k) + modpow(n-1, n-1)) + modpow(n, k) + modpow(n, n)) % mod
	
	print resp
