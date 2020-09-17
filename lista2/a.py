n = int(raw_input())
x = map(int, raw_input().split())

mi = 0
ma = 0
mi1 = 0
mi2 = 0
for i in range(n):
	ma = abs(max(x[-1] - x[i], x[i] - x[0]))
	
	if i + 1 < len(x):
		mi1 = abs(x[i+1] - x[i])
	if i - 1 >= 0:
		mi2 = abs(x[i] - x[i-1])
	if mi1 == 0 or mi2 == 0:
		mi = max(mi1, mi2)
	else:
		mi = min(mi1, mi2)
	
	print mi, ma
