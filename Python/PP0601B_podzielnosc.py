#test = int(raw_input())
#while test > 0:
#    test -= 1
#    n, x, y = map(int, raw_input().split())
 
#    output = []
#    for i in range(2, n):
#        if i%x == 0 and i%y != 0:
#            output.append(i)

#    output = [str(elem) for elem in output]
#    print " ".join(output)

test = int(raw_input())
for x in range(test):
    n, x, y = map(int, raw_input().split())

    output = []
    for i in range(2, n):
        if i%x == 0 and i%y != 0:
            output.append(i)

    output = [str(elem) for elem in output]
    print " ".join(output)

