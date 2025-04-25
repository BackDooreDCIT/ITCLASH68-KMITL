minpos = 1
maxpos = 25
curpos = 0
startpos = []
allmap = []
result = ""
checkforcar = ["o x x x x", "x o x x x", "x x o x x", "x x x o x", "x x x x o"]
car1 = "o x x x x"
car2 = "x o x x x"
car3 = "x x o x x"
car4 = "x x x o x"
car5 = "x x x x o"
empty = "x x x x x"
lastcmd = 1
laststrcmd = ""
lastval = 0
e = 0
for i in range(5):
    agar = input()
    startpos.append(agar)
    if agar == car1:
        curpos = 1 + (5 * i)
    elif agar == car2:
        curpos = 2 + (5 * i)
    elif agar == car3:
        curpos = 3 + (5 * i)
    elif agar == car4:
        curpos = 4 + (5 * i)
    elif agar == car5:
        curpos = 5 + (5 * i)
# print(curpos)
# print(pos0)
while curpos >= minpos and curpos <= maxpos:
    lastval = lastval
    cmd = input()
    if lastcmd == 0:
        allmap.append(empty)
        allmap.append(empty)
        allmap.append(empty)
        allmap.append(empty)
        allmap.append(empty)
        break
    if cmd == "U":
        curpos = curpos-5
    elif cmd == "D":
        curpos = curpos+5
    elif cmd == "L":
        curpos = curpos-1
    elif cmd == "R":
        curpos = curpos+1
    elif cmd == "-1":
        result = "Stop"
        break
    if curpos > 0 and curpos <= 5:
        if curpos == 1:
            if cmd == "L":
                allmap.append(checkforcar[0])
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                result = "Not in Area!!!"
                lastcmd = 0
            elif cmd == "U":
                allmap.append(checkforcar[curpos-1])
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                result = "Not in Area!!!"
                lastcmd = 0
        elif curpos == 5:
            if cmd == "R":
                allmap.append(checkforcar[4])
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                result = "Not in Area!!!"
                lastcmd = 0
            elif cmd == "U":
                allmap.append(checkforcar[curpos-1])
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                result = "Not in Area!!!"
                lastcmd = 0
        else:
            allmap.append(checkforcar[curpos-1])
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
    elif curpos > 5 and curpos <= 10:
        if curpos == 6:
            print('secondline')
            if cmd == "L":
                print('gethere')
                allmap.append(empty)
                allmap.append(checkforcar[0])
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                result = "Not in Area!!!"
                lastcmd = 0
        if curpos == 10:
            if cmd == "R":
                allmap.append(empty)
                allmap.append(checkforcar[4])
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                result = "Not in Area!!!"
                lastcmd = 0
        else:
            allmap.append(empty)
            allmap.append(checkforcar[curpos-6])
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
    elif curpos > 10 and curpos <= 15:
        if curpos == 11:
            if cmd == "L":
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(checkforcar[0])
                allmap.append(empty)
                allmap.append(empty)
                result = "Not in Area!!!"
                lastcmd = 0
        if curpos == 15:
            if cmd == "R":
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(checkforcar[4])
                allmap.append(empty)
                allmap.append(empty)
                result = "Not in Area!!!"
                lastcmd = 0
        else:
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(checkforcar[curpos-11])
            allmap.append(empty)
            allmap.append(empty)
    elif curpos > 15 and curpos <= 20:
        if curpos == 16:
            if cmd == "L":
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(checkforcar[0])
                allmap.append(empty)
                result = "Not in Area!!!"
                lastcmd = 0
        if curpos == 20:
            if cmd == "R":
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(checkforcar[4])
                allmap.append(empty)
                result = "Not in Area!!!"
                lastcmd = 0
        else:
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(checkforcar[curpos-16])
            allmap.append(empty)
    elif curpos > 20 and curpos <= 25:
        if curpos == 21:
            if cmd == "D":
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(checkforcar[curpos-21])
                result = "Not in Area!!!"
                lastcmd = 0
            elif cmd == "L":
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(checkforcar[0])
                result = "Not in Area!!!"
                lastcmd = 0
        if curpos == 25:
            if cmd == "D":
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(checkforcar[curpos-21])
                result = "Not in Area!!!"
                lastcmd = 0
            elif cmd == "R":
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(empty)
                allmap.append(checkforcar[4])
                result = "Not in Area!!!"
                lastcmd = 0
        else:
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(checkforcar[curpos-21])
        laststrcmd = cmd
        lastval = curpos
length = len(allmap)
print(length)
for i in range(int(length/5)):
    for a in range(5):
        print(allmap[e])
        e = e+1
    print()
print(result)