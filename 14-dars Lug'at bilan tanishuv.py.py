"""
Bismillahir Rohmanir Rohim
"""


"""
car_0={'model':'ferrari','rangi':'qizil','yili':'2023','ot kuchi':'925 ta'}
print(f"{car_0['model'].title()},\
   {car_0['rangi'].title()}-rangli,\
   {car_0['yili'].title()}-yil,\
   {car_0['ot kuchi']} ot kuchi!")
car_0['tezligi']='1200km/s'
car_0['matori']=4.8
print(car_0)




talaba={}
talaba['ism']='maqsusd to\'rayev'
talaba['kurs']=3
talaba['yosh']=20
print(talaba)
talaba['kurs']=4
print(f"Talaba {talaba['ism'].title()} {talaba['kurs']}-kursda o'qiyda va hozirda {talaba['yosh']} yoshda.")
del talaba['yosh']
print(talaba)




phons = {
    'Ali':'Iphone x' ,
    'Vali':'Galaxy S10',
    'Shuhrat':'Samsung A52',
    'Asad':'Samsung A51',
    'Dilshod':'Mi 10 pro',
    'Asilbek':'Iphone 14 pro max'
    }

print(f"Alining telefoni {phons['Ali']}")
print(phons.get('Hasan','Bunday ism mavjud emas.'))
 """



#                                AMALIYOT
"""
onam ={'ismi':'Jumagul','tugulgan_yil':'1977','shahri':'qashqadaryo'}
akam = {'ismi':'Muhammad','tugulgan_yil':'1999','shahri':'qashqadaryo'}
akam_2 = {'ismi':'Mahmud','tugulgan_yil':'2001','shahri':'qashqadaryo'}

print(f"Onamning ismi {onam['ismi']},\
 {onam['tugulgan_yil']}-yilda,\
 {onam['shahri'].title()} viloyatida tug'ilgan." )

print(f"Akamning ismi {akam['ismi']},\
 {akam['tugulgan_yil']}-yilda,\
 {akam['shahri'].title()} viloyatida tug'ilgan ")

print(f"Ikkinchi akamning ismi {akam_2['ismi']},\
 {akam_2['tugulgan_yil']}-yilda,\
 {akam_2['shahri'].title()} viloyatida tug'ilgan.")





taom = {'Onam':'honim','akam':'osh','akam_2':'kabob','ukam':'shurva',"ozim":'dimlama.'}
print(f"Onamning sevimli taomi {taom['Onam']},\
 Akamnini sevimli taomi {taom['akam']},\
 Ikkinchi akamning sevimli taomi {taom['akam_2']},\
 Ukamning sevimli taomi {taom['ukam']},\
 Mening sevimli taomim {taom['ozim']}")
"""




lugat={'integer':'butun son',
       'float':"o'nlik son",
       'string':'matn',
       'if':'agar',
       'else':'boshqa',
       'list':"ro'yxat",
       'tuple':"o'zgarmas ro'yxat"

       }

soz=input('Kalit s\'oz kiriting: ').lower()
#print(lugat.get(soz,"Bunday so'z mavjud emas" ))

tarjima=lugat.get(soz)

if tarjima==None:
    print("Bunday so'z mavjud emas!")
else:
    print(f"{soz} sozi {tarjima} deb tarjima qilinadi!")
















