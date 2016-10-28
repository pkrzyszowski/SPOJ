from fractions import gcd
def nwd(a, b):
 return gcd(a, b)



test = int(raw_input())
while test > 0:
 test -= 1
 a, b = map(int, raw_input().split())

 print nwd(a, b)
