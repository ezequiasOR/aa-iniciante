n = int(raw_input())
p = [0]

for i in range(1, n+1):
	p.append(int(raw_input()))

resp = 0

for i in range(1, n+1):
	cont = 0
	x = p[i]
	while x != -1:
		x = p[x]
		cont += 1
	resp = max(resp, cont)

print resp + 1
