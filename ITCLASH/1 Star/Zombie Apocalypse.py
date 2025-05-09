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
    elif int(armor[i]) > dmg:
        curdmgdealt = dmg-int(armor[i])
    elif int(armor[i]) <= dmg:
        armorcount = (i+1)**2
        curdmgdealt = dmg
    while int(hp[i]) > 0:
        if armorcount > 0:
            while armorcount > 0:
                armorcount -= 1
                totalbulletcount += 1
                if armorcount == 0:
                    break
        else:
            int(hp[i]) == curdmgdealt-int(hp[i])
            totalbulletcount += 1
        if int(hp[i]) <= 0:
            bulletdeath.append(totalbulletcount)
            break
print(totalbulletcount)
print(" ".join(bulletdeath))