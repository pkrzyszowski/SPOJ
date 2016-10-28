t = int(raw_input())
for x in range(t):
	n, m, i ,j = raw_input().split()
	m = int(m) * int(n)
	j = int(j) + int(i)
	print 'Possible.'  if m%2 and j%2==0 else  'Impossible.'
