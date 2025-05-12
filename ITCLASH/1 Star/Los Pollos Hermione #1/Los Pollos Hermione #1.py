output = "LPH: "
i = 0
class bill:
    def __init__(self, item):
        self.item = item

    def curitem(self):
        output += "Item " + str(i) + ": "
        output += self.item
        output += " -> "
loopamount = int(input())
for i in range(loopamount):
    myitem = input()
    totaled = bill(myitem)
    totaled.curitem
print(output)