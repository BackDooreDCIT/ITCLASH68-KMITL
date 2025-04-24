
# 7-segment display

# ให้น้องเขียนโปรแกรมเพื่อถอดรหัสจากข้อมูลไฟ 7 ดวงในรูปแบบของ 7-segment display
# ซึ่งจะแสดงเลข 0–9 ได้โดยการเปิดหรือปิดไฟตามตำแหน่ง segment
# "1" หรือ "0" แสดงว่าเปิดหรือปิดไฟในแต่ละตำแหน่ง

# โดยโปรแกรมจะรับข้อมูลทั้งหมด 8 บรรทัด
# แต่ละบรรทัดเป็นเลข 7 ตัว แสดงไฟของตัวเลข 1 หลัก
# น้องๆจะต้องแปลง segment เหล่านั้นให้เป็นตัวเลขจริง ๆ แล้วพิมพ์ผลลัพธ์ทั้งหมดออกมาเป็นสตริงตัวเลข

no0 = "1111110"
no1 = "0110000"
no2 = "1101101"
no3 = "1111001"
no4 = "0110011"
no5 = "1011011"
no6 = "1011111"
no7 = "1110000"
no8 = "1111111"
no9 = "1111011"
metalpipe = ""
for i in range(8):
    america = input().replace(" ", "")
    if america == no0:
        metalpipe = metalpipe+"0"
    elif america == no1:
        metalpipe = metalpipe+"1"
    elif america == no2:
        metalpipe = metalpipe+"2"
    elif america == no3:
        metalpipe = metalpipe+"3"
    elif america == no4:
        metalpipe = metalpipe+"4"
    elif america == no5:
        metalpipe = metalpipe+"5"
    elif america == no6:
        metalpipe = metalpipe+"6"
    elif america == no7:
        metalpipe = metalpipe+"7"
    elif america == no8:
        metalpipe = metalpipe+"8"
    elif america == no9:
        metalpipe = metalpipe+"9"
print(metalpipe)


                            # &   Made by Parattakorn Boonprakob :P   & #
                        # !!! IF YOU USE THIS CODE, PLEASE CREDIT THE ORIGINAL !!! #
                                    # ???   Thanks for reading =Δ=   ??? #

                                            # ~ From the team, ~ #
                                         #  ^「The Procasinators」^  #