t = int(raw_input("Number of test cases:"))
for z in range(t):
     a, b = map(int, raw_input().split())
     x = int(str(a)[::-1]) + int(str(b)[::-1])
     y = int(str(x)[::-1])
     print y
