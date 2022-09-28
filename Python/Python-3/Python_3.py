#Kullanıcıdan 3 tane sayı alalım ve toplamlarını ekrana yazdıralım.

a = int(input("Birinci sayıyı giriniz."))
b = int(input("İkinci sayıyı giriniz."))
c = int(input("Üçüncü sayıyı giriniz."))
print("Sayıların toplamı:",a+b+c)

#Oyuncu kaydetme programı
ad=input("Oyuncunun ismi:")
soyad=input("Oyuncunun soyismi:")
takımı= input("Oyuncunun takımı:")

bilgiler=[ad,soyad,takımı]  
print("Bilgiler kaydediliyor...")
print("Oyuncuadı:{} \nOyuncu soyadı:{}\nOyuncu takımı:{}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))
print("Bilgiler kaydedildi.")

#İkinci dereceden bir bilinmeyenli denklem kökü bulma. :o
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
Delta = b**2-4*a*c
x1=(-b-Delta**0.5) / (2*a) #**0.5 karekökü alır.
x2=(-b+Delta**0.5) / (2*a)
print("Birinci kök:{}\nİkinci kök:{}".format(x1,x2))

#Kullanıcıdan alınan 3 sayıyı çarpıp ekrana yazdır.
a=int(input("Birinci sayıyı giriniz:"))
b=int(input("İkinci sayıyı giriniz:"))
c=int(input("Üçüncü sayıyı giriniz:"))
print("Çarpım sonucu = {}".format(a*b*c))

#Beden kitle endeksini bulma.
Boy=float(input("Boyunuzu giriniz:"))
Kilo=float(input("Kilonuzu giriniz:"))
print("Vücut kitle endeksiniz:{}".format(Kilo/(Boy*Boy)))

#Kilometrede ne kadar tutar harcadığı ve kaç kilometre yol gittiği alınan bir aracın masraflarını hesaplayalım.
KmBaşıTutar= float(input("Km başı harcanan tutar ="))
GidilenKm= float(input("Gidilen km miktarı ="))
print("Toplam yol masrafınız: {} TL".format(KmBaşıTutar*GidilenKm))

#Kullanıcıdan alınan iki sayının yerlerini değiştirelim ve ekrana yazdıralım.
a=int(input("Birinci sayıyı giriniz:"))
b=int(input("İkinci sayıyı giriniz:"))
a,b=b,a
print(a,b)

# Kullanıcıdan bir dik üçgenin iki kenarını alın ve hipotenüsü hesaplayın. 
a= int(input("Bir kenarı giriniz: "))
b= int(input("İkinci kenarı giriniz: "))
print("Hipotenüs= {}".format((a**2) + (b**2))
