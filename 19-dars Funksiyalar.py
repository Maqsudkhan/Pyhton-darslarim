#Bismillahir rohmanir rohiym
"""
Created on Sat Feb 25 15:48:32 2023
author: @Maqsudkhan2oo3
"""
#  Functions (Funksiyalar)



def salom_ber():
    """Salom beruvchi funksiya"""
    print('Assalom alaykum!')
# salom_ber()



def salom_ber(ism):
    """Foydalanuvchi ismini qabul qilib,
    unga salom beruvchi funksiya."""
    print(f"Assalom alaykum, hurmatli {ism.title()}!")
    
# salom_ber('maqsud')
# salom_ber('asad')



def toliq_ism(ism,familiya):
    """Foydalanuvchi ism va familyasini jamlab chiqaruvchi funksiya."""
    print(f"Foydalanuvchi ismi: {ism.capitalize()}\n"
    f"Foydalanuvchi familiyasi: {familiya.capitalize()}")
    
# toliq_ism('maqsud',"to'rayev")
# toliq_ism("to'rayev","maqsud")



def yosh_hisobla(ism,t_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.capitalize()} {2023-t_yil} yoshda")
    
# yosh_hisobla('maqsud',2003)
# yosh_hisobla(2003,'maqsud')

# yosh_hisobla(t_yil=2003,ism='maqsud')
#toliq_ism(familiya="to'rayev",ism='maqsud')




def yosh_hisobla(t_yil, joriy_yil=2023):
    """Foydalanuvchi tog'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-t_yil} yoshdasiz")
    
# yosh_hisobla(2003,2023)
# yosh_hisobla(2000)


#########                           AMALYOT


### 1

# def t_yil(ism,yosh):
#     """Foydalanuvchidan ism va yoshini so'rab,
# uning tug'ilgan yilini chiqaradigan funksuya"""
#     print(f"{ism.title()} {2023-yosh}-yilga tug'ilgan.")
# ism = input('Ismingizni kiriting: ')
# yosh = int(input('Yoshingizni kirititng: '))
# t_yil(ism,yosh)


### 2
 
# def son(a):
#     """Foydalanuvchidan son olib uning kvadrati va kubini chiqaruvchi funksiya"""
#     print(f"{a} ning kvadrati {a**2} ga teng!")
#     print(f"{a} ning kubi {a**3} ga teng!")
# a=float(input('Istalgan sonni kiriting: '))
# son(a)


### 3

# def juft_toq(a):
#     """ Foydalanuvchidan son olib  juft yoki toqligini chiqaruvchi funksiya"""
#     if a%2 == 0:
#         print(f"{a} soni juft son!")
#     else:
#         print(f"{a} soni toq son!")
# a = int(input('Istangan butun son kiriting: '))
# juft_toq(a)


### 4

# def taqqoslash(a,b):
#     """Foydalanuvchidan 2 ta son olib ulardan kattasini,
#     agar sonlar teng bolsa tengligini konsolga chiqauvchi funksiya"""
#     if a>b:
#         print(a)
#     if a==b:
#        print('Sonlar teng!')
#     if b>a:
#        print(b)
# a= float(input('1-sonni kiriting: '))
# b= float(input('2-sonni kiriting: '))
# taqqoslash(a, b)


### 5

# def daraja(x,y):
#     """foydalanuvchidan x va y sonlarini olib  x ning  y darajasini hisoblovchi funksiya"""
#     print(f"{x} ning {y}-darajasi: {x**y}")
# x = float(input('1-sonni kiriting: '))
# y = float(input('2-sonni kiriting: '))
# daraja(x,y)


### 6 

# def daraja(x,y=2):
#     """foydalanuvchidan x va y sonlarini olib  x ning  y darajasini hisoblovchi funksiya"""
#     print(f"{x} ning {y}-darajasi: {x**y}")
# x = float(input('Istalgan sonni kiriting: '))
# daraja(x)


### 7 

def bolinish_alomatlari(a):
    """Foydalanuvchidan son qabul qilib sonni 2 dan 10 gacha
bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
    for n in range(2,11):
        if a%n == 0:
            print(f"{a} soni {n} ga qoldiqsiz bo'linadi!")
a = int(input('istangan butun sonni kiriting: '))
bolinish_alomatlari(a)





