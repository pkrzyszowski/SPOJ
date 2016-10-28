test = int(raw_input())
while test > 0:
 test -= 1
 n = int(raw_input())
 men = sorted(map(int, raw_input().split()))
 women = sorted(map(int, raw_input().split()))
 sum = 0
 for i in range(0, n):
  sum += men[i]*women[i]
 print sum 
