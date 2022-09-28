"""
open(dosya_adı,dosya_erişme_kipi) 
w = write yani dosya oluşturan kiptir.
a = appened yani ekleme yapan kiptir.
r = read yani dosya okuyan kiptir.
r+ = hem okuma hem yazma yapar.
"""
file = open("Dosya_işlemleri_deneme" , "w")
print(file)

#file2 = open("C:/Kullanıcılar/ebedi/Masaüstü/bilgilerrr.txt","w",encoding = "utf-8") # çalıştırdığımızda masaüstünde bilgiler.txt oluşacaktır.
#file2.write("Harun Çetin") #dosyaya yazma işlemi yapar.
file = open("Dosya_işlemleri_deneme", "a") #appened yani ekleme yaptık.
print(file.write("Harunnnnn\n"))
print(file.write("Ebediiiii"))
file = open("Dosya_işlemleri_deneme" , "r") # for döngüsü ile dosya okuma.
for i in file:
    print(i)

file = open("Dosya_işlemleri_deneme" , "r") # read fonksiyonu ile içerik okuma.
icerik = file.read()
print("Dosya içeriği: ")
print(icerik)

file = open("Dosya_işlemleri_deneme" , "r") # satır satır okutur.
print(file.readline())

file = open("Dosya_işlemleri_deneme" , "r") # liste şeklinde okuma yapar.
liste = file.readlines()
print(liste)

#with open(dosya_adı, dosya_kipi) as file: Dosyayı otomatik oalrak kapatır. 
    #dosya işlemleri yapılır...

with open("Dosya_işlemleri_deneme" ,"r") as file:
    for i in file:
        print(i)

with open("Dosya_işlemleri_deneme" ,"r") as file:
    print(file.tell()) #Dosyanın hangi baytında olduğumuzu gösterir.
    file.seek(5) # Dosyanın hangi baytından başlayacağını yazıyoruz.

with open("Dosya_işlemleri_deneme" ,"r") as file:
    file.seek(3) # bu bayta git 
    icerikk = file.read(2) # ve bu bayt sayısı kadar oku.
    print(file.tell()) # hangi bayttayız? 3+2 = 5. bayttayız.
    print(icerikk)

with open("Dosya_işlemleri_deneme" ,"r+") as file:
    file.seek(4)
    file.write("Deneme")
    print(file.read())

with open("Dosya_işlemleri_deneme" ,"a") as file:
    file.write("Deneme\n") # Dosyaların sonunda değişiklik yapıyoruz.
with open("Dosya_işlemleri_deneme" ,"r+") as file:
    print(file.read())

with open("Dosya_işlemleri_deneme" ,"r+") as file:
    icerik3 =file.read()
    icerik3 = "BAŞLAGIÇ\n" +icerik3
    file.seek(0)
    file.write(icerik3)
with open("Dosya_işlemleri_deneme" ,"r+") as file:
    print(file.read())
with open("Dosya_işlemleri_deneme" ,"r+") as file:
    liste = file.readlines()
    liste.insert(2,"XXXyyyZZZ\n") #ikinci indekse " " içini ekledik.
    file.seek(0)
    for i in liste: #for yerine file.writelines(liste) yazarsak listemizi dosyaya yazdırmış oluruz.
        file.write(i)     
with open("Dosya_işlemleri_deneme" ,"r+") as file:
    print(file.read())


file.close()# Dosya kapatıldı.
