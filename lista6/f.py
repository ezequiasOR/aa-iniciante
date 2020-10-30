# https://www.geeksforgeeks.org/pascal-triangle/
# https://www.geeksforgeeks.org/sum-of-all-elements-up-to-nth-row-in-a-pascals-triangle/

def pascal_tri(n, m):
	r = 1
	for i in range(m):
		r *= (n - i)
		r /= (i + 1)
	return r

n, m, t = map(int, raw_input().split())

resp = 0
for i in range(4, t):
	resp += pascal_tri(n, i) * pascal_tri(m, j)

print resp
