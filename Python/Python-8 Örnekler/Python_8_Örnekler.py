#Kullanıcıdan bir sayı alalım ve onun mükemmel sayı olup olmadığını gösterelim.
Sayı = int(input("Sayı: "))
i = 1
toplam = 0 
while(i<Sayı):
    if(Sayı % i ==0):
        toplam +=i 
    i+=1
if(toplam == Sayı):
    print(Sayı, "Sayınız bir mükemmel sayıdır.")
else:
    print(Sayı, "Sayı mükemmel sayı değildir.")
#Çarpım tablosu yapalım.
for i in range(1,11):
    for j in range(1,11):
        print("{}x{} = {}".format(i,j,i*j))
#While döngüsüyle kullanıcıdan sayı alarak bunları toplayalım ta ki q tuşuna basana kadar.
toplam = 0
while True:
    Sayı = input("Sayı: ")
    if(Sayı == "q"):
        break
    Sayı = int(Sayı)
    toplam += Sayı
    print("Toplam= {}".format(toplam))
#1 den 100 e kadar olan ve 3 e tam bölünen sayıları ekrana yazdıralım.
for i in range(1,101):
    if(i%3 == 0):
       print(i)







