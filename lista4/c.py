def gcd(a,b):
    if (b == 0):
         return a
    return gcd(b, a%b)

n = int(raw_input())
a = map(int, raw_input().split())
aux = ''

for i in range(n-1):
	aux += str(a[i]) + ' '
	if gcd(a[i], a[i+1]) != 1:
		aux += '1 '

aux += str(a[-1])
print len(aux.split(' ')) - n
print aux
