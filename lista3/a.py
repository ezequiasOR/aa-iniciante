import Queue

n, k = map(int, raw_input().split())
a = map(int, raw_input().split())

q = Queue.Queue()

if k >= n-1:
	print max(a)
else:
	for i in range(1, n):
		q.put(a[i])

	b, w = a[0], 0
	while w < k:
		top = q.get()
		if b > top:
			q.put(top)
			w += 1
		else:
			q.put(b)
			b, w = top, 1
	
	print b
