'''
N, K = map(int, raw_input().split())
A = map(int, raw_input().split())
T = map(int, raw_input().split())
Ac1 = [0]*(N+1)
Ac2 = [0]*(N+1)
resp = 0

for i in range(1, N+1):
	Ac1[i] = Ac1[i-1] + A[i-1]
	Ac2[i] = Ac2[i-1]
	if T[i-1] == 1:
		Ac2[i] += A[i-1]

for L in range(N-K+1):
	R = L+K-1
	sum1 = (Ac1[R] - Ac1[L-1])
	sum2 = (Ac2[R] - Ac2[L-1])
	resp = max(resp, sum1 - sum2)

print(Ac2[N]+resp)
'''
n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
t = map(int, raw_input().split())
resp = 0
aux1 = [0]*(n+1)
aux2 = 0

for i in range(n):
	if t[i] == 1:
		resp += a[i]
		a[i] = 0

for i in range(1, n+1):
	aux1[i] = a[i-1] + aux1[i-1]

for i in range(n, k-1, -1):
	aux2 = max(aux2, aux1[i] - aux1[i-k])

print aux2 + resp
