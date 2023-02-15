# 11/12/2022
# List (Ro'yhat)
# Muallif: Maqsudkhan


mevalar = ['olma' , 'anjir' , 'shaftoli' , "o'rik"]
narxlar = [120500 , 11000 , 17000 , 23500 , 33000 , -11000 , 12500]
sonlar = ['bir' , 'ikki' , 3 , 4 , 5]
ismlar = [     ]

#print("Birnchi meva: " , mevalar[0].title()) #Birinchi elementga murojaat qilamiz
#print("Ikkinchi meva: " , mevalar[2].upper())
#print(narxlar[0] + narxlar[3]) 
#print(narxlar[-1]) #eng oxirgi elementga murojaat qilimiz
narxlar[1] =15000 #Birinchi qiymatni 15000 ga o'zgartiramiz
narxlar[3] = narxlar[3] + 5000 # 3-qiymatga 5000 qo'shamiz

# Yangi element qo'shish  ,append() metodi

mevalar.append('tarvuz') #mevalar ro'yhati oxiriga tarvuz elementi qo'shildi
#print(mevalar)

cars = []
cars.append('Lasetti')
cars.append('Nexia 3')
cars.append('Trecker')
cars.append('Malibu')
cars.append('Cobalt')
cars.append('Damas')
#print(cars)

#   del indeks orqali qiymatni o'chirish

del cars[1] # 2-element Nexia 3 o'chirib tashlandi
#print(cars)

#   .removo elementni qiymati buyicha o'chirish

cars.remove('Damas')
#print(cars)

cars.append('Malibu')
#print(cars)

cars.remove('Malibu') # 2 ta bir xil element(Malibu) bo'lsa birinchisini o'chiradi
print(cars)

#    Elementni sug'urib olish .pop()  ,  agar .pop() metodiga indeks belrilmasa ro'yxatdan oxirgi qiyatni sug'irib oladi

bozorliq = ['un' , 'yog' , 'saroyog' , 'piyoz' , 'banan' , 'kartoshka']
mahsulot = bozorliq.pop(2)  # ruyxatdan saroyogni sug'irib olamiz
print("Men" , bozorliq , " sotib oldim.")
print("olinmagan mahsuloh " , mahsulot )

 

# AMALYOR






