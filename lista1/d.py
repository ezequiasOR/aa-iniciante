def num_operation(a, b, n):
	if(a > n or b > n):
		return 0
	return 1 + num_operation(max(a, b), a + b, n)


t = int(raw_input())

for i in range(t):
	a, b, n = str(raw_input()).split(' ')
	a = int(a)
	b = int(b)
	n = int(n)
	
	print(num_operation(a, b, n))
