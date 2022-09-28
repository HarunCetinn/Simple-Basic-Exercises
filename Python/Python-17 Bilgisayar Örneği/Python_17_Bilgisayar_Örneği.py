import time
class Bilgisayar():
    def __init__(self,Pc_durum="Kapalı",Pc_Ses = 0,Programlar = ["Bilgisayarım", "İnternet","Çöp Kutusu", "Belgelerim"],):
        self.Pc_durum = Pc_durum
        self.Pc_Ses = Pc_Ses
        self.Programlar =Programlar

    def Ses_Ayarla(self):
        while True:
            karakter = input("Sesi azaltmak için: '<' Arttırmak için: '>' Çıkmak için: 'q' basın: ")
            if(karakter == "<"):
                if(self.Pc_Ses!=0):
                    self.Pc_Ses -=1
                    print("Ses:",self.Pc_Ses)
            elif(karakter == ">"):
                if(self.Pc_Ses!=100):
                    self.Pc_Ses +=1
                    print("Ses:",self.Pc_Ses)
            else:
                print("Ses güncellendi: ",self.Pc_Ses)
                break

    def Pc_Aç(self):
        time.sleep(3)
        print("Pc açılıyor...")
    def Pc_Kapat(self):
        time.sleep(1)
        print("Pc kapatılıyor...")
    def __str__(self):
        return "Pc durumu: {}\nSes{}\nProgramlar: {}\n".format(self.Pc_durum,self.Pc_Ses,self.Programlar)
    def __len__(self):
        return len(self.Programlar)

    def Program_Ekle(self,Program_İsmi):
        time.sleep(1)
        print("Program eklendi: ",Program_İsmi)
        self.Programlar.append(Program_İsmi)

Bilgisayar1 = Bilgisayar()
print("""
             LENOVO

1.PC AÇ

2.PC KAPAT

3.PC BİLGİLERİ

4.PROGRAM SAYISI

5.PROGRAM EKLE

6.SESİ AZALT YA DA ARTTIR
ÇIKMAK İÇİN 'q' BAS

""")

while True:
    işlem=input("İşlem seçiniz.")
    if(işlem=="1"):
        Bilgisayar1.Pc_Aç()
    elif(işlem=="2"):
        Bilgisayar1.Pc_Kapat()
    elif(işlem=="3"):
        print(Bilgisayar1)
    elif(işlem=="4"):
        print(len(Bilgisayar1))
    elif(işlem=="5"):
        EkProgram= input("Hangi programı eklemek istiyorsunuz?")
        Bilgisayar1.Program_Ekle(EkProgram)
    elif(işlem=="6"):
        Bilgisayar1.Ses_Ayarla()
    else:
        print("Geçersiz işlem...")

