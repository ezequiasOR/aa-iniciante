def f(s, n):
	if n == 0 or s == 0:
		return 0
	if memo[n][s] != -1:
		return memo[n][s]
	if weight[n-1] <= s:
		memo[n][s] = max(value[n-1] + f(s-weight[n-1], n-1), f(s, n-1))
		return memo[n][s]
	elif weight[n-1] > s:
		memo[n][s] = f(s, n-1)
		return memo[n][s] 

s, n = map(int, raw_input().split())

weight = [0]*n
value = [0]*n
memo = [[-1 for i in range(s + 1)] for j in range(n + 1)] 

for i in range(n):
	p, v = map(int, raw_input().split())
	weight[i] = p
	value[i] = v

print f(s, n)
