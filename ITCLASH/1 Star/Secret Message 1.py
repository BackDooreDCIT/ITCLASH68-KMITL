# Secret Message 1

# ทางผู้จัดงานแข่ง IT Cast (ชื่องานคล้ายๆ กัน) โดยผู้จัดงานแข่งขันต้องการส่งข้อความลับที่มีแต่เพียงแต่ผู้ที่มีไหวพริบจะสามารถถอดรหัสได้ ให้คุณในฐานะผู้เข้าร่วมการแข่งขัน IT Cast ทำการเขียนโปรแกรมถอดรหัสข้อความลับที่ผู้จัดงานแข่งขันส่งมา

# ข้อความที่ผู้สมัครได้จะประกอบไปด้วยตัวเลขจำนวนเต็ม ตั้งแต่ 1 - 26 โดยที่อักษรแต่ละตัวจะสามารถแทนได้ด้วยตัวเลขของลำดับของตัวอักษรในภาษาอังกฤษ เช่น A=1, B=2, C=3, ..., Z=26 และอาจจะมีเว้นวรรคเข้ามาในข้อความ

# หากเจอตัวเลข 0 จะถือว่าเป็นการเว้นวรรค
# หากเป็นเครื่องหมาย / จะถือว่าเป็นการขึ้นบรรทัดใหม่
# โปรแกรมจะต้องแสดงผลของข้อความลับที่ถอดรหัสได้ออกมาที่หน้าจอ

import string
alphabets = list(string.ascii_uppercase)
# print(alphabets)
builder = input().split()
# print(builder)
output = ""
# print(len(builder))
# print(alphabets[0])
for i in range(len(builder)):
    if builder[i] > "0" and builder[i] != "/":
        output += alphabets[int(builder[i])-1]
    else:
        if builder[i] == "0":
            output += " "
        elif builder[i] == "/":
            output += "\n"
print(output)


                            # &   Made by Parattakorn Boonprakob :P   & #
                        # !!! IF YOU USE THIS CODE, PLEASE CREDIT THE ORIGINAL !!! #
                                    # ???   Thanks for reading =Δ=   ??? #

                                            # ~ From the team, ~ #
                                         #  ^「The Procasinators」^  #