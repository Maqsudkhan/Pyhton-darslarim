""" Bismillahir Rohmanir Rohim

Created on Tue Feb 21 23:32:16 2023
"""
# input()

#ism = input('Ismingiz nima? ')
#savol = f"Salom, {ism.title()}. yoshingiz nechchida? "
#yosh =  int(input(savol))
#height = float(input("Bo'yingiz nechchi metr? "))

###                          while()

son = 1
while son<=10:
    print(son, end=' ')
    son += 1
print('Dastur tugadi.')
"""

#####                        while and input
"""
print('Kiritilgan sonni kvadratini qaytaruvchi dastur.')
savol = "Istalgan sonni kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing):\n>>> "
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)
print('Dastur tugadi.')




print('Kiritilgan sonni kvadratini qaytaruvchi dastur.')
savol = "Istalgan sonni kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing):\n>>> "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)
print('Dastur to\'xtadi!')


######                       break while

print('Kiritilgan sonni kvadratini qaytaruvchi dastur.')
savol = "Istalgan sonni kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing):\n>>> "
while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    else:
        print(float(qiymat)**2)
print('Dastur to\'xtadi!')


#####                        break for

sonlar = list(range(1,11))
for son in sonlar:
    if son == 6:
        break
    print(f"{son} ning kvadrati {son**2} ga teng")



######                         continue


sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        continue
    print(f"{son} ning kvadrati {son**2} ga teng")




########                  continue while


son=0
while son<10:
    son += 1
    if son%2 == 0:
        continue
    else:
        print(son)
    


########                  infinite loop

son=0
while son<10:
    if son%2 != 0:
        continue
    else:
        print(son)



son=0
while son<10:
    
    if son%2 == 0:
        continue
    else:
        print(son)
son += 1





son=1
while son>0:
    son += 1
    if son%2 != 0:
        continue
    else:
        print(son)



#######                          AMALYOT


# 1

savol = "Yaxshi ko'rgan kitobingzni kiriting "
savol += "(dasturni tuxtatish uchun 'stop' deb yozing): "
kitob=''
#while kitob != 'stop':
#    kitop = input(savol)
#    if kitop == 'stop':
#        break
    
#while True:
#    kitob = input(savol)
#    if kitob == 'stop':
#        break
#print('Raxmat!')    


# 2
#2.1

yosh=''
savol = 'Yoshingizni kiriting: '
while True:
    yosh= input(savol)  
    if yosh == 'exit' or yosh =='quit':
        break        
    if int(yosh) <= 7:
        narx=2000
    if 7 < int(yosh) <= 18:
        narx=3000
    if 18< int(yosh) <= 65:
        narx=10000
    if int(yosh)>65:
        narx=0
    if narx == 0:
        print('Sizga chipta bepul!\n')
    else:
        print(f"Sizga chipta {narx} so'm!\n")    
    
 

#2.2
  
yosh=''
savol = 'Yoshingizni kiriting: '

while yosh != 'exit' or yosh != 'quit':
    yosh= input(savol) 
    
    if yosh == 'exit' or yosh == 'quit':
        break
    if int(yosh) <= 7:
        narx=2000
    if 7 < int(yosh) <= 18:
        narx=3000
    if 18< int(yosh) <= 65:
        narx=10000
    if int(yosh)>65:
        narx=0
    if narx == 0:
        print('Sizga chipta bepul!\n')
    else:
        print(f"Sizga chipta {narx} so'm!\n")    


#2.3

yosh=''
savol = 'Yoshingizni kiriting: '
ishora = True
while ishora:
    yosh= input(savol)  
    if yosh == 'exit' or yosh =='quit':
        ishora=False        
        
    elif int(yosh) <= 7:
       print('2000 so\'m')
    elif 7 < int(yosh) <= 18:
        print("3000 so'm")
    elif 18< int(yosh) <= 65:
        print("10000 so'm")
    elif int(yosh)>65:
        print('bepul')
    

    

#3

savol = "Kiritilgan sonni ildizini qaytaruvchi dastur.\n"
savol += 'Musbat son kiriting '
savol += "(dasturni tuxtatish uchun 'exit' deb yozing):"

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break    
    if float(qiymat) < 0:
        continue
    else:
        ildiz =  float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng! ")









