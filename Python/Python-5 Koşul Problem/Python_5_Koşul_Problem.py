# Boy ve kilo alarak kişinin vke hesapla ve sonuç bildir.
def main():
    Boy=float(input("Boyunuzu giriniz:"))
    Kilo=float(input("Kilonuzu giriniz:"))
    VKE = Kilo/(Boy*Boy)
    if (VKE<18.5):
        print("ZAYIFSINIZ.")
        print(VKE)
    elif(18.5<=VKE and VKE<25):
        print("İDEAL KİLODASINIZ.")
        print(VKE)
    elif(25<=VKE and VKE<30):
        print("AŞIRI KİLOLUSUNUZ.")
        print(VKE)
    else:
        print("OBEZSİNİZ.")
        print(VKE)

#Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
Sayı1=float(input("Sayı1'i giriniz:"))
Sayı2=float(input("Sayı2'i giriniz:"))
Sayı3=float(input("Sayı3'i giriniz:"))
if(Sayı1>Sayı2 and Sayı1>Sayı3):
    print("Sayı1 en büyüktür.")
elif(Sayı2>Sayı1 and Sayı2>Sayı3):
    print("Sayı2 en büyüktür.")
elif(Sayı3>Sayı1 and Sayı3>Sayı2):
    print("Sayı3 en büyüktür.")

# Şekili sor ve kenar uzunluklarını al sonra da alanını hesaplayalım.
Şekil= input("Hangi şekili seçeceksiniz?")
if(Şekil == "Üçgen"):
    Kenar1 = float(input("İlk kenarı giriniz: "))
    Kenar2 = float(input("İkinci kenarı giriniz: "))
    Kenar3 = float(input("Üçüncü kenarı giriniz: "))
    print("Üçgenin alanı= {}".format(Kenar1*Kenar2*Kenar3))
elif(Şekil == "Dikdötgen"):
    Kenar1 = float(input("İlk kenarı giriniz."))
    Kenar2 = float(input("İkinci kenarı giriniz."))
    print("Dikdörtgenin alanı= {}".format(Kenar1*Kenar2))
else:
    print("Tanımsız şekil girildi.")