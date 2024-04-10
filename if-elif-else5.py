"""
25/11/2020
Dasturlash asoslari
#11-dars: if-elif-else
Muallif: Anvar Narzullaev
Web sahifa: https://python.sariq.dev
"""

users = ['alisher','aziza','yasina','umar']

login = input("Yangi login tanlang: ")

if login in users:
    print('Login band, yangi login tanlang!')
else:
    print(f"Xush kelibsiz, {login.title()}!")