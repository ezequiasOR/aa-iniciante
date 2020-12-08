k, r = map(int, raw_input().split())

for i in range(1,11):
    c = k*i%10
    if c == 0 or c == r:
        print i
        break
