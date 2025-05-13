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
        elif curobject == "0":
            if finishline - curpos >= 3:
                if (obby[curpos+1] == " " and obby[curpos+2] == " " and obby[curpos+3] == " ") or obby[curpos+3] == "|" or obby[curpos+3] == "o" or obby[curpos+3] == "0":
                    curpos += 3
                    jumps += 3
                elif obby[curpos+2] == "|" or obby[curpos+2] == "o" or obby[curpos+2] == "0":
                    curpos += 2
                    jumps += 2
                elif obby[curpos+1] == "|" or obby[curpos+1] == "o" or obby[curpos+1] == "0":
                    curpos += 1
                    jumps += 1
            elif finishline - curpos < 3:
                if finishline - curpos == 2:
                    if obby[curpos+2] == "|" or obby[curpos+2] == "o" or obby[curpos+2] == "0":
                        curpos += 2
                        jumps += 2
                if finishline - curpos == 1:
                    if obby[curpos+1] == "|" or obby[curpos+1] == "o" or obby[curpos+1] == "0":
                        curpos += 1
                        jumps += 1
print(result)
print(jumps)