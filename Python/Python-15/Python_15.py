#OVERRİDİNG (İPTAL ETME)   Metodlar üzerinde değişiklik yapmak için kullanılıyor.
#Python yukarıdan aşağıya okuduğu için kodları, alt tarafta yeni metod tanımlarsak üsttekileri iptal ederiz.
class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigoster(self):
        print("Çalışan sınıfının bilgileri.....")
        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman
 
class Yönetici(Çalışan):
    #Bir parametre daha eklemek için yeni bir init fonksiyonu hazırlarız.
    def __init__(self,isim,maaş,departman,kişi_sayısı): # Sorumlu olduğu kişi sayısı
        print("Yönetici sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
        self.kişi_sayısı = kişi_sayısı # Yeni eklenen özellik
    def bilgilerigoster(self): 
        print("Yönetici sınıfının bilgileri.....")
        print("İsim : {} \nMaaş: {} \nDepartman: {}\nSorumlu kişi sayısı: {}".format(self.isim,self.maaş,self.departman,self.kişi_sayısı))
    def zam_yap(self,zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı
a = Yönetici("Mustafa Murat Coşkun",3000,"Bilişim",10) # Yönetici sınıfının init fonksiyonu. Override edildi.
a.bilgilerigoster()
#SÜPER ANAHTAR --- Burada iptal edilen metodu da kullanmamızı sağlıyor.
# super().__init__(isim,maaş,departman) departman yazarsak yönetici sınıfında sadece kişi sayısını tanımlarız. Bu sayede daha az yük alırız.  

#ÖZEL METODLAR...
class Kitap():
    def __init__(self,isim,yazar,sayfa_sayisi,tür):
        print("İnit fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tür = tür
    def __str__(self): #Kendi string metodumuzu oluşturduk.
        return "isim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(self.isim,self.yazar,self.sayfa_sayisi,self.tür)
#kitap1 = Kitap() İnit metodu çağırılıyor.
#del kitap1 kitap1 objesini siler. 
kitap2 = Kitap("Nutuk","Mustafa Kemal ATATÜRK", 700, "Söylev")
print(kitap2)
#Del metodu override edilemez, sadece ekleme yapılır.





