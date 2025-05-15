obby = list(input())
curpos = 0
jumps = 0
curobject = ""
result = ""
deathpos = -1
finishline = len(obby)-1
for i in range(len(obby)):
    curobject = obby[curpos]
    if curobject == " ":
        result = "IMPOSSIBLE"
        deathpos = curpos-1
        jumps = finishline - deathpos
        break
    elif curobject == "|":
        result = "POSSIBLE"
        break
    else:
        if curobject == "^":
            curpos += 1
            jumps += 1
        if curobject == "o":
            curpos += 1
            jumps += 1
        if curobject == "O":
            print("enter O")
            if finishline - curpos >= 3:
                if obby[curpos+3] == "|" or obby[curpos+3] == "o" or obby[curpos+3] == "O":
                    curpos += 3
                    jumps += 3
                    print("enter3.1")
                elif obby[curpos+1] == " " and obby[curpos+2] == " " and obby[curpos+3] == " ":
                    curpos += 3
                    jumps += 3
                    print("enter3.2")
                elif obby[curpos+2] == "|" or obby[curpos+2] == "o" or obby[curpos+2] == "O":
                    curpos += 2
                    jumps += 2
                    print("enter3.3")
                elif obby[curpos+1] == "|" or obby[curpos+1] == "o" or obby[curpos+1] == "O":
                    curpos += 1
                    jumps += 1
                    print("enter3.4")
            elif finishline - curpos < 3:
                if finishline - curpos == 2:
                    if obby[curpos+1] == " " and obby[curpos+2] == " ":
                        curpos += 2
                        jumps += 2
                    if obby[curpos+2] == "|" or obby[curpos+2] == "o" or obby[curpos+2] == "O":
                        curpos += 2
                        jumps += 2
                if finishline - curpos == 1:
                    if obby[curpos+1] == " ":
                        curpos += 1
                        jumps += 1
                    if obby[curpos+1] == "|" or obby[curpos+1] == "o" or obby[curpos+1] == "O":
                        curpos += 1
                        jumps += 1
print(result)
print(jumps)