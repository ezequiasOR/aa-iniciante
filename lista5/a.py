mod = 1000000007
names = []
resp = 1

n, m = map(int, raw_input().split())

for i in xrange(n):
	names.append(raw_input())

for i in xrange(m):
	letters = []
	for j in xrange(n):
		name = names[j]
		if not name[i] in letters:
			letters.append(name[i])
	
	resp = (resp * len(letters)) % mod

print resp % mod
