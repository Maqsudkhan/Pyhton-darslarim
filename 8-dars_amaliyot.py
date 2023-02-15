# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 08:28:51 2023

@author: User
"""
davlatlar=['Xitoy', 'amirica' , 'Korea' , 'yaponiya' , 'buyuk britaniya' , 'olmaniya' , 'rassia' , "o'zbekiston" , 'hindiston' , 'turkiya']

#print(len(davlatlar))

#print(sorted(davlatlar))
#print(sorted(davlatlar,reverse=True))

#print(davlatlar)
davlatlar.reverse()
#print(davlatlar)
davlatlar.sort()
#print("Alifbo boyicha \n>>>" , davlatlar)
davlatlar.sort(reverse=True)
#print("Alifboga teskari tartibda \n>>>" , davlatlar)

#juft_sonlar=list(range(120,1200,2))
#print("120 dan 1200 gacha juft sonlar yig'indisi:\n>>>" , sum(juft_sonlar))

#print("Eng katta va eng kichkina sonlar ayirmasi:\n>>>" , max(juft_sonlar) - min(juft_sonlar))

#print("Elementlar soni:\n>>>" , len(juft_sonlar))

#print("Boshidan 20 ta son:\n>>>" , juft_sonlar[:20]) 

#print("Oxoridan 20 ta son:\n>>>" , juft_sonlar[520:])

#print("O'rtasidan 20 ta son:\n>>>" , juft_sonlar[260:280])

taomlar=['osh','manti','tandir','shashlik','kabob','xonim','kasha'] 
nonushta=taomlar[:]
nonushta.remove('manti')
nonushta.remove('osh')
nonushta.remove('tandir')
nonushta.remove('xonim')

nonushta.append('tuxum')
nonushta.append('shurguruch')
nonushta.append("saryog'")

print(taomlar)


nonushta=tuple(nonushta)

nonushta[0]="non va qaymoq"

print(nonushta)























