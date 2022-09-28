bool(-7.56) #Boolen değerler 0 harici bir değere sahipse true olur.
bool(0) #false olur.
print(1>5) #false yazar.
print(1<5) #true yazar.
a= None #Değer atanmadı.
print(a)
"""
== DEĞERLER BİRBİRİNE EŞİT İSE
!= DEĞERLER BİRBİRİNE EŞİT DEĞİLSE
> BÜYÜKTÜR
< KÜÇÜKTÜR
>= BÜYÜK EŞİTTİR
<= KÜÇÜK EŞİTTİR
"""
"MEHMET" == "MEHMET" #TRUE DÖNER
"ALİ" != "VELİ" #False döner. TRUE OLMASIN REYİZ?
a = 1>0 and "AYŞE" == "AYŞE" #Ve operatörü...
print(a)
b= 1>9 or "serdar" == "serdar" #Ya da operatörü
print(b)
c= not 2 ==2 #Tam tersine çıkarır, bu örnekte mesela false çıkar.
print(c)
##### İF ELSE ELİF #####
yaş = int(input("Yaşınızı giriniz."))
if(yaş<18):
    print("Ehliyet alamazsınız.")
else:    #ELSE VE ELİF BLOĞU TEK BAŞINA KULLANILAMAZ.
    print("Ehliyet alabilirsiniz.")
#Hesap makinesi yapıyorum.
Sayı1= int(input("Bir sayı giriniz."))
Sayı2 = int(input("İkinci sayıyı da giriniz."))
print("Toplama : + \nÇıkarma : - \nBölme : / \nÇarpma: *")
İşlem =input("İşlem seçiniz:")
if İşlem == "*":
    print("Sonuç = {}".format(Sayı1*Sayı2))
elif İşlem == "+":
     print("Sonuç = {}".format(Sayı1+Sayı2))
elif İşlem == "-":
     print("Sonuç = {}".format(Sayı1-Sayı2))
elif İşlem =="/":
    print("Sonuç = {}".format(Sayı1/Sayı2))
else:
    print("Tanımsız işlem türü seçildi.")
#İF blokları sağlanırsa direkt olarak çalışır ama elif ve else blokları üstündeki koşulu sorgular ve ona göre çalışır.
print("""*****************************
KULLANICI GİRİŞİ
**********************************""")
SYS_KullanıcıAdı= "Ebedi"
SYS_Parola = "12345"

KullanıcıAdı= input("Kullanıcı Adı: ")
Parola=input("Parola: ")
if (SYS_KullanıcıAdı == KullanıcıAdı and SYS_Parola == Parola):
    print("Giriş yapılıyor.")
else:
    print("Hatalı kullanıcı adı veya parola girildi.")






