

davlatlar = ["o'zbekiston"  , 'yaponiya' , 'korea' ,'kuba' , 'danya' , 'xitoy' , 'aqsh' , 'marokash' , 'berlin' , 'qatar' , 'arabiston' ]
#print(len(davlatlar)) # uzunligi

#print(sorted(davlatlar))

#print(sorted(davlatlar , reverse=True))

#print(davlatlar)

davlatlar.reverse()

#print(davlatlar)

davlatlar.sort()

#print(davlatlar)

davlatlar.sort(reverse = True)

#print(davlatlar)

juft_sonlar = list(range(120,1200,2))

#print(juft_sonlar)

yigindisi = sum(juft_sonlar)
#print(yigindisi)

katta = max(juft_sonlar)
kichik = min(juft_sonlar)
#print(katta-kichik)

soni = len(juft_sonlar)
#print(soni)

#print(juft_sonlar[:20])
#print(juft_sonlar[:20])
#print(juft_sonlar[260:280])

taomlar = ['mastava' , 'grechka' , 'lagmon' , 'shurva' , 'osh']
nonushta = taomlar[:]

nonushta.remove('osh')
nonushta.remove('lagmon')
nonushta.remove('grechka')
#print(nonushta)
nonushta.append('tuxum')
nonushta.append('kasha')

print(taomlar)
print(nonushta)

nonushta = tuple(nonushta)

nonushta[0] = "qaymoq va non"















