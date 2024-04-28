#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 18:13:11 2024
#29-DARS. CLASSLAR BILAN ISHLASH
@author: moon
"""

class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
        
        
    def set_bosqich(self, yangi_bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = yangi_bosqich
    
    def update_bosqich(self):
        """Talabaning bosqichini 1taga ko'paytirish"""
        self.bosqich += 1
    
    def get_info(self):
        """Talaba haqidagi ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    
    def get_lastname(self):
        """Talabaning familyasini qaytaradi"""
        return self.familiya
    
    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"

    def get_age(self, yil):
        """Talabaning yoshini qaytaradi"""
        return yil - self.tyil

    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'g'ilganman {self.get_age(2024)} yoshdaman va {Fan.get_name(matematika)} faniga qatnashaman")
    
    
class Fan:
    """Fan nomli klass"""

    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_name(self):
        """Fan nomi"""
        return self.nomi

    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return [talaba.get_fullname() for talaba in self.talabalar]

    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni
    
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith("__") is False]


matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon", "Valiyev", 2000)
talaba2 = Talaba("Hasan", "Alimov", 2001)
talaba3 = Talaba("Akrom", "Boriyev", 2001)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

# print(matematika.talabalar_soni)
# print(matematika.talabalar)
# mat_talabalar = matematika.get_students()
# print(mat_talabalar)

# print(see_methods(Talaba))
#print(see_methods(talaba1))
#print(see_methods(str))
# print(talaba1.__dict__)
# print(talaba1.__dict__.keys())