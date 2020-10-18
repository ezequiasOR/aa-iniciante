from sys import stdin, stdout
read, write = stdin.readline, stdout.write
prime = [1] * 1000001

def sq_root(x):
	root = int(x ** 0.5) - 1
	if root * root == x:
		return root
	root += 1
	if root * root == x:
		return root
	root += 1
	if root * root == x:
		return root
	return -1

prime[0] = prime[1] = 0
for i in xrange(2, 1001):
	if prime[i] == 1:
		for j in xrange(i*i, 1000001, i):
			prime[j] = 0

n = int(raw_input())
numbers = map(int, read().split())
for i in numbers:
	root = sq_root(i)
	if root != -1 and prime[root]:
		write('YES\n')
	else:
		write('NO\n')
