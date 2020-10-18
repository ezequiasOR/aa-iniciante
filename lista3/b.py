s = list(raw_input())
pilha = [s[0]]
count = 0

for i in range(1, len(s)):
	if len(pilha) > 0 and s[i] == pilha[-1]:
		pilha.pop()
		count += 1
	else:
		pilha.append(s[i])

if count % 2 == 1:
	print 'YES'
else:
	print 'NO'
