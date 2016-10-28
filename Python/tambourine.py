from math import pi, sin
while(True):
    r, N = map(int, raw_input().split())
    if r==0 and N==0: break
    print '%.2f' % (r / sin(pi/2/N))
