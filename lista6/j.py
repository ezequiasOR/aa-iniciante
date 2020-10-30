mod = 1000000007

def md(x):
	return ((x%mod)+mod)%mod

s = raw_input()
res = 1
cnt = 1
for c in s:
	if c == 'a':
		cnt += 1
	elif c == 'b':
		res = md(res*cnt)
		cnt = 1

res = md(res*cnt)

print md(res-1)

