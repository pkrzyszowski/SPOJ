from fractions import gcd
t = int(raw_input())

while t > 0:
 t -= 1 
 a, b = map(int, raw_input().split())
 g = gcd(a, b)

 print a/g, b/g


