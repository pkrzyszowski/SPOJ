from fractions import gcd

test = int(raw_input())
while test > 0:
 test -= 1
 c, d = map(int, raw_input().split())

 def lcm(a, b):
  return abs( a * b / gcd(a, b) )

 x = lcm(c, d)

 print x
