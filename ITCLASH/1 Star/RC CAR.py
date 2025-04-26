# RC CAR (1*)

# พี่เพิ่งซื้อรถบังคับมาใหม่ราคา 1 แบงค์แดง (ทอน 0.25 บาท) ด้วยราคาไม่ถึง 1 แบงค์แดง คุณภาพก็อาจตามราคานั้นแหละ พี่อยากให้น้องๆ ช่วยตรวจสอบว่า รถบังคับของพี่อยู่ในพื้นที่ที่สามารถควบคุมได้ไหม?

# โดยแทน 'o' เป็นตำแหน่งของรถบังคับ และ 'x' เป็นพื้นที่ว่างที่สามารถบังคับไปได้ รถบังคับสามารถบังคับได้แค่ 4 ทิศทางเท่านั้น:

# U: ไปข้างหน้า (ขึ้น)

# D: ไปข้างหลัง (ลง)

# L: ไปทางซ้าย

# R: ไปทางขวา

# วิธีการทำงาน:
# รับกริด 5x5 ที่ประกอบด้วยตัวอักษร 'o' (รถบังคับ) และ 'x' (พื้นที่ว่าง)

# หลังจากนั้นให้ผู้ใช้กรอกคำสั่งเพื่อย้ายตำแหน่งของรถบังคับในกริด โดยใช้คำสั่ง:

# 'U' (ขึ้น)

# 'D' (ลง)

# 'L' (ซ้าย)

# 'R' (ขวา)

# หากรถบังคับไปเกินขอบเขตกริด จะต้องแสดงข้อความว่า "Not in Area!!!" และจบการทำงานทันที

# หากผู้ใช้กรอกคำสั่ง -1 จะต้องแสดงข้อความว่า "Stop" และจบการทำงานทันที


checkforcar = ["o x x x x", "x o x x x", "x x o x x", "x x x o x", "x x x x o"]
car1 = "o x x x x"
car2 = "x o x x x"
car3 = "x x o x x"
car4 = "x x x o x"
car5 = "x x x x o"
empty = "x x x x x"
allempty = ["x x x x x", "x x x x x", "x x x x x", "x x x x x", "x x x x x"]
allmap = []
startmap = []
maxheight = ["ofb", "1", "2", "3", "4", "5", "ofb"]
curheight = "ofb"
maxwidth = ["ofb", "1", "2", "3", "4", "5", "ofb"]
curwidth = "ofb"
a = 0
result = ""
e = 0
for i in range(5):
    mapinp = input().replace(" ", "")
    mapinp = " ".join(mapinp)
    startmap.append(mapinp)
    if mapinp in checkforcar:
        curheight = maxheight[i+1]
        if mapinp == car1:
            curwidth = maxwidth[1]
        elif mapinp == car2:
            curwidth = maxwidth[2]
        elif mapinp == car3:
            curwidth = maxwidth[3]
        elif mapinp == car4:
            curwidth = maxwidth[4]
        elif mapinp == car5:
            curwidth = maxwidth[5]
# print(curheight)
# print(curwidth)
while a != -1:
    if startmap == allempty:
        result = "Not in Area!!!"
        break
    if curheight == "ofb" or curwidth == "ofb":
        allmap.append(empty)
        allmap.append(empty)
        allmap.append(empty)
        allmap.append(empty)
        allmap.append(empty)
        result = "Not in Area!!!"
        break
    cmd = input()
    if cmd == "U":
        curheight = maxheight[int(curheight)-1]
    elif cmd == "D":
        curheight = maxheight[int(curheight)+1]
    elif cmd == "L":
        curwidth = maxwidth[int(curwidth)-1]
    elif cmd == "R":
        curwidth = maxwidth[int(curwidth)+1]
    elif cmd == "-1":
        result = "Stop"
        break
    if curheight == "1":
        if curwidth == "1":
            allmap.append(car1)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
        elif curwidth == "2":
            allmap.append(car2)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
        elif curwidth == "3":
            allmap.append(car3)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
        elif curwidth == "4":
            allmap.append(car4)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
        elif curwidth == "5":
            allmap.append(car5)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
    elif curheight == "2":
        if curwidth == "1":
            allmap.append(empty)
            allmap.append(car1)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
        elif curwidth == "2":
            allmap.append(empty)
            allmap.append(car2)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
        elif curwidth == "3":
            allmap.append(empty)
            allmap.append(car3)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
        elif curwidth == "4":
            allmap.append(empty)
            allmap.append(car4)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
        elif curwidth == "5":
            allmap.append(empty)
            allmap.append(car5)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
    elif curheight == "3":
        if curwidth == "1":
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(car1)
            allmap.append(empty)
            allmap.append(empty)
        elif curwidth == "2":
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(car2)
            allmap.append(empty)
            allmap.append(empty)
        elif curwidth == "3":
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(car3)
            allmap.append(empty)
            allmap.append(empty)
        elif curwidth == "4":
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(car4)
            allmap.append(empty)
            allmap.append(empty)
        elif curwidth == "5":
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(car5)
            allmap.append(empty)
            allmap.append(empty)
    elif curheight == "4":
        if curwidth == "1":
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(car1)
            allmap.append(empty)
        elif curwidth == "2":
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(car2)
            allmap.append(empty)
        elif curwidth == "3":
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(car3)
            allmap.append(empty)
        elif curwidth == "4":
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(car4)
            allmap.append(empty)
        elif curwidth == "5":
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(car5)
            allmap.append(empty)
    elif curheight == "5":
        if curwidth == "1":
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(car1)
        elif curwidth == "2":
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(car2)
        elif curwidth == "3":
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(car3)
        elif curwidth == "4":
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(car4)
        elif curwidth == "5":
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(empty)
            allmap.append(car5)
length = len(allmap)
# print(length)
for i in range(int(length/5)):
    for a in range(5):
        print(allmap[e])
        e = e+1
    print()
print(result)

# NOTE: This is not a very efficient way of solving this problem. Instead, you can use .find() or .index()
#       to make your life easier :P


                            # &   Made by Parattakorn Boonprakob :P   & #
                        # !!! IF YOU USE THIS CODE, PLEASE CREDIT THE ORIGINAL !!! #
                                    # ???   Thanks for reading =Δ=   ??? #

                                            # ~ From the team, ~ #
                                         #  ^「The Procasinators」^  #