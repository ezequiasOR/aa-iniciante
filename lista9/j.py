def lcs(s, t, m, n):
	memo = [[0]*(n+1) for i in xrange(m+1)]
	
	for i in range(1,m+1):
		for j in range(1,n+1):
			if s[i - 1] == t[j - 1]:
				memo[i][j] = memo[i - 1][j - 1] + 1
			else:
				memo[i][j] = max(memo[i-1][j], memo[i][j-1])				
	
	return memo[m][n]


def minCost(s, t):
	costS, costT = 15, 30
	m, n = len(s), len(t)
	qtyLcs = lcs(s, t, m, n)
	
	return (costS * (m - qtyLcs) + costT * (n - qtyLcs))


while True:
	s = raw_input()
	if s == '#': break
	t = raw_input()
	
	print minCost(s, t)
