#FOR DÖNGÜSÜ
Liste = [1,2,3,4,5,6,7,8,9]
toplam=0
for eleman in Liste:
    toplam +=eleman
print(toplam)

Liste2 = [2,6,3,5,9,56,24,26,23,28,29]
for eleman in Liste2:
    if eleman %2 == 0:
        print(eleman)

A="Python" 
for i in A:
    print(i*3)
    #Bu örneklerde for döngüsüyle listelerde gezdik ve işlemler yaptık.
Demet=(1,2,3,5,6,9)
for b in Demet:
    print(b)

Liste3=[(1,2),(3,4),(5,6)]
for (i,j) in Liste3:
    print("i: {} ve j: {}".format(i,j))

Sözlük={"bir": 1 , "iki": 2, "üç": 3, "dört": 4}
print(Sözlük.keys())
print(Sözlük.values())
print(Sözlük.items())

#WHİLE DÖNGÜSÜ
i=0
while(i<10):
    print(i)
    i+=1

d=0
a="kalem"
while(d<7):
    print(a)
    d+=1 #Eğer d yi arttırmazsak sonsuz döngüye gireriz.

Liste4=[4,23,6,35,41]
index=0
while (index<len(Liste4)):
    print("İndex: ", index , "Liste elemanı: " , Liste4[index])
    index+=1

#RANGE FONKSİYONU 
print(*range(0,20)) #Liste yerine kullanılabilir.
print(*range(1,100,2)) #Atlama değeri de girdik.
print(*range(20,0,-1)) #geriye götürdük.
for x in range(1,100,5):
    print(x * "*")

#BREAK VE CONTİNUE 
i = 0
while (i<10):
    if(i==7):
        break
    print(i)
    i+=1
"""
m=0
while (m<8):
    if(m==3 or m == 7):
        continue
    print(m) #Alttaki işlemleri yaptırmaz ama pek kullanılmaz. While da sonsuz döngüye girer.
    m+=1
"""
#LİST COMPRASHİON...
liste1= [1,2,3,4,5]
liste2 = []
for i in liste1:
    liste2.append(i)
print(liste2)

liste3 =[1,2,3,6,9,8,10]
liste4=[i for i in liste3] #ÖNEMLİ
print(liste4)

listdemet= [(1,2,),(3,4),(5,6)]
listdemet2 =[i*j for i,j in listdemet]
print(listdemet2)

u ="Python"
listemm= [i * 5 for i in u]
print(listemm)

for i in listdemet: #List comp şeklinde ise 
    for x in i:  #listd = [x for i in listdemet for x in i] yazılır.
        print(x)