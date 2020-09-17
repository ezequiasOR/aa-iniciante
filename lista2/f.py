n = int(raw_input())
t = map(int, raw_input().split())
aux = []

x = 1
for i in range(1, n):
	if t[i-1]==t[i]:
		x += 1
	else:
		aux.append(x)
		x = 1

aux.append(x)
resp = 0
for i in range(1, len(aux)):
	resp = max(resp, min(aux[i-1], aux[i]))

print resp * 2
