import math
f = open("spoj1.txt", "r")


while True:
 g,t,a,d = map(int, f.readline().split())

 if g < 0:
  break

 teams_in_groups = g * t

 matches_in_groups = g * ((t * (t - 1)) / 2)

 teams_in_knockout2 = g * a + d

 teams_in_knockout = g * a + d


 l = math.log(teams_in_knockout, 2)
 p = int(math.ceil(l))


 if (teams_in_knockout % 2) != 0:
  teams_in_knockout = 2**p

 matches_in_knockout = teams_in_knockout - 1

 total_matches = matches_in_groups + matches_in_knockout

 add_teams = teams_in_knockout - teams_in_knockout2

 print str(g) + "*" + str(a) + "/" + str(t) + "+" + str(d) + "=" + str(total_matches) + "+" + str(add_teams)
