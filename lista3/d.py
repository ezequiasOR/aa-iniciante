q = int(raw_input())

d = {}
count = 0

for i in range(q):
	old, new = map(str, raw_input().split())
	if old not in d:
		d[new] = old
		count += 1
	else:
		d[new] = d[old]
		del d[old]

print count
for newOutput, oldOutput in d.items():
	print oldOutput, newOutput
