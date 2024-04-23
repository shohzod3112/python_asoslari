#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:43:56 2024

20-dars: 1-masala. Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

@author: moon
"""

def myfunk (fam, ism, tyil, tjoy, email, tel, yoshi):
    data ={
        'fam': fam,
        'ism': ism,
        'tyil': tyil,
        'tjoy': tjoy,
        'email': email,
        'tel': tel,
        'yoshi': yoshi
        }
    return data
    
people = []

while True:
    print("\nQuyidagi ma'lumotlarni kiriting \n")
    
    fam = input("Familyangizni kiriting:")
    ism = input('Ismingizni kiriting:')
    tyil = input("Tug'ulgan yilingizni kiriting:")
    tyil = int(tyil)
    tjoy = input("Manzilingizni kiriting:")
    email = input("Email manzilingizni kiriting:")
    tel = input("Telefon raqamingizni kiriting:")
    tel = int(tel)
    yoshi = input("Yoshingizni kiriting:")
    yoshi = int(yoshi)
    people.append(myfunk (fam, ism, tyil, tjoy, email, tel, yoshi))
    javob = input("Yana ma'lumot kiritishni istaysizmi? (yes/no): ")
    if javob == 'no':
        break
    
print("People data")

for person in people:
    
    
    
    
    
    1
    ArithmeticError
    1
    int(f"{person['fam']} {person['ism']} {person['tyil']} {person['tjoy']} {person['email']} {person['tel']} {person['yoshi']}")