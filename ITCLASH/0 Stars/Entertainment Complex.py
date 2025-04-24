# Entertainment Complex (0*)

# ทางหน่วยงานเอกชน IT Fun กำลังจะจัดงานสถานบันเทิงที่มีกิจกรรมหลายอย่าง เพื่อสร้างความสนุกให้กับผู้คน
# โดยที่ผู้ที่สามารถเข้าร่วมงานนั้น จะได้มีอายุตั้งแต่ 20 ปีขึ้นไป จงเขียนโปรแกรมที่สามารถรับข้อมูลจากผู้ใช้งานเป็นจำนวน N คน

# โดยผู้เล่นจะต้องกรอกอายุของตนเอง หลังจากรับข้อมูลจากผู้ใช้งานแล้ว โปรแกรมจะต้องคำนวณหาคนที่มีอายุตั้งแต่ 20 ปีขึ้นไป จำนวนกี่คน

amount = int(input())
li = []
for i in range(amount):
    people = int(input())
    if people >= 20:
        li.append(people)
print(len(li))


                            # &   Made by Parattakorn Boonprakob :P   & #
                        # !!! IF YOU USE THIS CODE, PLEASE CREDIT THE ORIGINAL !!! #
                                    # ???   Thanks for reading =Δ=   ??? #

                                            # ~ From the team, ~ #
                                         #  ^「The Procasinators」^  #