a= 3+5 
print (a)

f = 3.2
b= 2.9
c=f+b
print(c)

r = 10
r *=3
print(r)

print("Burası da bir satırlık yorum satırı.")
"""
int değer ilk satırımız sonrasında float değerleri topladık.
Burası yorum satırı mı? EVET
"""
a= 4
b=5
a,b = b,a
print(a,b) #Burada da sayıların yerlerini değiştirdik.

4/2  #float bölmesi
4//2 #tam sayı bölmesi
4**2 #Üs bulma ; 4**0.5 der ise 4'ün karekökünü buluruz. ; 8**(1/3) =2 küp kök bulma 
13%2 #Mod bulma

'String yazmaları'
"String"
"""String """

L="ANAN"
print(L[0])
print(L[1])
print(L[2])
print(L[3])
print(L[-1])
print(L[-2])
print(L[-3])
print(L[-4])
"Önce normal şekilde stringi parçaladık sonra da tersten yazdırdık."

h ="Benim Adım Harun." # [başlama değeri : bitiş değeri : atlama değeri]
print(h[0:10]) #Boşluk index olarak sayılmıyor, 10 dahil edilmiyor.
print(h[10:16])
# 4.indeksten 12'nci indekse 3'er atlayarak stringi al.
print(h[4:12:3]) #md yazdı
# Başlangıç değeri belirtilmemişse en baştan başlayarak alır.
print(h[:10])
# Bitiş değeri belirtilmemişse en sonuna kadar alır.
print(h[4:])
# İki değer de belirtilmemişse tüm stringi al.
print(h[:])
#Son karaktere kadar al.
print(h[:-1]) 
# Baştan sona 2 değer atlaya atlaya stringi al.
print(h[::2])
# Baştan sona -1 atlayarak stringi al. (String'i ters çevirme)
print(h[::-1])
print(len(h))
#String nesneleri toplama işaretiyle birlikte yan yana eklenebilir, kendileri aralarında çarpılabilir.

x=59
print(float(x)) #Benzer şekilde float değerler de int değerlere dönüşür.
print(str(x)) #sanırım int değerini stringe çevirdim. Sanırım olmadı aeıydgıaeyds

u = "3.5689"
l = float(u)
print(l) #string değerler de int ve float değerlere dönüşebilirler.

print("Merhaba" , "benim" , "adım" , "harun") #Boşluklu yazar.
print("merhaba\nbenim\nadım\nharun") #Alt alta yazar.
print("Merhabalar\taq") #4 boşluk bırakır daha doğrusu 1 tab kadar.
type(34) # ya da içine string koy fark etmez tipini belirtir nesnenin.
print(25,63,59,25595,5614, sep = "/") #her bir değer arasına / işareti koyar.
print(*"Python") #Her karakter arası boşluk bırakır.
a = 3
b = 4
print("{} + {} 'nin toplamı {} 'dır".format(a,b,a+b)) #Süslü parantezlerin içindeki sayılar format fonksiyonun içinden hangi sıradaki değerin geleceğini söylüyor.
print("{1} {0} {2}".format(43,"Murat","Yaşında"))


