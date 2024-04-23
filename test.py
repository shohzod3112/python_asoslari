#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:36:29 2024

@author: moon
"""

class Talaba:
    def __init__(self, ism, familya, tyil):
        self.ism = ism
        self.familya = familya
        self.tyil = tyil
        
    def get_name(self):
        return self.ism
    
    def get_age(self, yil):
        return yil - self.tyil
    
    def get_lastname(self):
        return self.familya
    
    def tanishtir(self):
        return f"Ismim {self.ism}, Familiyam {self.familya}, tug'ilgan yilim {self.tyil}"
    
    
talaba1 = Talaba("Olim", "Davletov", 2011)
talaba2 = Talaba("Hasan", "Husanov", 2001)
talaba3 = Talaba("Malik", "Qayumov", 1991)