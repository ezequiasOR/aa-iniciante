def numberN(n):
	return (n * (n + 1)) / 2


n, k = str(raw_input()).split()
n, k = int(n), int(k)

ids = str(raw_input()).split()

for i in range(n, -1, -1):
	j = numberN(i)
	if(j < k):
		print(ids[k-j-1])
		break
