# -*- coding: utf-8 -*-
"""
Spyder Editor

***
STRING METODLARI
Pythonda string ustida amalga oshirish mumkin bo'lgan tayyor amallar to'plami mavjud. Bunday amallar to'plami metodlar deb ataladi. 

Metodlarni qo'llash uchun metod nomi matndan so'ng .metod_nomi() ko'rinishida yoziladi. Keling shunday metodlarning ba'zilari bilan tanishaylik.
***

"""


ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())




"""
title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi. 
"""

ism_sharif = 'james bond'
print(ism_sharif.title())

"""
capitalize() esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.

"""

ism_sharif = 'james bond'
print(ism_sharif.capitalize())





"""
strip(), rstrip() va lstrip() metodlari
Bu metodlar matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi.

lstrip() — matn boshidagi bo'shliqni,

rstrip() – matn oxiridagi bo'shliqni,

strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi
"""

meva = "     olma     "
print("Men " + meva.lstrip() + " yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() + " yaxshi ko'raman")
print("Men " + meva + " yaxshi ko'raman")






"""
INPUT —FOYDALANUVCHI BILAN MULOQOT
Shu paytgacha biz o'zgaruvchilarning qiymatini dasturning ichida berayotgan edik. Keling endi qiymatni o'zimiz emas, balki dastur foydalanuvchilariga kiritish imkonini beramiz. 

Buning uchun input() funktsyasidan foydalanamiz. 
"""

ism = input("Ismingiz nima? \n")
print("Assalom alaykum, " + ism)



























