# Zombie apocalypse

# คุณตื่นขึ้นมากลางดึกแล้วพบว่าตอนนี้โลกของเราเต็มไปด้วยซอมบี้เสียแล้ว คุณต้องกำจัดซอมบี้ทั้งหมดที่อยู่บริเวณบ้านของคุณเพื่อให้คุณมีชีวิตรอดต่อไปได้ แต่ซอมบี้บางตัวมี "เกราะ" ซึงช่วยลดความเสียหายจากกระสุนที่ได้รับ กระสุนปืนของคุณมีพลังทำลายที่แน่นอน (damage) แต่ผลของมันจะถูกลดลงตามค่า เกราะ(armor) ของซอมบี้แต่ละตัว

# ถ้า damage <= armor จะต้องใช้กระสุนยิงจำนวน n นัดเพื่อทำลายเกราะ โดยที่ n จะเท่ากับลำดับที่ของซอมบี้ตัวนั้นยกกำลัง 2 และนัดต่อๆไปซอมบี้จะโดนดาเมจเข้าเท่ากับ ดาเมจของกระสุน
# ถ้า damage > armor ซอมบี้จะได้รับดาเมจในแต่ละนัดเท่ากับ damage - armor
# ** คุณต้องคำนวณว่าต้องใช้กระสุนทั้งหมดกี่นัด และซอมบี้แต่ละตัวตายในนัดที่เท่าไหร่ **

dmg = int(input())
hp = input().split()
armor = input().split()
armorcount = 0
bulletdeath = []
totalbulletcount = 0
curdmgdealt = 0
for i in range(len(hp)):
    if int(armor[i]) == 0:
        curdmgdealt = dmg
    elif int(armor[i]) < dmg:
        curdmgdealt = dmg-int(armor[i])
    elif int(armor[i]) >= dmg:
        armorcount = (i+1)**2
        curdmgdealt = dmg
    if dmg == 0:
        break
    else:
        while int(hp[i]) > 0:
            if armorcount > 0:
                while armorcount > 0:
                    armorcount -= 1
                    totalbulletcount += 1
                    # print("count in",totalbulletcount)
                    # print("death in",bulletdeath)
                    if armorcount == 0:
                        armor[i] = 0
                        break
            else:
                hp[i] = int(hp[i])-curdmgdealt
                totalbulletcount += 1
                # print("count out",totalbulletcount)
                # print("death out",bulletdeath)
            if int(hp[i]) <= 0:
                bulletdeath.append(totalbulletcount)
                break
print(totalbulletcount)
if len(bulletdeath) == 1:
    print(bulletdeath[0])
elif totalbulletcount == 0:
    print(0)
else:
    print(*bulletdeath, sep=' ')



                            # &   Made by Parattakorn Boonprakob :P   & #
                        # !!! IF YOU USE THIS CODE, PLEASE CREDIT THE ORIGINAL !!! #
                                    # ???   Thanks for reading =Δ=   ??? #

                                            # ~ From the team, ~ #
                                         #  ^「The Procasinators」^  #