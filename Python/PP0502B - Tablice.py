test = int(raw_input())
while test > 0:
 test -= 1
 n = int(raw_input())
 x = map(int, raw_input().split())
 list = []
 for i in x:
  list.append(i)

 list.reverse()
 print list

