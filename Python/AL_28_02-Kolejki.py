t = int(raw_input())

for v in range(t):
    a, b, c = map(int, raw_input().split())
    d, e, f = map(int, raw_input().split())

    x = (a*d+d)
    y = (b*e)
    z = (c*f)
    
    if y >= x:
        t = (y - x) + e
    else:
        t = e
    
    if z >= (x + t):
        u = z - (x+t) + f
    else:
        u = f

     

    minutes = x + t + u
    print minutes



