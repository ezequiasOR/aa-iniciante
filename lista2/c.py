t = int(raw_input())

for i in range(t):
	n = int(raw_input())
	s = str(raw_input())
	out = ''
	#for i in range(n):
	for i in range(0, 2*n-1, 2):
		out += s[i]
	
	print out
