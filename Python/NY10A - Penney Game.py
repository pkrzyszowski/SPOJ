t = int(raw_input())
count = 0
while t > 0:
 num = [0, 0, 0, 0, 0, 0, 0, 0]

 t -= 1
 count += 1
 print count
 a = str(raw_input())
 b = len(a)
 for i in range(b):
  if a[i:i + 3] == "TTT":
   num[0] += 1
  elif a[i:i + 3] == "TTH":
   num[1] += 1
  elif a[i:i + 3] == "THT":
   num[2] += 1
  elif a[i:i + 3] == "THH":
   num[3] += 1
  elif a[i:i + 3] == "HTT":
   num[4] += 1
  elif a[i:i + 3] == "HTH":
   num[5] += 1
  elif a[i:i + 3] == "HHT":
   num[6] += 1
  elif a[i:i + 3] == "HHH":
   num[7] += 1
 for i in range(7):
  print num[i],
 print num[7]


  
