def pascal_tri(n, m):
	r = 1
	for i in range(m):
		r *= (n - i)
		r /= (i + 1)
	return r

n, m = map(int, raw_input().split())

kmin = (m - n%m) * pascal_tri(n/m, 2) + n%m * pascal_tri(n/m+1, 2)
kmax = pascal_tri(n-m+1, 2)

print kmin, kmax
