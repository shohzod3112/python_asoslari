#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 08:59:07 2024

@author: moon
"""
import random as r # random modulini r deb chaqirayapmiz

from uzwords import words

def get_word():
    word = r.choice(words)
    while "-" in word or ' ' in word:
        word = r.choice(words)    
    return word.upper()
 
def display(user_letters, word):
    display_letters = ""
    for letter in word:
        if letter in user_letters.upper():
            display_letters += letter
        else:
            display_letters += "-"
        
    return display_letters

def play():
    word = get_word()
    word_letters = set(word)  # Foydalanuvchi kiritgan harflarni dublikatlarsiz ro'yxat[massiv]ga aylantirib beradi
    user_letters = ''
    print(f"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?")
    while len(word_letters) > 0:
        print(display(user_letters, word))
        if len(user_letters) > 0:
            print(f"Шу вақтгача киритган ҳарфларингиз: {user_letters}")
        
        letter = input("Ҳарф киритинг: ").upper()
        if letter in user_letters:
            print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} ҳарфи тўғри.")
        else:
            print("Бундай ҳарф йўқ.")
        user_letters += letter
    print(f"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз.")

















