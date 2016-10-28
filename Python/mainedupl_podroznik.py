t = int(raw_input("ilosc etapow: "))

kierunki = []

for m in range(t):
    a, b = raw_input().split()

    kierunki.append(b)

    c = list("".join(kierunki))

    def north():
        nswe = []
        for x in c:
            if x == "N":
               x = "|^"
            elif x == "S":
                x ="|"
            elif x == "W":
                x = "<-"
            elif x == "E":
                x = "->"
            nswe.append(x)
        print "".join(nswe)

north()

