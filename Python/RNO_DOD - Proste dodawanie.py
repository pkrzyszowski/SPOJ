test = int(raw_input())
while test > 0:
 test -= 1
 n = int(raw_input())
 d = map(int, raw_input().split())
 sum=0
 for i in range(0, n):
  sum += d[i]
 print sum
