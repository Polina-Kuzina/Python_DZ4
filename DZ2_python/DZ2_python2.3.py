#игра с конфетами
# Игрок и умный бот


candys = 2021
print('На столе ', candys, 'конфет')
while candys > 0:
    if candys > 28:
        a1 = int(input("Ваш ход. Сколько вы берете конфет: "))
        if a1 > 28:
            a1 = int(input("Вы не можете взять больше 28 конфет. Сколько вы берете конфет? "))            
            candys -= a1
            print('На столе осталось', candys, 'конфет')
        else:            
            candys -= a1
            print('На столе осталось', candys, 'конфет')
    else:
        print("Вы победили!")
        break   
    if candys > 28:
        a2 = candys % 28 - 1
        if a2 <= 0:
            a2 = 1
        print("Ход бота Сладкоежки. Бот Сладкоежка взял", a2, 'конфет')
        candys -= a2
        print('На столе осталось', candys, 'конфет')
    else:
        print("Бот Сладкоежка победил!")
        break