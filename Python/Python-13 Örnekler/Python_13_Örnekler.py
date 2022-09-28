# Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirmeye çalışın.
import math
def Toplama(a,b):
    return a+b
def Çıkarma (a,b):
    return a-b
def Çarpma(a,b):
    return a*b
def Bölme(a,b):
    return a/b
def Faktöriyel(x):
    return math.factorial(x)
def Üslü(a,b):
    return a**b
def Karekök(x):
    return x**0.5

print(""" 
1.TOPLAMA
2.ÇIKARMA
3.ÇARPMA
4.BÖLME
5.FAKTÖRİYEL
6.ÜSLÜ ALMA
7.KAREKÖKE ALMA
""")
İslemsayisi = int(input("Bir işlem sayısı seçiniz:"))
if(İslemsayisi==1):
    a = int(input("İlk sayıyı giriniz:"))
    b= int(input("İkinci sayıyı giriniz:"))
    print("Sonuç= ", a+b)
elif(İslemsayisi==2):
    a = int(input("İlk sayıyı giriniz:"))
    b= int(input("İkinci sayıyı giriniz:"))
    print("Sonuç= ", a-b)
elif(İslemsayisi==3):
    a = int(input("İlk sayıyı giriniz:"))
    b= int(input("İkinci sayıyı giriniz:"))
    print("Sonuç= ", a*b)
elif(İslemsayisi==4):
    a = int(input("İlk sayıyı giriniz:"))
    b= int(input("İkinci sayıyı giriniz:"))
    print("Sonuç= ", a/b)
elif(İslemsayisi==5):
    x = int(input("Sayıyı giriniz:"))
    print("Sonuç= ",Faktöriyel(x))
elif(İslemsayisi==6):
    a = int(input("İlk sayıyı giriniz:"))
    b= int(input("İkinci sayıyı giriniz:"))
    print("Sonuç= ", a**b)
elif(İslemsayisi==7):
    a = int(input("İlk sayıyı giriniz:"))
    print("Sonuç= ", a**0.5)
else:
    print("Hatalı sayı girdiniz.")