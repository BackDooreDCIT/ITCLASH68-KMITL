# เวลาของเธอกับเขาแต่ระหว่างเรามันไม่เท่ากัน 1 (1*)

# ในโลกแห่งหนึ่งซึ่งเวลานั้นบิดเบี้ยว โดยมีชายหนุ่มชื่อ "สมชาย" ที่เดินหน้าไปในแต่ละวันตามปกติ และส่วนหญิงสาวชื่อ "คชสาร" กลับเดินถอยหลังในแต่ละวันของชีวิตชายหนุ่ม ทั้งสองนั้นเกิดมาโดยมีชะตากรรมที่ทำให้ได้พบเจอกันและกันแบบนี้ เพื่อพิสูจน์ต่อจักรวาลว่ารักแท้นั้นมีอยู่จริง
# และถึงแม้เวลาทั้งสองจะสวนทางกัน แต่พวกเขาหวังว่าสักวันหนึ่ง จะมี "วันของทั้งสองตรงกัน" หมายถึงตัวเลขวันในเดือนที่ทั้งสองอยู่ตรงกันพอดี

# ทั้งสองเริ่มเดินทางในเส้นเวลาของตนเองโดย

# สมชายเริ่มจากวันที่ n และจบวันที่ m
# คชสารเริ่มจากวันที่ m และจบวันที่ n
# และทั้งสองต้องการจะพบกันให้ได้ในวันที่พอดี ว่ามีโอกาสเป็นไปได้ไหม โดยที่ :

# สมชายเริ่มที่วันที่ n แล้วเพิ่มวันไปเรื่อย ๆ ด้วยอัตรา V1
# คชสารเริ่มที่วันที่ m แล้วลดวันลงไปเรื่อย ๆ ด้วยอัตรา V2
# ทั้งสองคนอยากรู้ว่าเวลาของทั้งสองบรรจบกันเมื่อใด นั่นคือ "วันที่พวกเขาได้พบกัน" หรือ วันที่เป็น "จุดตัดของช่วงเวลา" ทั้งสองคนนั้นเอง


gay = input().split(" <-> ")
(guy, girl) = gay
# print(guy)
# print(girl)
step1 = int(input())
step2 = int(input())
current1 = int(guy)
current2 = int(girl)
result = ""
awaawa = 0
if int(guy) == int(girl):
    print(int(guy))
else:
    while current1 < int(girl) and current2 > int(guy):
        current1 = current1+step1
        current2 = current2-step2
        # print(current1,current2)
        if current1 == current2:
            awaawa = current1
            current2 = int(guy)
    if current1 != awaawa:
        result = "So sadly doe TT."
    else:
        result = awaawa
    print(result)


                            # &   Made by Parattakorn Boonprakob :P   & #
                        # !!! IF YOU USE THIS CODE, PLEASE CREDIT THE ORIGINAL !!! #
                                    # ???   Thanks for reading =Δ=   ??? #

                                            # ~ From the team, ~ #
                                         #  ^「The Procasinators」^  #