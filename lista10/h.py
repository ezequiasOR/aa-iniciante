a, b, n = map(int, raw_input().split())
resp = ''

for i in range(10):
    x = int(str(a) + str(i))
    if x % b == 0:
        resp = str(x) + ('0' * (n-1))
        break

if resp != '':
	print resp
else:
    print -1
