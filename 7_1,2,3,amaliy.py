# 13/12/2022
# List (Ro'yhat)
# Muallif: Maqsudkhan


ismlar = ['Asad' , 'Asliddin' , 'Ramazon' , 'Shuhrat' , 'Dilshod']
#print('Salom' , ismlar[0] ,'qandaysiz yaxshimisiz?')
#print(ismlar[1] , 'bugun darsga boramizmi?')
#print('Bugun vaqtingiz qanday' , ismlar[2],'?')
#print('Assalom alaykum' , ismlar[3] , 'yaxshimisan jigar?')


sonlar = [17,20.5,23,45,-19,-25,10,12.5,-6.25]
#print(sonlar[1]+sonlar[4] - sonlar[6])
#print(sonlar[-1] - sonlar[3] * sonlar[0])
#print(sonlar[5] * sonlar[2] / sonlar[5])
#print(sonlar[6] / sonlar[7] + sonlar[2])

sonlar[4] = -15
sonlar[-1] = -17.25
sonlar[5] = 50
sonlar[3] = 35

#print(sonlar)


t_shaxslar = ['Ibn Sino' , 'Aleshir Navoiy' , 'Amir Temur' , 'Al-Xorazmiy']
z_shaxslar = ['Elon Musk' , 'Stiw Jobs' , 'Bell Gates' , 'Kara']

#print("Men tarixiy shaxslardan" , t_shaxslar.pop(2) , 'bilan, zamonaviy shaxslardan esa' , z_shaxslar.pop(3) , 'bilan suhbat qilishni istar edim!!!')


friends = []

friends.append('Dilshod')
friends.append('Asliddin')
friends.append('Asad')
friends.append('Shuhrat')
friends.append('Asilbek')
friends.append('Xondamir')
friends.append('Erajbek')

print('Opshe mehmonlar' , friends)

friends.remove('Erajbek')
friends.remove('Asad')

print('kelganlar' , friends)

friends.insert(0, 'Hasan')
friends.insert(3 , 'Anvar')
friends.insert(7 , 'Husan')

print('qushilganlar bilan opshesi' , friends)


mehmonlar = []


friends.pop(0)
friends.pop(0)
friends.pop(0)
friends.pop(0)
friends.pop(0)
friends.pop(0)

print(friends)

mehmonlar.append('Hasan')
mehmonlar.append('Dilshod')
mehmonlar.append('Asliddin')
mehmonlar.append('Anvar')
mehmonlar.append('Shuhrat')
mehmonlar.append('Asilbek')

print("Kelgan mehmonlar:" , mehmonlar)














