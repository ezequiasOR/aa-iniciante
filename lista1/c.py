def isPrime(number):
	s = int(number ** 1/2)
	
	while s > 1:
		if(number % s == 0):
			return False
		s -= 1
	return True


n = int(input())

m = 1
while True:
	k = n * m + 1
	if(not isPrime(k)):
		print(m)
		break
	m += 1
