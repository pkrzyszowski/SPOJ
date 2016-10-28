from fractions import gcd
for _ in xrange(input()):
	A, B = map(int, raw_input().split())
	g = gcd(A, B)
	print B/g, A/g
