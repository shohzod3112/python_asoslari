#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 23:17:36 2024
20-dars: 6-masala. Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.  Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
@author: moon
"""
import sys
sys.set_int_max_str_digits(100000)
print("a = ", end='')
a = int(input())

def Fibonachchi(a):
    fibo = []
    f1 = 1
    f2 = 1
    f3 = f1 + f2
    for i in range(1, a + 1):
        f1 = f2
        f2 = f3
        f3 = f1 + f2

        fibo.append(f3)
    
    return fibo

print(Fibonachchi(a))
    