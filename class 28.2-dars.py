#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 18:06:05 2024
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
    
    def get_info(self):
        return f"Foydalanuvchi: {self.login}, ismi: {self.ism} {self.familya}, email: {self.email}"
        
user1 = User("Shohzod", "Ro'ziyev", "shoh", "passwd", "itsmygml6@gmail.com")

print(user1.get_info())