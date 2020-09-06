name = str(raw_input())

letters = []

for letter in name:
	if(letter not in letters):
		letters.append(letter)

if(len(letters) % 2 == 0):
	print('CHAT WITH HER!')
else:
	print('IGNORE HIM!')
