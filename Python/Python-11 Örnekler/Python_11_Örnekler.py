#Asal sayı bulalım.
def asal_mi(sayi):
    if(sayi<=1):
        return False
    elif(sayi==2):
        return True
    else:
        for i in range(2,sayi):
            if(sayi %i== 0):
                return False
        return True
while True:
    sayi= input("Sayıyı giriniz: ")
    if(sayi == "q"):
        break
    else:
        sayi = int(sayi)
        if(asal_mi(sayi)):
            print(sayi,"Sayısı asaldır. ")
        else:
            print(sayi, "Sayısı asal sayı değildir.")
# Bir sayının tam bölenlerini bulalım.
def tambölenleribul(sayi2):
    tambölenler = []
    for i in range(2,sayi2):
        if(sayi2 %i == 0):
            tambölenler.append(i)
    return tambölenler
while True:
    sayi2 =input("Sayı: ")
    if(sayi2== "q"):
        print("Program sonlandırılıyor...")
        break
    else:
        print("Tam bölenler= ",tambölenleribul(sayi))
#Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
def Okunus(Sayi):
    birinci = Sayi %10
    ikinci = Sayi//10 # Tam sayı bölmesi
    return onlar[ikinci] + " " + birler[birinci]
Sayi = int(input("Lütfen iki basamaklı bir sayı giriniz: "))
print(Okunus(Sayi))
#Kullanıcıdan istediği kadar sayı alalım ve tek ve çift sayıların ortalamasını alalım.
tekAdet= 0
çiftAdet= 0
tekToplam= 0
çiftToplam =0 
n = int(input("Kaç adet sayı gireceksiniz?"))
for i in range(n):
    Sayi3= int(input("Sayı= "))
    if(Sayi3%2==0):
        çiftAdet+=1
        çiftToplam +=Sayi3
    else:
        tekAdet +=1
        tekToplam += Sayi3
if(tekAdet!=0):
    print("Tek sayı ortalaması= ",tekToplam/tekAdet)
if(çiftAdet!=0):
    print("Çift sayı ortalaması= ",çiftToplam/çiftAdet)
print("Çift sayılar= ",çiftAdet)
print("Tek sayılar= ",tekAdet)
#Python ile bir liste içinde 5’in katları olan sayıları listeleme.
Liste=[16,15,25,36,95,64,38,564,68531,15,67,99,34]
sayac= 0
for i in Liste:
    if(i%5==0):
        sayac +=1
        print("{0} Saysısı 5 in katıdır.".format(i))
else:
    print("Döngü bitti.")
    print("5'in katı olan sayıların adedi={0} " .format(sayac))
#Fonksiyon kullanarak dairenin alanını hesaplayalım.
def AlanHesapla(Yariçap):
    alan= 3.14*float(Yariçap)*float(Yariçap)
    print("Alan= ",alan)
    return alan
r=input("Yarıçapı giriniz: ")
AlanHesapla(r)
#Maaş ve zam oranı kullanıcıdan alınan işçinin yeni maaşını hesaplayalım.
yeniMaaş= 0
def MaaşHesapla(Maaş,ZamOranı):
    yeniMaaş =int(Maaş) + (int(Maaş) * int(ZamOranı)/100)
    print("Zamlı maaş= ", yeniMaaş)
    return yeniMaaş
Maaş= input("Maaşınzı giriniz: ")
ZamOranı= input("Zam oranınızı giriniz: ")
MaaşHesapla(Maaş, ZamOranı)
#1'den kullanıcının girdiği sayıya kadar olan tek ve çift sayıları ayrı ayrı toplayalım.
sınırsayi=input("Sayı: ")
TekToplam=0
ÇiftToplam=0
for i in range(1,int(sınırsayi)):
    if(i%2== 0):
        ÇiftToplam +=i
    else:
        TekToplam +=i
print("Tek toplam= {0}".format(TekToplam))
print("Çift toplam= {0}".format(ÇiftToplam))
#Girilen sayının asallığını kontrol edelim.
sayac= 0
for i in range(2,int(sayi)):
      if(int(sayi)%i==0):
            sayac+=1
            break
if(sayac!=0):
      print("Sayı Asal Değil")
else:
      print("Sayı Asal")
 