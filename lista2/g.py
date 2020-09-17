t = int(raw_input())

for i in range(t):
	n, k = map(int, raw_input().split())
	
	print (k-1)/(n-1) + k
