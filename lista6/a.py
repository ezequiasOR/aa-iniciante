def pascal_tri(n, m):
	r = 1
	for i in range(m):
		r *= (n - i)
		r /= (i + 1)
	return r

n = int(raw_input())
#names = []
l = [0]*26

for i in range(n):
	name = raw_input()
	#names.append(name)
	l[ord(name[0])-97] += 1

num = 0
for x in l:
	if x != 0:
		if x % 2 != 0:
			num += pascal_tri(x/2, 2)
			num += pascal_tri((x/2)+1, 2)
		else:
			num += 2 * pascal_tri(x/2, 2)

print num
