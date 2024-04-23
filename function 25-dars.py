
"""
Created on Sat Apr 13 14:24:33 2024

@author: moon
"""

import random as r # random modulini r deb chaqirayapmiz

def sontop(x = 10):
    komp_oylagan_son = r.randint(1,x) # 0 va 100 oralig'ida tasodifiy son
    print(" \n1 <= 10 oraliqda son o'yladim. Topa olasizmi?\n", end = '')
    user_urunish_soni = 0
    
    while True:
        user_urunish_soni += 1
        userson=int(input(">>>"))
    
        if userson < komp_oylagan_son :
            print("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling:")
                  
        elif userson > komp_oylagan_son :
            print("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling:")
        
        else: 
            break
    print(f"Tabriklayman. {user_urunish_soni} ta taxmin bilan topdingiz!")
    return user_urunish_soni


def sontop_pc(x = 10):
    input(f"\n1 <= {x} gacha oraliqda son o'ylang. Men topishga harakat qilaman.\n\nSon o'ylagan bo'lsangiz istalgan tugmani bosing.\n")

    quyi = 1
    yuqori = x
    komp_urunish_soni = 0
    
    while True:
        komp_urunish_soni += 1
        if quyi != yuqori:
            user_oylagan_son = r.randint(quyi, yuqori)
        else: 
            user_oylagan_son  = quyi
        javob = input(f"Siz {user_oylagan_son} ni o'yladingiz: to'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)??".lower())
        
        if javob == '-':
            yuqori = user_oylagan_son - 1
        elif javob == '+':
            quyi = user_oylagan_son + 1
        else:
            break
    print(f"Siz o'ylagan soningizni {komp_urunish_soni} ta taxmin bilan topdim!")
    return komp_urunish_soni

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user>taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va yutdim!")
        elif taxminlar_user<taxminlar_pc:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))
            
play()