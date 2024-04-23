#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:54:28 2024
#28-DARS. KLASSLAR
@author: moon
"""

class User():
    def __init__(self, ism, familya, login, parol, email):
        self.ism = ism
        self.familya = familya
        self.login = login
        self.parol = parol
        self.email = email

    def get_name(self):
        return self.ism
    
    def get_fam(self):
        return self.familya
    
    def get_login(self):
        return self.login
    
    def get_passwd(self):
        return self.parol
    
    def get_email(self):
        return self.email    
        
user1 = User("Shohzod", "Ro'ziyev", "shoh", "passwd", "itsmygml6@gmail.com")

print(user1.get_name())
print(user1.get_fam())
print(user1.get_login())
print(user1.get_passwd())
print(user1.get_email())