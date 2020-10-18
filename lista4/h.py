'''
def gcd(a,b):
    if (b == 0):
         return a
    return gcd(b, a%b)
'''

n, k = map(int, raw_input().split())
# p = range(1, n+1)
out = ''

if n == k:
	print '-1'
elif n-1 == k:
	for i in xrange(1, n):
		out += str(i) + ' '
	print out + str(n)
else:
	out += str(k+2) + ' '
	for i in xrange(2, n):
		if i <= k+1:
			out += str(i) + ' '
		else: 
			out += str(i+1) + ' '
	print out + '1'
