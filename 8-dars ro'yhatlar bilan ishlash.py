# 14.12.2022
# 8-dars
# Muallif: Maqsudkhan

# TARTIBLASH

cars = ['bmw' , 'Mercedes benz' , "volvo" , 'general motors' , 'Tesla' , 'audi' , 'chevrolet cobol']
#cars.sort()
#print(cars)

#cars.sort(reverse=True)
#print(cars)


# # SORTED()

#print(sorted(cars)) #asl ruyhat o'zgarmadi
#print(sorted(cars , reverse=True))


# # SONLI RO'YHATLAR

ages = [15,45,23,7,-78 , 7.2 , 998,-7.5, 103]
#ages.sort()
#print(ages)
#print(sorted(ages , reverse=True))


# # RO'YHATNI ORTIDAN BOSHLAB CHIQARISH

fruits = ['olma' , 'olcha' , 'banan' , 'shaftoli' , 'xurmo' , 'anjir']
#fruits.reverse()
#print(fruits)


# # RO'YHAT UZUNLIGI

#print(len(cars))
#print(len(ages))
#print(len(fruits))


# # RANGE()

sonlar = list(range(0,11))
[#print(sonlar)



# # MAX() , MIN() , SUM()

narxlar = [12000 , 15000 , 9000  , 78000 , 3000 , 101000 , 120000]
arzon = min(narxlar)
qimmat = max(narxlar)
jami = sum(narxlar)
#print("Eng arzon narx" , arzon , "Eng qimmati" , qimmat , "Jami" , jami)


# # RO'YHATNI KESISH

cars = ['bmw' , 'Mercedes benz' , "volvo" , 'general motors' , 'Tesla' , 'audi' , 'chevrolet cobolt']
my_cars = cars[0:3] # 0-indeksdan boshlan 3 ta elementni ajratib chiqaradi
#print(my_cars)
#print(cars[2:5])
#print(cars[:4])
#print(cars[2:])


# # RO'HATDAN NUSXA OLISH

cars = ['bmw' , 'Mercedes benz' , "volvo" , 'general motors' , 'Tesla' , 'audi' , 'chevrolet cobolt']
#my_cars = cars
#print(cars)
#print(my_cars)
#my_cars.remove('volvo')
#print(my_cars)
#my_cars[0] = 'lasetti'
#print(my_cars)
#print(cars)

cars = ['bmw' , 'Mercedes benz' , "volvo" , 'general motors' , 'Tesla' , 'audi' , 'chevrolet cobolt']
my_cars = cars[:]
#print(my_cars)
my_cars.remove('volvo')
#print(my_cars)
#print(cars)


# # TUPLES

toys = ('car' , 'bus' , 'bear' , 'dino' , 'snake' , 'lizard')
#print(toys[0])
#print(toys[-1])
#print(toys[2:5])

toys = list(toys)

toys[2] = 'teddy'
print(toys)
toys.remove('dino')
print(toys)
toys.append('ball')
print(toys)

toys = tuple(toys)
print(toys)





