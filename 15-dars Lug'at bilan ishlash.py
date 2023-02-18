""" Bismillahir Rohmanir Rohim

Created on Sat Feb 18 08:43:32 2023
"""

ozim={
      'ism':'Maqsud',
      'familiya':'Turayev',
      'yosh':22,
      'fakultet':'DIF',
      "kurs":3
      }
                              ###  items() metodi
"""                              
print(ozim.items())
for key, value in ozim.items():
    print(f"Kalit: {key}")
    print(f"Qiymat: {value}\n")

"""
 
phons ={
        'ali':'iphone 11',
        'vali':'galaxy s10',
        'soli':'redmi 11',
        'hasan':'nokia 3310',
        'husan':'samsung A51'
        
        }
                             ###  keys() metodi
                             
#for k, q in phons.items():
#    print(f"{k.title()}ning telefoni {q.title()}.")
    
#print(phons.keys())

#print('Isimlar ro\'yxatii:')
#for ism in phons.keys():
#    print(ism.title())





mahsulotlar={
    'olma':5000,
    'uzum':15000,
    'anor':12000,
    'banan':18000,
    "nok":20000,
    'xurmo':35000,
    'apelsin':10000
    }
"""
bozorlik=['xurmo','nok','olma','qovun','non','baliq','uzum','shaftoli','anor','tarvuz','banan']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga {buyum.title()} ham olib keling!")

for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())

"""

                               ###  values() metodi
"""
print('Foydalanuvchilar quydagi telfonlarni ishlatadilar:')
for tel in phons.values():
    print(tel.title())
"""


                                ###  set()
phons ={
        'ali':'iphone 11',
        'vali':'galaxy s10',
        'soli':'redmi 11',
        'hasan':'nokia 3310',
        'husan':'samsung A51',
        'maqsud':'samsung A52',
        'shuhrat':'iphone 11',
        'asilbek':'redmi 11',
        'asliddin':"iphone 11",
        'dilshid':'iphone 11'
        }

#print('Foydalanuvchilar quydagi telfonlarni ishlatadilar:')
#for tel in set(phons.values()):
#    print(tel)
    
#toys = {'ball','car','lamp','ball','bear','ar'}
#print(toys)




                          ###    AMALIYOT    ###





lugat_py={     
     'boolean':'mantiqiy qiymat',
     'float':"o'nlik son",
     'for':'biror amalni qayta-qayta bajarish tsikli',
     'if':'shartlarni tekshirish operatori',
     'integer':'butun son',
     'string':'matn',
     'list':"ro'yxat",
     'dictionry':'lug\'at',
     'keys':'kalit',
     'values':'qiymat'
     }

#for k, q in sorted(lugat_py.items()):
#    print(f"{k.title()}-{q.capitalize()}")



davlatlar = {
    "o'zbekiston":'toshkent',
    'rassia':'moskva',
    'aqsh':'washington',
    'tojikiston':'dushanbe',
    "qozog'ziston":'bishkek',
    'italya':'rim',
    'malayziya':'kuala-lumpur'
    }
"""
print("Do'nyo davlatlari:")
for davlat in sorted(davlatlar):
    print(f"{davlat.upper()}")

print('\nDavlatlarning poytaxtlari:')

for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())


m=input('Qaysi davlatling poytaxtinmi bilishni istaysiz?: ')
m=m.lower()
if m in davlatlar:
    print(f"{m.upper()}ning poytaxti {davlatlar[m].title()}")
else:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q!')

"""




menyu = {
    'non':'4000',
    'choy':'2000',
    'cola':'12000',
    'bliss':'13000',
    'osh':'25000',
    'shurva':'18000',
    'manti':'6000',
    'shashlik':'14000',
    'lag\'mon':'20000',
    'norin':'17500',
    'mastava':'19000'
    }
buyurtma=[]
print('3 ta taom buyurtma bering: ')
for n in range(3):
    buyurtma.append(input(f"{n+1}-taom: ").lower())
for z  in buyurtma:    

    if z in menyu:
        print(f"{z.title()} {menyu[z]} so'm.")
    else:
        print(f"Kechirasiz, bizda {z} yo'q.")
















