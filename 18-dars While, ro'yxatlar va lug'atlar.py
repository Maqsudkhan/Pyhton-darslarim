# Bismillahir rohmanir rohiym


print("Yaqin do'stlaringiz ro'yxatini tuzmiz.")
names = []
n = 1
while True:
    savol = f"{n}-do'stingizni ismini kiriting: "
    name = input(savol)
    names.append(name)
    takrorlash = input("Yana ism qushasizmi?(ha/yo'q) ")
    n +=1
    if takrorlash != 'ha':
        break
    
print("Do'stlaringiz ro'yxati:")
for name in names:
    print(name.title())




print("Do'stlaringiz yoshini saqlaymiz.")
friends = {}
ishora = True
while ishora:
    name = input("\nDo'stingizni ismini kiriting: ")
    age = input(f"\n{name}ning yoshini kirting: ")
    friends[name]=int(age)
    javob = input("\nYana ma'lumot qushasizmi? (ha/yoq) ")
    if javob=='yoq':
        ishora=False

for name, age in friends.items():
    print(f"{name.title()} {age} yoshda.")




cars = ['lacetti','nexia','toyota','nexia','audi','lacetti','malibu','nexia']
car='lacetti'
while car in cars:
    cars.remove(car)  
print(cars)



talabalar = ['Ali','Vali','Soli','Hasan','Husan','Maqsud']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba} baholandi.\n")
    baholangan_talabalar[talaba]=int(baho)
print(baholangan_talabalar)




####                            AMALIYOT

### 1

print("Assalom alaykum xayrli kun!")
zakas = []
while True:
    buyurtma = input("\nNima buyutrma qilasiz: ")
    zakas.append(buyurtma)
    savol = input('\nYana nimadir buyurtma qilasizmi? (ha/yoq) ')
    if savol == 'yoq':
        break
print(f"\nSizning buyutmalaringiz {zakas}")   
 


### 2

bozor = {}
ishora = True
while ishora:
    mahsulot = input('Mahsulot nomini kiriting: ')
    narx = input('{mahsulot.title()}ning narxini kiriting: ')
    bozor[mahsulot]=int(narx)
    savol = input("\nYana mahsulot qushasizmi? (ha/yoq) ")
    if savol == 'yoq':
        break
print(f"\nBizdagi mahsulotlarning narxlari\n{bozor}")



# ### 3 


buyurtmalar = ['olma','anor','nok','banan','uzum','tarvuz','quvun','bodring']
bozor = {'olma': 5000,
         'nok': 15000,
         'tarvuz': 15000,
         'bodring': 35000,
         'qovun': 14000,
         'banan':18000}
while buyurtmalar:
    buyurtma=buyurtmalar.pop()
    if buyurtma in bozor.keys():
        narx=bozor[buyurtma]
        print(f"{buyurtma.title()}-{narx} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yoq.")


























