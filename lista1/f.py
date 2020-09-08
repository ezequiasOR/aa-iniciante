t = int(raw_input())

for i in range(t):
	s = str(raw_input())
	
	ans = [False]*26
	
	j = 0
	while j < len(s):
		k = j
		while k + 1 < len(s) and s[k + 1] == s[j]:
			k += 1
		if((k - j) % 2 == 0):
			ans[ord(s[j]) - 97] = True
		
		j = k
		
		j += 1
	
	r = ''
	for j in range(26):
		if ans[j]:
			r += chr(j+97)
	
	print r
