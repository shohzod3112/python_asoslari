#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:04:22 2024
#29-DARS. CLASSLAR BILAN ISHLASH
@author: moon
"""

class Myauto:
    """Mening mashinalarim haqida ma'lumot beradigan class"""
    def __init__(self, km, model, narh, rang = "qora", korobka = "avtomat"):
        self.km = km
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh

    def get_km(self):
        return f"{self.model} avtomobili {self.km} km yurgan"

    def get_model(self):
        return self.model

    def get_rang(self):
        return self.rang
    
    def get_info(self):
        return f"Modeli: {self.model}, Rangi: {self.rang}, Korobka: {self.korobka}, Narxi: {self.narh}"
    
    def set_km(self, new_km):
        self.km = self.km + new_km
        return self.km
    
    
auto1 = Myauto(0, "BMW", 150000)
auto2 = Myauto(0, "KI", 25000)
auto3 = Myauto(0, "BYD", 52000)
auto4 = Myauto(0, "Hyndai", 25000)

print(auto1.get_info())

class Avtosalon:
    def __init__(self, name, address = "Olmazor tumani", how_many_auto = 50000, when_created = 2028):
        self.name = name
        self.address = address
        self.how_many_auto = how_many_auto
        self.when_created = when_created
        self.auto_type = []
        
    def set_type_auto(self, new_model):
        self.auto_type.append(new_model)
        
    def get_type_auto(self):
        return [m.get_model() for m in self.auto_type]
    
    def get_info1(self):
        return f"{self.name} salonimiz {self.when_created} da tashkil topgan va {self.address}da joylashgan bo'lib {[a.get_model() for a in self.auto_type]} turidagi avtomobillar bor!!!"
 
new_auto = Avtosalon("Drivers village")
new_auto.set_type_auto(auto1)
new_auto.set_type_auto(auto2)
new_auto.set_type_auto(auto3)
new_auto.set_type_auto(auto4)
n = new_auto.get_type_auto()

print(n)
print(new_auto.get_info1(), "\n")
print(type(str), "\n")
print(f"str classining xususiyatlari va metodlari {dir(str)} \n")
print(type(int), "\n")
print(f"int classining xususiyatlari va metodlari {dir(int)} \n")

print("__dict__ metodi obyketning xususiyatlarini lug'at ko'rinishida qaytaradi. \n\n")
print(auto1.__dict__, "\n")
print("Natijadan faqatgina kalitlarni ajratib olsak, obyektning xususiyatlari chiqadi:\n")
print(auto1.__dict__.keys(), "\n")