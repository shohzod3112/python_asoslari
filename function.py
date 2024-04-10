"""
16/12/2020

Dasturlash asoslari

#19-dars: FUNCTIONS (FUNKSIYALAR)

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

# Foydalanuvchidan son qabul qilib, sonni 2, 3, 4 va 5 ga qoldiqsiz bo'linishini tekshiruvchi 
# funksiya yozing. 
# Natijalarni konsolga chiqaring ("15 soni 3 ga qoldiqsiz bo'linadi" ko'rinishida)
def bolinish_alomatlari(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(20)

# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
def kv_kub(son):
    """Kiritilgan sonning kvadrati va kubini konsolga chiqaruvchi funksiya"""
    print(f"{son} ning kvadrati {son**2} ga, kubi {son**3} ga teng")

kv_kub(-4)

# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
def juftmi(son):
    """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
    if son%2:
        print(f"{son} toq son")
    else:
        print(f"{son} juft son")

juftmi(20)
juftmi(123)

# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
def solishtir(x,y):
    """Ikki sonni solishtiruvchi funksiya"""
    if x>y:
        print(f"{x}>{y}")
    elif x<y:
        print(f"{y}>{x}")
    else:
        print(f"{x}={y}")

solishtir(10,20)
solishtir(-9,12)
solishtir(1223*5,5**4)

# Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.
# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
def daraja(x,y=2):
    print(f"{x} ning {y}-darajasi {x**y} ga teng")

daraja(5,2)
daraja(3,3)
daraja(94,4)
daraja(6)

# Foydalanuvchidan son qabul qilib, sonni 2, 3, 4 va 5 ga qoldiqsiz bo'linishini tekshiruvchi 
# funksiya yozing. 
# Natijalarni konsolga chiqaring ("15 soni 3 ga qoldiqsiz bo'linadi" ko'rinishida)
def bolinish_alomatlari(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(20)