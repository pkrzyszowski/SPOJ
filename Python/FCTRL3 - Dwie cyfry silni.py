test = int(raw_input())
while test > 0:
 test -= 1
 n = int(raw_input())
 
 def silnia(a):
  if a>1:
   return  a * silnia(a-1)
  else:
   return 1

 a = silnia(n)%10
 b = silnia(n)/10
 print b, a

