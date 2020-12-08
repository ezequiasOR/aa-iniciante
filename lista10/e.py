n = int(raw_input())
a = map(int, raw_input().split())
lista = list(a)
aS = sorted(lista)

l, r = 0, n-1

while l < n and a[l] == aS[l]:
	l += 1

while r >= 0 and a[r] == aS[r]:
	r -= 1

if l == n or r == -1:
	l = r = 0

resp = (l+1, r+1)

while l < r:
	if a[l] < a[l+1]:
		print 'no'
		break
	l += 1
else:
	print 'yes'
	print str(resp[0]) + ' ' + str(resp[1])
