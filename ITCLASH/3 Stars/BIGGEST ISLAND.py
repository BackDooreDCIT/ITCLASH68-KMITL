mapsize = input().split() # mapsize
seamap = []
islandsize = 0
# print(size)
for i in range(int(mapsize[0])): # map input
    lineinp = input().replace(" ", "")
    seamap.append(lineinp)
# how 2 find islands
# 