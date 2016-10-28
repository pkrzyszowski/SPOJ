ca = '*.'*50
cp = '.*'*50

t = int(raw_input())
while t > 0:
   t -= 1
   nl, nc = map(int, raw_input().split())
   f = 0
   while f < nl:
      if f%2:
         print cp[0:nc]
      else:
         print ca[0:nc]
      f += 1
