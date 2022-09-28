#Listeler

liste = [3,5,"a" , "elif" , "azra" ,3.45]  #Stringlerle aynı özellikleri taşır.
a = liste[2]
print(a)
type(liste)
b = liste[1:5:2] #1'den almadan başla sonrakini al, atla al (2 old. için), 5'i de alma.
print(b)
liste1 = [1,2,3]
liste2 = [4,5,6]
listetop = liste1+liste2
print(listetop)
liste2[1] = 8 # Stringlerden farklı olarak değiştirilebilir.
print(liste2)
liste2.append("Python") # Append metodu ile ekleme yaptık.
print(liste2)
liste2.pop() # Listenin sondaki elemanını siler. İçine hangi indexi girersen onu atar listeden.
print(liste2)
listetop.sort() # Küçükten büyüğe doğru listenin içindeki elemanları sıralar.
listeiç = [[1,2] , [5,6] , [7,8]] #içiçe listeler
f=listeiç[1][0]
print(listeiç)
print(f)

#Demetler(Tuplelar)        Listeler ve stringlerle benzer özellikler taşırlar.

demet=(4,3,2,6,8,9,75,5,3,4,6,2,56,23)
print(demet[5])
print(demet.count(3)) # Count metodu ile seçilen nesnenin demet içinde kaç defa geçtiğini buluruz.
print(demet.index(75)) #İndex metodu; aranılan değerin kaçıncı indexte olduğunu gösterir.

# Sözlükler                Anahtar değer ilişkisine sahiplerdir.
sözlük1 = {"bir" : 1 , "iki" : 2, "üç" : 3}
print(sözlük1["bir"]) #Sözlükteki bir elemana ulaştık.
sözlük1["dört"] = 4 #Sözlüğe bir eleman ekledik.
print(sözlük1)

a = {"bir" : [1,2,3,4], "iki": [[1,2],[3,4],[5,6]],"üç" : 15}
a["üç"]+=3
print(a["üç"])
print(a["iki"][1][1])

s={"sayılar" : {"bir" : 1 , "iki" : 2 , "üç" : 3} , "meyveler" :{"elma":"kış" , "armut":"sonbahar" , "ayva":"yaz" , "üzüm" : "bahar"}}  #iç içe diziler.
print(s["sayılar"]["iki"])
# Sözlük metodları
print(s.keys()) #Keyleri aldı sadece
print(s.values()) #Değerleri aldı sadece
print(s.items()) #Sözlükteki değerleri demetler olarak yazar.

#İnput, kullanıcıdan veri alma...
input()
a = input("Lütfen bir sayı giriniz:") #Bir değişkene atamamız gerekir.
print("Kullanıcının girdiği değer:",a) #Unutma ki değiştirmezsek string değer alır. int(input(...)) yapmamız gerek.



