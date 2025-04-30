i = 0
output = "LPH: "
item = "Item " + str(i) + ": "
# print(item)
a = int(input())
for i in range(a):
    itemname = input()
    output += str(item) + itemname
    if i == a-1:
        break
    else:
        output += " -> "
print(output)