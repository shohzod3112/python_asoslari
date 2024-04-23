#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:04:22 2024
#29-DARS. OBYEKTLAR BILAN ISHLASH
@author: moon
"""

class Myauto:
    """Mening mashinalrim haqida ma'lumot beradigan class"""
    def __init___(self, km, model, rang, korobka, narh):
        self.km = km
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh

    def get_km(self):
        return self.km

    def get_model(self):
        return self.model

    def get_rang(self):
        return self.rang
    
    def get_info(self):
        return f"Modeli: {self.model}, Rangi: {self.rang}, Korobka: {self.korobka}, Narxi: {self.narh}"
    
    def set_km(self, new_km):
        return self.km + new_km
    
    
auto1 = Myauto()

print(auto1.get_info())