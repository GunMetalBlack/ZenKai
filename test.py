hp = 30
power = 2
defense = 4
ki = 7
max_ki = 7
while(True):
    ki -= 1
    damage = power + int(1 - (defense * ki/max_ki))
    print( 1 - (defense * ki/max_ki), " Prec: dmg", "KI:", ki)
    print(damage , "DMG")
    if(damage > 0):
        hp -= int(damage)
    print(hp , "HP")
    input()