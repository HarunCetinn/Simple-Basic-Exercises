def selamla(): #Parantez içine alacağı değerleri ekliyoruz.
    print("Merhaba...")
    print("Nasılsın?")
    print("Hamza")

selamla() #Fonsiyonumuzu çağırıyoruz.
 #  x==0
#for x in selamla():
   # x=+1  
    #if(x<4):
     #   break
def İsim(isminiz):
    print("İsminiz: ",isminiz)
İsim("Harun") #Harun ismi bir argümandır.
İsim("Ayşe")

def Toplam(a,b,c):
    print("Toplam değeri: ",a+b+c)
Toplam(2,3,5)

def Faktöriyel(sayi): #Fonksiyon tanımı
    faktöriyel = 1
    if(sayi ==0 or sayi ==1):
        print("Faktöriyel= ", faktöriyel)
    else:
        while(sayi>1):
            faktöriyel *=sayi
            sayi-=1
        print("Faktöriyel= ",faktöriyel)
Faktöriyel(5) #Fonksiyon çağrısı

def Topla(a,b,c):
    return a+b+c
def İkiyleÇarp(a):
    return a*2
toplamm=Topla(2,5,3) #Nesneyi fonksiyona gönderdik.
print(İkiyleÇarp(toplamm))

def üçleçarp(a):
    print("1.fonksiyon çalıştı")
    return a*3
def ikiyletopla(a):
    print("2.fonksiyon çalıştı")
    return a + 2
def dördeböl(a):
    print("3.fonksiyon çalıştı")
    return a / 4
# 3 ünü beraber kullanalım.
print(dördeböl(ikiyletopla(üçleçarp(3))))

def toplama(a,b,c):
    return a + b + c
    print("Toplama fonksiyonu") # Çalışmaz, returnden öne al.
#PARAMETRE TÜRLERİ
def Tanış(isim = "Harun"):
    print("Merhaba",isim)
Tanış() #Normalde boş parametre veremezdik isimi almamız gerekiyordu ama ilk başta değer atadık.
Tanış("Ali") #Biz yine de bir değer atarsak isim parametresi yernie yazılır.
def bilgilerigöster(ad = "Bilgi Yok",soyad = "Bilgi Yok",numara =  "Bilgi Yok"):
    print("Ad:",ad,"Soyad:",soyad,"Numara:",numara)
bilgilerigöster() # Bütün parametreler varsayılan değerle ekrana basılacak.
bilgilerigöster("Mustafa Murat","Coşkun") # ad ve soyad değerini verdik ancak numara parametresi varsayılan değer oldu. 

def Toplamaİşlemi(*a):
    toplam =0
    for i in a:
        toplam +=i
    print(toplam)
Toplamaİşlemi(1,2,3,4,5)


