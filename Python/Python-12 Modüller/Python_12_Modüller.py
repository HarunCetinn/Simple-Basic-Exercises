import math # math modülünü programa ekledik.
dir(math)
# help(math) bütün özelliklerini gösterdi. 
a =math.factorial(5)
print(a)
math.floor(5.6) #Aşağı yuvarlar
math.ceil(5.6) #Yukarı yuvarlar
import math as matematik # Burada math modulünü matematik ismiyle kullanacağımızı belirttik.
b= matematik.factorial(4)
print(b)
from math import * #Math modulü içindeki her fonksiyonu dahil ederiz bu şekilde.
c= factorial(6) # Bu yöntemle modül adını her zaman yazmamıza gerek kalmıyor. Sadece fonksiyonun ismini yazmamız yeterli.
print(c)
# from math import floor,ceil = sadece iki fonksiyonu aldırır.
import random
import time
print("""*************
SAYI TAHMİN OYUNU
 1 İLE 40 ARASINDAKİ SAYIYI TAHMİN EDİNİZ.
*******************""")
rastgelesayi= random.randint(1,40)
tahminhakki= 5
while True:
    tahmin = int(input("Tahmininiz= "))
    if(tahmin<rastgelesayi):
        print("Bilgiler karşılaştırılıyor.")
        time.sleep(1) #1 Saniye bekletiyor bizi.
        print("Daha yüksek bir sayı giriniz.")
        tahminhakki-=1
    elif(tahmin>rastgelesayi):
        print("Bilgiler karşılaştırılıyor.")
        time.sleep(1)
        print("Daha düşük bir sayı giriniz.")
        tahminhakki-=1
    else:
        print("Bilgiler karşılaştırılıyor.")
        time.sleep(1)
        print("Tebrikler...")
        break
    if(tahminhakki<=0):
        print("Tahmin hakkınız kalmadı.")
        print("Sayı= ",rastgelesayi)
        break