n1 = int(raw_input())
n2 = int(raw_input())

def add_number(a, b):
    if a>200 or b>200:
        print "Enter numbers less than 200"
    else:
        return a + b

print add_number(n1, n2)

