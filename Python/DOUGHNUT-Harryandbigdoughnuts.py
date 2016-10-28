t = int(raw_input())

for x in range(t):
    
    a, b, c = map(int, raw_input().split())
    
    if (a * c) <= b:
        print "yes"
    else:
        print "no"
        
