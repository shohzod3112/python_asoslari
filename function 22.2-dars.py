"""
Dasturlash asoslari

22-dars: *args va **kwargs. 
Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
ism = input("Ismingizni kiriting: ")
fam = input("Familyangizni kiriting: ")

#info = {}

def kopaytma(ism, fam, **info):
    info['ism'] = ism
    info['fam'] = fam
    
    return info


print(kopaytma(ism, fam, yoshi = '4'))