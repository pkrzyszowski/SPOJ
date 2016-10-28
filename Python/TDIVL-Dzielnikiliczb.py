t = int(raw_input())
for x in range(t):
    a, b = map(int, raw_input().split())
    
    if a%b ==0:
        print "TAK"
    else:
        print "NIE"
