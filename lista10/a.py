o, letters = 97, 26

name = raw_input()
resp = 0

for l in name:
	resp += min(abs(o - ord(l)), letters - abs(o - ord(l)))
	o = ord(l)

print resp
