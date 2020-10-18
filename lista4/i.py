def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 


def lcm(a,b): 
    return (a*b) / gcd(a,b) 


t = int(raw_input())

for i in range(t):
	l, r = map(int, raw_input().split())
	x, y = 0, 0
	
	if 2 * l <= r:
		x, y  = l, 2*l
	else:
		x, y  = -1, -1
	
	print x, y
