n = int(raw_input())
a = raw_input().split()

e = []
s = ''

for i in range(len(a)-1, -1, -1):
	if a[i] not in e:
		e.append(a[i])
		s = ' ' + a[i] + s

print len(e)
print s.lstrip()
