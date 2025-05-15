array = input().split()
# print("array:", array)
array2 = []
for i in array:
    array2.append(int(i))
# print('array2:', array2)
boxsize = int(input())
output = ""
i = 0
while True:
    checkmedian = array2[0+i:boxsize+i]
    # print("before",checkmedian)
    checkmedian.sort()
    # print("after",checkmedian)
    txt = f"{int(checkmedian[1]):.1f}"
    output += txt
    i += 1
    if boxsize+i == len(array)+1:
        break
    else:
        output += " "
print(output)