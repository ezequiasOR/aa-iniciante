n = int(raw_input())
numbers = map(int, raw_input().split())
#soma = sum(numbers)

memo = [0]*(n+1)
memo[0] = numbers[0]

for i in range(1, n):
	memo[i] = numbers[i] + memo[i-1]
#print memo
resp = 0

for i in range(n-1):
	if memo[i] == memo[n-1] - memo[i]:
		resp += 1

print resp
