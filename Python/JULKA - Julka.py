i = 0
while True:
 i += 1
 l = int(raw_input())
 k = int(raw_input())
 
 x = (l - k)/2
 y = l - x

 if i < 10:
  print y
  print x
  print "[and" + " " + str(10 - i) + " " + "test cases more]"
 else:
  print "FINAL"
  break
