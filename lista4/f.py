resp = [0]*100001

n = int(raw_input())
count = 1
for i in range(2, n+1):
	if resp[i] == 0:
		for j in range(i, n+1, i):
			resp[j] = count
		count += 1

for i in range(2, n+1):
	print resp[i],
