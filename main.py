
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
astreoids = []
m = int(g)
count = []
distance = g
line = []
score = 0
sil = 0
silik = 0
for add in range(72):
    line.append("-")
not_crash = True
konum = 0
t = 0
komut = None
for e in range(y):
    count.append(0)
for e in range(x):
    astreoids.append([])
    for i in range(y):
        astreoids[e].append("*")
if y % 2 == 0 and y != 2:
    konum = int(y/2)
elif y == 2:
    konum = -0
else:
    konum = int((y+1)/2)
if x == 0:
    not_crash = False
    print("YOU WON!")
    for e in range(x + m):
        print()
    print(" " * (konum - 1) + "@")
    for i in line:
        print(i, end="")
    print()
    print("YOUR SCORE: ", 0)
else:
    for e in range(x):
        for i in astreoids[e]:
            print(i, end="")
        print()
    for e in range(g):
        print()
    print(" " * (konum - 1) + "@")
    for i in line:
        print(i, end="")
    print()
    komut = str(input("Choose your action:!"))  # kullanıcı emri
while not_crash:
    t += 1
    g = m
    silik = 0
    sil = 0
    for i in range(x-1,-1,-1):
        for e in astreoids[i]:
            if e == " ":
                sil += 1
        sil = sil//y
        if sil !=0:
            silik += 1
    if y == 1:
        silik = count[konum-1]
    g = g - t//5 + silik
    if not g >= 0:
        for e in astreoids:
            for i in e:
                if i == " ":
                    score += 1
                else:
                    continue
        g = 0
        print("GAME OVER")
        for e in range(x):
            for i in astreoids[e]:
                print(i, end="")
            print()
        for e in range(g):
            print()
        print(" " * (konum - 1) + "@")
        print("YOUR SCORE: ",score)
        not_crash = False
        break
    if komut.lower() == "fire":
        distance = g
        if count[konum-1] != x:
            count[konum-1] += 1
            while distance > 0:
                distance -= 1
                for i in range(t // 5):
                    print()
                for q in range(x):
                    for i in astreoids[q]:
                        print(i, end="")
                    print()
                if count[konum-1] > 1:
                    for e in range(distance-count[konum-1]):
                        print()
                else:
                    for e in range(distance):
                        print()
                print(" "*(konum-1)+"|")
                for e in range(1, g-distance):
                        print()
                print(" " * (konum - 1) + "@")
                for i in line:
                    print(i, end="")
                print()
            if count[konum-1] > 1:
                for i in range(t // 5):
                    print()
                for h in range(1,count[konum-1]):
                    astreoids[x-h][konum-1] = "|"
                    for a in range(x):
                        for i in astreoids[a]:
                            print(i, end="")
                        print()
                    for e in range(g):
                        print()
                    print(" " * (konum - 1) + "@")
                    for i in line:
                        print(i, end="")
                    print()
                    astreoids[x-h][konum-1] = " "
            astreoids[x-count[konum-1]][konum-1] = " "
            for i in range(t // 5):
                print()
            for a in range(x-silik):
                for i in astreoids[a]:
                    print(i, end="")
                print()
            for e in range(g):
                print()
            print(" " * (konum - 1) + "@")
            for i in line:
                print(i, end="")
            print()
        else:
            distance = g
            while distance > 0:
                distance -= 1
                if g != 0:
                    for i in range(t // 5):
                        print()
                    for q in range(x):
                        for i in astreoids[q]:
                            print(i, end="")
                        print()
                    for e in range(distance):
                        print()
                    print(" " * (konum - 1) + "|")
                    for e in range(1, g - distance):
                        print()
                    print(" " * (konum - 1) + "@")
                    for i in line:
                        print(i, end="")
                    print()
                else:
                    pass
                for h in range(1,count[konum-1]+1):
                    for i in range(t // 5):
                        print()
                    astreoids[x-h][konum-1] = "|"
                    for e in range(x):
                        for i in astreoids[e]:
                            print(i, end="")
                        print()
                    for e in range(m):
                        print()
                    print(" " * (konum - 1) + "@")
                    for i in line:
                        print(i, end="")
                    print()
                    astreoids[x-h][konum-1] = " "
                for i in range(t // 5):
                    print()
                for e in range(x):
                    for i in astreoids[e]:
                        print(i, end="")
                    print()
                for e in range(m):
                    print()
                print(" " * (konum - 1) + "@")
                for i in line:
                    print(i, end="")
                print()
        for e in astreoids:
            for i in e:
                if i == " ":
                    score += 1
                else:
                    continue
        if score == x * y:
            not_crash = False
            print("YOU WON!")
            for e in range(x+m):
                print()
            print(" " * (konum - 1) + "@")
            for i in line:
                print(i, end="")
            print()
            print("YOUR SCORE: ", score)
            break
    if komut.lower() == "right":
        for i in range(t//5):
            print()
        if konum == y:
            for a in range(x):
                for i in astreoids[a]:
                    print(i, end="")
                print()
            for e in range(g):
                print()
            print(" "*(konum-1)+"@")
            for i in line:
                print(i, end="")
            print()
        else:
            konum = int(konum + 1)
            for a in range(x):
                for i in astreoids[a]:
                    print(i, end="")
                print()
            for e in range(g):
                print()
            print(" "*(konum-1)+"@")
            for i in line:
                print(i, end="")
            print()
    if komut.lower() == "left":
        for i in range(t//5):
            print()
        if konum == 0:
            for e in range(x):
                for i in astreoids[e]:
                    print(i, end="")
                print()
            for e in range(g):
                print()
            print(" "*(konum-1)+"@")
            for i in line:
                print(i, end="")
            print()
            konum = 1
        else:
            konum = int(konum - 1)
            for e in range(x):
                for i in astreoids[e]:
                    print(i, end="")
                print()
            for e in range(g):
                print()
            print(" "*(konum-1)+"@")
            for i in line:
                print(i, end="")
            print()
    if komut.lower() == "exit":
        not_crash = False
        for i in range(t//5):
            print()
        for e in range(x):
            for i in astreoids[e]:
                print(i, end="")
            print()
        for e in range(g):
            print()
        print(" " * (konum - 1) + "@")
        for e in astreoids:
            for i in e:
                if i == " ":
                    score += 1
                else:
                    continue
        for i in line:
            print(i, end="")
        print()
        print("YOUR SCORE: ",score)
        break
    if komut.lower() != "left" and komut.lower() != "right" and komut.lower() != "fire" and komut != "exit":
        pass
    score = 0
    komut = str(input("Choose your action:!"))  
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
