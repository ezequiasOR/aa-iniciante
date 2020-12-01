memo = [[0]*(2007) for i in xrange(2007)]

n, m = map(int, raw_input().split())
n, m = n-1, m-1
p = map(int, raw_input().split())

s1 = raw_input()
s2 = raw_input()

for i in range(n, -1, -1):
	for j in range(m, -1, -1):
		if i == n or j == m:
			memo[i][j] = 0
		resp = 0
		resp = max(resp, memo[i+1][j])
		resp = max(resp, memo[i][j+1])
		if s1[i] == s2[j]:
			resp = max(resp, memo[i+1][j+1] + p[ord(s1[i])-97])
		memo[i][j] = resp

print memo[0][0]
