def fonk():
    a =10
    print(a)
fonk() #Yerel değişkeni kullanarak yazdırdık 10 sayısını.
# print(a) Burada hata verir çünkü a değişkeni yerel bir değişkendir.
b=5 #Global bir değişken olduğu için rahatlıkla kullanılabilir.
def fonk2():
    print(b)
fonk2()

c= 10
def fonk3():
    c=2 #İki c değeri var biri yerel biri global.
    print(c) #İkiyi basar.
fonk3()
print(c) #Globaldeki c değerini basar.

d= 7 
def fonk4():
    global d #Globaldeki d değerini kullandı.
    d= 3 #Bu iki satırla globaldeki değeri değiştirdik.
    print(d)
fonk4()
print(d)
#İF VE WHİLE GİBİ ŞEYLERİN İÇİNDE TANIMLANAN NESNELER DE GLOBAL NESNEDİR.

ikiyleçarp = lambda x : x*2 #x*2 return ediyor gibi, fonk gibi işliyor.
print(ikiyleçarp(3)) #Fonksiyon ile aynı işlemi yapıyor.

Toplama = lambda a,b,c : a+b+c
print(Toplama(3,5,7))

Tersçevir = lambda s:s[::-1]
print(Tersçevir("KALP"))

Çiftsorgu=lambda sayı: sayı %2==0
print(Çiftsorgu(13)) #True false cevabını verdirdik.