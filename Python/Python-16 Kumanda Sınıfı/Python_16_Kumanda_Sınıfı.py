import random
import time
class Kumanda():
    def __init__(self,tv_durum = "Kapalı", tv_ses = 0, tv_KanalListesi = ["TRT"], kanal = "TRT"):
        self.tv_durum =tv_durum
        self.tv_ses = tv_ses
        self.tv_KanalListesi =tv_KanalListesi
        self.kanal = kanal

    def Tv_Aç(self):
        if(self.tv_durum == "Açık"):
            print("Tv açık...")
        else:
            print("Tv açılıyor...")

    def Tv_Kapat(self):
        if(self.tv_durum =="Kapalı"):
            print("Tv kapalı...")
        else:
            print("Tv kapatılıyor...")

    def Ses_Ayarları(self):
        while True:
            cevap = input("Sesi azaltmak için '<' Arttırmak için '>' basınız, çıkmak için 'q' basınız.")
            if(cevap == "<"):
                if(self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)
            elif(cevap == ">"):
                if(self.tv_ses !=100):
                    self.tv_ses +=1
                    print("Ses", self.tv_ses)
            else:
                print("Ses Güncellendi:",self.tv_ses)
                break

    def Kanal_Ekle(self,Kanal_İsmi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.tv_KanalListesi.append(Kanal_İsmi)
        print("Kanal eklendi.")

    def Rastgele_Kanal(self):
        rnd = random.randint(0,len(self.tv_KanalListesi)-1)
        self.kanal = self.tv_KanalListesi[rnd]
        print("Kanal = ",self.kanal)

    def __len__(self):
        return len(self.tv_KanalListesi)
    def __str__(self):
        return "Tv durumu: {}\nTv ses: {}\nKanal listesi {}\nŞu anki kanal: {}\n".format(self.tv_durum,self.tv_ses,self.tv_KanalListesi,self.kanal)

kumanda = Kumanda()
print("""
                TV UYGULAMASI
1.TV AÇ

2.TV KAPAT

3.SES AYARLARI

4.KANAL EKLE

5.KANAL SAYISI ÖĞRENME

6.RASTGELE KANAL

7.TV BİLGİLERİ

ÇIKMAK İÇİN 'q' BASIN
""")

while True:
    işlem = input("İşleminizi seçiniz:")
    if(işlem == "1"):
        kumanda.Tv_Aç()
    elif(işlem=="2"):
        kumanda.Tv_Kapat()
    elif(işlem=="3"):
        kumanda.Ses_Ayarları()
    elif(işlem =="4"):
        kanal = input("Eklemek istediğiniz kanalı giriniz:")
        kumanda.Kanal_Ekle(kanal)

    elif(işlem =="5"):
        print("Kanal sayısı: ",len(kumanda))
    elif(işlem == "6"):
        kumanda.Rastgele_Kanal()
    elif(işlem=="7"):
        print("Tv bilgileri: ", kumanda)
    elif(işlem == "q"):
        print("İşlem sonlandırılıyor...")
        break
    else:
        print("Geçersiz işlem...")
