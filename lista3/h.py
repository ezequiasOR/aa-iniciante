n = int(raw_input())

a = map(int, raw_input().split())
b = map(int, raw_input().split())

auxA = [0] * max(a)
auxB = [0] * max(b)
count = 0
aux = -1

for i in range(n):
	auxB[b[i]-1] = i

for i in range(n):
	auxA[i] = auxB[a[i]-1]
'''
for i in range(n):
	auxA[a[i]-1] = i

print auxA
print auxB

for i in range(n):
	if auxA[i] < auxB[i]:
		
for i in range(n):
	print auxA[i], auxB[i]
	if auxA[i] > auxB[i]:
		count += 1
'''
for i in range(n):
	#print auxA[i], auxB[i]
	if auxA[i] <= aux:
		count += 1
	else:
		aux = auxA[i]

print count
