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
    
    fam = input("Familiyangizni kiriting:")
    ism = input('Ismingizni kiriting:')
    tyil = input("Tug'ulgan yilingizni kiriting:")
    while True:
        if not tyil.isdigit():
            print("Iltimos faqat son kiriting\n")
            print(type(tyil))
            tyil = input("Tug'ulgan yilingizni kiriting:")
        else: break
        
    tyil = int(tyil)
    print(type(tyil))
    tjoy = input("Manzilingizni kiriting:")
    email = input("Email manzilingizni kiriting:")
    tel = input("Telefon raqamingizni kiriting:")
    while True:
        if not tel.isdigit():
            print("Iltimos faqat son kiriting\n")
            tel = input("Telefon raqamingizni kiriting:")
        else:
            break
    tel = int(tel)
    yoshi = input("Yoshingizni kiriting:")
    while True:
        if not yoshi.isdigit():
            print("Iltimos faqat son kiriting\n")
            yoshi = input("Yoshingizni kiriting:")
        else:
            break
    yoshi = int(yoshi)
    people.append(myfunk (fam, ism, tyil, tjoy, email, tel, yoshi))
    javob = input("Yana ma'lumot kiritishni istaysizmi? (yes/no): ")
    if javob == 'no':
        break
    
print("Kiritgan ma'lumotlaringiz")

for person in people:
    print(f"Familya: {person['fam']}\nIsmingiz: {person['ism']}\nTug'ulgan yilingiz: {person['tyil']}\nManzilingiz: {person['tjoy']}\nEmailingiz: {person['email']}\nTelefon raqamingiz: {person['tel']}\nYoshingiz: {person['yoshi']}")