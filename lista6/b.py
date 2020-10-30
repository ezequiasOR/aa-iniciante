n, k = map(int, raw_input().split())
s = raw_input()
lettersA = raw_input().split()
subs = []
sub = []

for l in s:	
	if l in lettersA:
		sub.append(l)
	else:
		subs.append(sub)
		sub = []
subs.append(sub)

resp = 0
for i in range(len(subs)):
	x = len(subs[i])
	resp += ((1 + x) * x) / 2

print resp
