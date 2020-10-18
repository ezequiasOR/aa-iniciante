n = int(raw_input())

names = {}

for i in range(n):
	name = raw_input()
	if name not in names:
		names[name] = 0
		print 'OK'
	else:
		number = names[name] + 1
		names[name] = number
		newName = name + str(number)
		names[newName] = 0
		print newName
