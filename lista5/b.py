def modpow(a, b):
	if b == 0:
		return 1
	elif b % 2 == 1:
		return (a * modpow(a, b-1)) % mod
	else:
		tmp = modpow(a, b/2)
		return (tmp * tmp) % mod


mod = 1000000007

n = int(raw_input())

a = modpow(3, 3*n)
b = modpow(7, n)
print (((a - b) % mod) % mod + mod) % mod
