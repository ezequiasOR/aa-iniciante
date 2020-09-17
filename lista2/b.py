n = int(raw_input())
v = map(int, raw_input().split())
m = int(raw_input())
v2 = v[:]
v2.sort()
sum1 = [0]*(n+1)
sum2 = [0]*(n+1)

for i in range(1, n+1):
	sum1[i] = sum1[i-1] + v[i-1]
	sum2[i] = sum2[i-1] + v2[i-1]
	
for l in range(m):
	t, l, r = map(int, raw_input().split())
	if t == 1:
		print sum1[r]-sum1[l-1]
	else:
		print sum2[r]-sum2[l-1]
