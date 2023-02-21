#Bismillahir Rohmanir Rohim!
"""
Created on Mon Feb 20 22:56:20 2023
"""
"""
car0={
      'model':'lacetti',
      'rangi':'oq',
      'yil':2018,
      'narh':13000,
      'km':50000,
      'karobka':'avtomat'
      }

car1={
      'model':'nexia 3',
      'rangi':'qora',
      'yil':2015,
      'narh':11000,
      'km':98000,
      'karobka':'mexanika'
      }


car2={
      'model':'gentra',
      'rangi':'qora',
      'yil':2022,
      'narh':17000,
      'km':18000,
      'karobka':'avtomat'
      }

car=car0
print(f"{car['model'].title()}, "
      f"{car['rangi']} rang, "
      f"{car['yil']}-yil, {car['narh']}$.")


car=car1
print(f"{car['model'].title()}, "
      f"{car['rangi']} rang, "
      f"{car['yil']}-yil, {car['narh']}$.")


car=car2
print(f"{car['model'].title()}, "
      f"{car['rangi']} rang, "
      f"{car['yil']}-yil, {car['narh']}$.")



cars=[car0,car1,car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rangi']} rang, "
          f"{car['yil']}-yil, {car['narh']}$!")
              


print(f"{cars[2]['rangi'].title()} "
      f"{cars[2]['model'].title()}")




malibus=[]
for n in range(10):
    new_car = {
        'model':'malibu',
        'rangi':None,
        'yil':2023,
        'narh':None,
        'km':0,
        'karobka':'avtomat'        
        }
    malibus.append(new_car)

#for malibu in malibus:
#    print(malibu)

for malibu in malibus[:3]:
    malibu['rangi']='qizil'

#for malibu in malibus:
#    print(malibu)

for malibu in malibus[3:6]:
    malibu['rangi']='qora'

#for malibu in malibus:
#    print(malibu)

for malibu in malibus[6:]:
    malibu['rangi']='qora'
    malibu['karobka']='mexanika'

#for malibu in malibus:
#    print(malibu)


for malibu in malibus:
    if malibu['karobka']=='avtomat':
        malibu['narh']=40000
    else:
        malibu['narh']=35000

print(malibus)





dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
   }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quydagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quydagi dasturlash tillarini biladi:",end='')
    for til in tillar:
        print(f'{til.upper()} ', end='')






hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']},    
    
    
    'vali':{'familiya':'aliyev',
            'tyil':2000,
            'malumot':"o'rta-maxsus",
            'tillar':['html','css','js']},
    
    'maqsud':{'familiya':"torayev",
              'tyil':2003,
              'malumot':'maxsus',
              'tillar':['python','blender']}
       
    }



for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan.\n"
          f"Ma'lumoti: {info['malumot']}.\n"
          f"Quyidagi tillarni biladi:")
    
    for til in info['tillar']:
        print(til.upper())

"""

                              ###   AMALYOT   ###

######## 1
"""
shaxs={ 
       'Abu Abdulloh Muhhammad ibn Ismoil':{
           'tyil':810,
           'tjoy':'buxoro',
           'umri':60 },
       
       'abdulla qodiriy':{
           'tyil':1984,
           'tjoy':'toshkent',
           'umri':44 },
       
       'erkin vohidov':{
           'tyil':1936,
           'tjoy':"farg'ona",
           'umri':80 },
       
       'alisher navoiy':{
           'tyil':1441,
           'tjoy':'xirot',
           'umri':60 }
             
       }

for ism, info in shaxs.items():
    print(f"{ism.title()} {info['tyil']}-yilda "
          f"{info['tjoy'].title()}da tavallud topgan. "
          f"{info['umri']} yil umr ko'rgan.")


####### 2

shaxs={ 
       'Abu Abdulloh Muhhammad ibn Ismoil':{
           'tyil':810,
           'tjoy':'buxoro',
           'umri':60, 
           'asarlar':['Al-jome\' as-sahih','Al-adab al-mufrad','At-tarix al-kabir','At-tarix al-sag\'ir']},
       
       'abdulla qodiriy':{
           'tyil':1984,
           'tjoy':'toshkent',
           'umri':44, 
           'asarlar':["O'tgan kunlar",'Mehrobdan chayon','Obid ketmon'] },
              
       'erkin vohidov':{
           'tyil':1936,
           'tjoy':"farg'ona",
           'umri':80,
           'asarlar':['Tong nafasi',"Qo'shiqlarim sizga","O'zbegim",'Qiziquvchan Matmusa']},
       
       'alisher navoiy':{
           'tyil':1441,
           'tjoy':'xirot',
           'umri':60,
           'asarlar':['Xamsa','Lison ut-Tayr','Mahbub Al-Qulub']}
             
       }

for ism, info in shaxs.items():
    print(f"\n{ism.title()} ning mashxur asarlari:")
    for asar in info['asarlar']:
        print(asar)



######## 3

friend={
        'shuhrat':['termenator','rambo','titanic'],
        'dilshod':['tenet','inception','interstellar',],
        'asilbek':['abdullajon','bomba','shaytanat'],
        'asad':['mahallada duv-duv gap','john wick','merlin']
        }

for ism,ruyxat in friend.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in ruyxat:
       print(kino.capitalize())




####### 4

davlatlar = {
   "o'zbekiston":{
      'poytaxt':'toshkent',
      'hudud':'448978 kv.km',
      'aholi':33000000,
      'pul birligi':"so'm" },
  
    "rossia":{
       'poytaxt':'moskva',
       'hudud':'17098246 kv.km',
       'aholi':144000000,
       'pul birligi':"rubl" },
   
    "AQSH":{
       'poytaxt':'vashington',
       'hudud':'963141 kv.km',
       'aholi':327000000,
       'pul birligi':"dollar" },
   
    "malayziya":{
       'poytaxt':'kuala-lampur',
       'hudud':'329750 kv.km',
       'aholi':25000000,
       'pul birligi':"rinngit" }
    }


for davlat, info in davlatlar.items():
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].capitalize()}.\n"
          f"Hududi: {info['hudud']}\nAholisi: {info['aholi']}\nPul birligi: {info['pul birligi'].capitalize()}")


"""
 

#######  5


davlatlar = {
   "o'zbekiston":{
      'poytaxt':'toshkent',
      'hudud':'448978 kv.km',
      'aholi':33000000,
      'pul birligi':"so'm" },
  
    "rossia":{
       'poytaxt':'moskva',
       'hudud':'17098246 kv.km',
       'aholi':144000000,
       'pul birligi':"rubl" },
   
    "aqsh":{
       'poytaxt':'vashington',
       'hudud':'963141 kv.km',
       'aholi':327000000,
       'pul birligi':"dollar" },
   
    "malayziya":{
       'poytaxt':'kuala-lampur',
       'hudud':'329750 kv.km',
       'aholi':25000000,
       'pul birligi':"rinngit" }
    }

davlat=input('Davlat nomini kiriting: ').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].capitalize()}.\n"
              f"Hududi: {info['hudud']}\nAholisi: {info['aholi']}\nPul birligi: {info['pul birligi'].capitalize()}")
        
else:
    print('Bizda bu davlat haqida ma\'lumot mavjud emas!')
       



