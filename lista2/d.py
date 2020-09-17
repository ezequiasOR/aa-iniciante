'''
def substring(s):
	nL = 0
	l1 = []
	
	for i in range(len(s)):
		n = 0
		l2 = []
		if s[i] == '1':
			for j in range(i, len(s)):
				if s[j] == '1':
					n += 1
					l2.append(j)
				else:
					break
		if n > nL:
			nL = n
			l1 = l2
	return l1

t = int(raw_input())

for i in range(t):
	s = str(raw_input())
	c = 0
	a = list(s)
	k = []
	for j in range(len(s)+1):
		if j % 2 == 0:
			k = substring(a)
			c += len(k)
		else:
			k = substring(a)
	print c
'''

t = int(raw_input())

for i in range(t):
	s = str(raw_input())
	
	a = []
	r = 0
	for j in range(len(s)):
		if r > 0 and s[j] == '0':
			a.append(r)
			r = 0
		elif s[j] == '1':
			r += 1
	
	if r > 0:
		a.append(r)
	a.sort(key=int, reverse=True)
	
	resp = 0
	for k in range(0, len(a), 2):
		resp += a[k]
	
	print resp
