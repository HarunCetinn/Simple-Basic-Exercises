#Kullanıcı girişi programı
true_kullanıcıadi = "Ebedi"
true_parola= "123456"
girişhakkı = 3
while True:
    Kullanıcı_Adı = input("Kullanıcı Adı: ") 
    Parola = input("Parola: ")
    if(girişhakkı!=0):
        if(Kullanıcı_Adı ==true_kullanıcıadi or Parola == true_parola):
            print("Giriş Yapılıyor...")
            break
        else: 
            print("Kullanıcı adı veya parola yanlış. ")
            girişhakkı -=1
    else:
        print("Giriş Hakkınız Kalmadı.")
        break

#ATM MAKİNESİ PROGRAMI
print("""**************************
1.BAKİYE SORGULAMA

2.PARA YATIRMA

3.PARA ÇEKME

ÇIKIŞ İÇİN X'E BASIN
********************************""")
Bakiye = 1000

while True:
    işlem = input("İşlemi giriniz.")

    if(işlem == "X"):
        print("Çıkış Yapılıyor.")
        break
    elif(işlem == "1"):
        print("Bakiyeniz: {} tl dir.".format(Bakiye))
    elif(işlem=="2"):
        miktar= int(input("Miktarı giriniz."))
        Bakiye += miktar
    elif(işlem == "3"):
        miktar =int(input("Miktarı giriniz."))
        if(Bakiye<miktar):
            print("Bakiyeniz yok.")
            continue
        Bakiye -= miktar
    else:
        print("Geçersiz işlem...")

#Faktöriyel bulma programı
while True:
    Sayı =input("Sayı: ")
    if(Sayı == "q"):
        print("Program sonlandırılıyor.")
        break
    else: 
        Sayı = int(Sayı)
        faktöriyel = 1
        for i in range(2,Sayı+1):
            faktöriyel *=i
            print("Faktöriyel = {}".format(faktöriyel))
#Fibonacci serisi oluşturalım.
a=1
b=1
fibonacci = [a,b]
for i in range(20):
    a,b = b,a+b
    fibonacci.append(b)
print(fibonacci)





