#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 22:11:40 2024

20-dars: 3-masala. Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

@author: moon
"""

def maximum(x, y, z):
    maxi = x
    if maxi < y:
        maxi = y
    if maxi < z:
        maxi = z
    return maxi

print("\nbirinchi sonni kiriting: ")
x = int(input());
print("\nIkkinchi sonni kiriting: ")
y = int(input());
print("\nUchinchi sonni kiriting: ")
z = int(input());

print(f"\nSonlarning eng kattasi: {maximum(x, y, z)}")
