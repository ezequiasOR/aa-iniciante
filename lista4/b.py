b = int(raw_input())

i = 1
resp = 0

while i*i <= b:
	if b % i == 0:
		resp += 1
		if i*i != b:
			resp += 1
	i += 1

print resp
