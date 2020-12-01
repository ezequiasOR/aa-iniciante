import sys
sys.setrecursionlimit(10**5)

memo = [-1] * 5007

def rec(i, n, s):
	if i == n:
		return 1
	if memo[i] != -1: return memo[i]
	resp = 0
	if s[i] >= '1' and s[i] <= '9':
		resp += rec(i+1, n, s)
	if i+1 < n:
		if s[i] == '1':
			resp += rec(i+2, n, s)
		if s[i] == '2' and s[i+1] >= '0' and s[i+1] <= '6':
			resp += rec(i+2, n, s)
	memo[i] = resp
	return resp

while True:
	s = list(raw_input())
	
	if s[0] == '0': break
	
	memo = [-1]*5007
	n = len(s)
	
	print rec(0, n, s)
	
