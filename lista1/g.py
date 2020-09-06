v_e = ['a', 'e', 'i', 'o', 'u', '1', '3', '5', '7', '9']

s = str(raw_input())

n = 0
for l in s:
	if l in v_e:
		n += 1

print(n)
