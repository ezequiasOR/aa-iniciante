#TLE
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

t = int(raw_input())

for j in xrange(t):
	resp = 0
	n, k = map(int, raw_input().split())
	numbers = map(int, raw_input().split())
	numbers.sort()
	
	for i in xrange(n):
		resp += comb(i, k-1) * numbers[i]
			
	print 'Case #{}: {}'.format(j+1, resp)
