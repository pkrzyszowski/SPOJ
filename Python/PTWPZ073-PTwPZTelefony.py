t = int(raw_input())

for m in range(t):

   a = raw_input()
   
   number_list = []
   
   if len(list(a)) < 4 or len(list(a)) > 10:
       break

   for x in list(a):
       if x == 'A' or x == 'B' or x == 'C':
           number_list.append('2')
       elif x == 'D' or x == 'E' or x == 'F':
           number_list.append('3')
       elif x == 'G' or x == 'H' or x == 'I':
           number_list.append('4')
       elif x == 'J' or x == 'K' or x == 'L':
           number_list.append('5')
       elif x == 'M' or x == 'N' or x == 'O':
           number_list.append('6')
       elif x == 'P' or x == 'Q' or x == 'R' or x == 'S':
           number_list.append('7')
       elif x == 'T' or x == 'U' or x == 'V':
           number_list.append('8')
       elif x == 'W' or x == 'X' or x == 'Y' or x == 'Z':
           number_list.append('9')
       else:
           break

print "".join(number_list)

