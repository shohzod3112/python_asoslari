#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:57:48 2024
QIYMAT QAYTARUVCHI FUNKSIYA: Funktsiya orqali obyekt qaytarishga misol
@author: moon
"""

def avto_info(kompaniya, model, rang, korobka, yil, narh=None):
    avto = {
        "kompaniya": kompaniya,
        "model": model,
        "rang": rang,
        "korobka": korobka,
        "yil": yil,
        "narh": narh,
    }
    return avto

print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting",end='')
    kompaniya=input("\nIshlab chiqaruvchi: ")
    model=input("Modeli: ")
    rang=input("Rangi: ")
    korobka=input("Korobka: ")
    yil=input("Ishlab chiqarilgan yili: ")
    narh=input("Narhi: ")
    
    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model, rang, korobka, yil, narh))
    
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break
    
for avto in avtolar:
    print(f"{avto['kompaniya'].upper()}, {avto['model'].title()}, {avto['rang'].title()}, {avto['korobka'].title()}, {avto['yil']}, {avto['narh']}")