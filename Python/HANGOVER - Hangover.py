while True:
	c = float(raw_input())
	n = 2
	if c == 0: 
		break
	while c > 0:
		c-= 1.0/n
		n+= 1
	print n-2, 'card(s)'
