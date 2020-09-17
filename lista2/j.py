t = int(raw_input())

for i in range(t):
	aux = [0]
	resp = 0
	s = str(raw_input())
	
	for i in range(len(s)):
		if s[i] == 'R':
			aux.append(i+1)
	
	aux.append(len(s)+1)
	#print aux
	for i in range(len(aux)-1):
		resp = max(resp, aux[i+1]-aux[i])
	
	print resp
