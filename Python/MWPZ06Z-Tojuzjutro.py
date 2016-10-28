t = int(raw_input())

for x in range(t):
    a, b = map(int, raw_input().split())
    
    if 100%a != 0:
        break

    if b%a == 0:
        print "TAK"
    else:
        print "NIE"
