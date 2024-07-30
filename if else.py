# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 19:32:06 2024

@author: 99890
"""

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     print('Sizga kirish bepul.')
# elif yosh<=12:
#     print('Sizga kirish 5000 so\'m')
# elif yosh<=18:
#     print('Sizga kirish 8000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     narh = 0
# elif yosh<=12:
#     narh = 5000
# elif yosh<=18:
#     narh = 8000
# else:
#     narh = 10000
# print(f"Sizga kirish {narh} so'm") # Qisqartirib yozish usuli

# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')

# kun = input("Bugun nima kun?>>>")
# harorat = float(input("Havo harorati "))

# if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
#     print("Cho'milgani kettik!")
# elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<=30:
#     print('Uyda qolamiz!')


# narh = 15000 # mijoz 15000 so'mga taom oldim
# choy = True # mijoz choy ham oldi
# salat = True # mijoz salat olmadi

# if choy and salat : # agar mijoz choy ham salat ham olmagan bolsa
#     narh = narh+10000 #narhga 10000 qo'shamiz
# elif choy or salat: # agar choy yoki salat olgan bo'lsa
#     narh = narh+5000 #narhga 5000 qo'shamiz
    
# print(f"Jami {narh} so'm") #yakuniy narhni chiqazamiz

# narh = 15000 #mijoz 15 so'mga ovqat oldi
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 1
# #Quyidagi shart alohida tekshiriladi bir biriga bog'liq emas
# if choy: #Agar choy olsa
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat: #Agar salat olsa
#         print("Mijoz salat oldi.")
#         narh = narh + 5000
# if non: #Agar non olsa
#             print("Mijoz non oldi.")
#             narh = narh + 2000
# if kompot: #Agar kompot olsa
#                 print("Mijoz kompot oldi.")
#                 narh = narh + 5000
# if assorti: #Agar assorti olsa
#                     print("Mijoz assorti oldi.")
#                     narh = narh + 3000
# print(f"Jami {narh} so'm")


menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
ovqat = input('Nima ovqat yeysiz?>>>')
if ovqat.lower() in menu:
    print('Buyurtma qabul qilindi.')
else:
    print("Afsuski bizda bunday ovqat yo'q")
