'''
val[]
peso[]
qrdpacodetes
dp[101[101][101]
rec(k, n, p):
	if p >= qtdpacotes: return INF
	if k < 0: return INF
	if n == 0:
		if k != 0: return INF
		else: return 0
	if k == 0:
		if n != 0: return INF
		else: return 0
	if dp[k][n][p] != -1: return dp[k][n][p]
	
	resp = INF
	resp = min(resp, rec(k-peso[p],n-1,p)+val[p])
	resp = min(resp, rec(k, n, p+1))
	dp[k][n][p] = resp
	return dp[k][n][p]
'''

INF = 999999999

c = int(raw_input())

for _ in range(c):
	n, k = map(int, raw_input().split())
	a = map(int, raw_input().split())
	prices = [0] + a
	
	memo = [-1]*(k+1)
	memo[0] = 0
	
	for i in range(1, k+1):
		minAmount = INF
		
		for j in range(1, k+1):
			if prices[j] != -1 and i >= j:
				if memo[i-j] != -1:
					minAmount = min(minAmount, prices[j]+memo[i-j])
				else:
					minAmount = -1
		
		if minAmount != INF:
			memo[i] = minAmount
		else:
			memo[i] = -1
		
	print memo[k]
