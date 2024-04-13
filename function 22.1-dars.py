"""
Dasturlash asoslari

#22-dars: *args va **kwargs. Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

def kopaytma(*sonlar):
    k = 1
    for son in sonlar:
        k *= son
    return k


print(kopaytma(10, 2, 3))