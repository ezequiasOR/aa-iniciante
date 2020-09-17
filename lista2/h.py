n = int(raw_input())
a = map(int, raw_input().split())

a.sort()

c = 0
j = 0
for i in range(n):
	while j < n and a[j] - a[i] <= 5:
		j += 1
		if j - i > c:
			c = j - i

print c
