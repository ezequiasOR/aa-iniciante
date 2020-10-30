def modpow(a, b, mod):
	if b == 0:
		return 1
	elif b % 2 == 1:
		return (a * modpow(a, b-1, mod)) % mod
	else:
		tmp = modpow(a, b/2, mod)
		return (tmp * tmp) % mod

mod = 1000000007
def md(x):
	return ((x%mod)+mod)%mod

def invmod(a):
	return modpow(a, mod-2, mod)

fact = [1]*1000001
invfact = [1]*1000001
for i in xrange(1, 1000001):
	fact[i] = md(fact[i-1]*i)
	invfact[i] = invmod(fact[i])

def comb(a, b):
	if (b > a):
		return 0
	return md(md(fact[a]*invfact[b])*invfact[a-b])

while True:
	try:
		n, a, b, d = map(int, raw_input().split())
		c1, c2 = comb(n, a), comb(b, d)
		print md(c1*modpow(c2, a, mod))
	except EOFError:
		break
