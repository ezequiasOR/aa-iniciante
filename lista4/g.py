from math import sqrt
n = int(raw_input())
root = int(sqrt(n))
count = 0

while n % 2 != 0:
	p = n
	for i in range(2, root + 2):
		if (n % i == 0):
			p = i
			break
	n -= p
	count += 1

count += n/2
print count
