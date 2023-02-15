# 05-dars. STRING
# sana: 9/12/2022
# Muallifi: Maqsudkhan 


ism="фгволый"
matn='men yangi 📱 oldim'
smayl='😁'
#print(matn)

# STRING USTIDAAMALLAR

ism='Maqsud'
#print('Mening ismim ' + ism)
ism='Maqsud'
familiya='Torayev'
#print(ism+familiya)
#print(ism+ ' '+familiya)

# f-string

ism="Maqsud"
familiya="To'rayev"
ism_familiya=f"{ism} {familiya}"
#print(ism_familiya)
ism = 'James'
familiya='Bond'
#print(f"Salom, mening ismim {ism} , familiyam {familiya}")

# MAHSUS BELGILAR

#print("Hello World!")
#print("Hello \tWorld!")
#print("Hello \nWorld!")

# STRING METODLARI

ism = 'James'
familiya ='Bond'
ism_sharif = f"{ism} {familiya}"
#print(ism_sharif.upper()) # upper barcha harflarni katta harflarga o'zgartiradi
ism_sharif = ism_sharif.upper()

#print(ism_sharif.lower()) # lower barcha harflarni kichik harflarga o'zgartiradi
ism_sharif = ism_sharif.lower()

#print(ism_sharif.title()) # title Har bir so'zning 1-harfini katta harflarha o'zgartiradi
ism_sharif = ism_sharif.title()

#print(ism_sharif.capitalize()) # capitalize Matndagi so'zning faqat 1-harfini katta harfga o'zgartiradi
ism_sharif=ism_sharif.capitalize()


meva="     olma     "
#print(meva)
#print("Men " + meva.lstrip() + "ni yaxshi ko'raman") # lstrip chap tarafdagi bo'shliqni olib tashlaydi
#print("Men " + meva.rstrip() + "ni yaxshi ko'raman") # lstrip o'ng tarafdagi bo'shliqni olib tashlaydi
#print("Men " + meva.strip() + "ni yaxshi ko'raman") # strip ikala tarafdagi bo'shliqni olib tashlaydi

# INPUT

#ism = input("Ismingiz nima?")
#print("Assalom Alaykum," + ism)

#ism = input("Ismingiz nima?\n>>>") # isimni yangi qatordan yozish 
#print("Assalom alaykum, " + ism.title())


# AMALIYOT

kocha="Bog'bon"
mahalla="Sog'bon"
tuman="bodomzor"
viloyat="samarqand"

#print(f"{kocha} ko'chasi,{mahalla} \nmahallasi, {tuman} tumani, \n{viloyat} viloyati")



#kocha=input("Qayerda yashsaysiz?\nKo'cha >>>" )

#print(kocha +" ko'chasi, ")

#mahalla=input("mahalla ")

#print(mahalla + " mahallasi, ")

#tuman=input("tuman " )

#print(tuman + " tumani, ")

#viloyat=input("viloyat " )

#print(viloyat + " viloyati.")



yangi_manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"

print(yangi_manzil)

print(yangi_manzil.title())

print(yangi_manzil.upper())

print(yangi_manzil.lower())

print(yangi_manzil.capitalize())









