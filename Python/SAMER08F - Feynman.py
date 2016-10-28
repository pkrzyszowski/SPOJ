f = open("square.txt", "r")

def nsquares(n):
 return n*(n+1)*(2*n+1)/6

while True:
 l = int(f.readline())
 if l == 0:
  break	

 
 print nsquares(l)


