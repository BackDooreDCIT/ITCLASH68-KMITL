# i = 0
output = "LPH: "

# print(item)
a = int(input())
for i in range(a):
    item = "Item " + str(i+1) + ": "
    itemname = input()
    output += str(item) + itemname
    if i == a-1:
        break
    else:
        output += " -> "
print(output)

