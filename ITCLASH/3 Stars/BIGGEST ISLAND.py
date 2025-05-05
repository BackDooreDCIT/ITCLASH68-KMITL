mapsize = input().split() # mapsize
seamap = []
islandsize = 0
findland = 0
landcount = 0
biggestislandsize = 0
# print(size)
for i in range(int(mapsize[0])): # map input
    lineinp = input().replace(" ", "")
    seamap.append(lineinp)
for i in range(len(seamap)): # checking if island exist
    x = seamap[i].find("1")
    if x == -1:
        findland = 0
    else:
        findland += 1
        landcount = seamap[i].count("1")

# print(biggestislandsize)