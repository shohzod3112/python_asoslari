#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 23:20:30 2024
20-dars: 5-masala. Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
@author: moon
"""

print("\na = ")            
a = int(input());

print("\nb = ")
b = int(input());

def tub(a, b):
    tub_sonlar = []
    for son in range(a, b + 1):
        x = 0
        for k in range(2, int(son / 2)):
            
            if son % k == 0:
                x = x + 1
                break

        if x == 0:
            tub_sonlar.append(son)
            
    return tub_sonlar

print(tub(a, b))