while True:
    a, d = map(int, raw_input().split())
    if a == 0 and d == 0:
        break
    alst = map(int, raw_input().split())
    dlst = map(int, raw_input().split())
    dlst.sort()
    alst.sort()
    if min(alst) < min(dlst):
        print 'Y'
    else:
	print 'N'


