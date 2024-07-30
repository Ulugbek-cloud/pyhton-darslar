# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:12:11 2024

@author: 99890
"""

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print("Salom", mehmon)
#     print("Hayr", mehmon)

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi\n")

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(11)) #1 dan 10 gacha sonlar ro'yhatini yozing
# sonlar_kvadrati =   [] # bo'sh ro'yhat yaratamiz
# for son in sonlar: #sonlardagi har bir son uchun
#      sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, 
    
# print(sonlar)
# print(sonlar_kvadrati)    

dostlar = [] #bo'sh ro'yhat
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): # n bu yerda 0 dan 4 gacha qiymat oladi
    dostlar.append(input(f"{n+1}-do'stingizni ismini kiriting: "))
    print(dostlar)