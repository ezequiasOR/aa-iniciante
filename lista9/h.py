#import sys
#sys.setrecursionlimit(10**7)

mod = 1000000007
#memo[-1]*10000007
memo1 = 1
memo2 = 0
'''
def f(idx, n, memo1, memo2):
	if idx < n:
		memo1, memo2 = (3 * memo2) % mod, (memo1 + memo2 * 2) % mod
		f(idx+1, n, memo1, memo2)
		print 'mexi aqui', memo1
	return memo1
'''
n = int(raw_input())

for i in xrange(n):
	memo1, memo2 = (3 * memo2) % mod, (memo1 + memo2 * 2) % mod
	
print memo1
