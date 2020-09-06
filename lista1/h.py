t = int(raw_input())

for i in range(t):
	freqp = [0]*26
	p = str(raw_input())
	h = str(raw_input())
	
	for j in p:
		freqp[ord(j) - 97] += 1
	
	resp = 'NO'
	
	for j in range(len(h)):
		freqh = [0]*26
		
		if(j + len(p) <= len(h)):
			for l in range(j, j + len(p)):
				freqh[ord(h[l]) - 97] += 1
		
		if freqp == freqh:
			resp = 'YES'

	print(resp)
