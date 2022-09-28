class Araba():
    model = "Toyota corolla"
    renk="Beyaz"
    beygir_gücü = 110
    silindir = 4
    def __init__(self):
        print("init fonksiyonu çağırıldı.")

araba1 = Araba()
araba2 = Araba()
print(araba1.model)
print(araba2.model) # Aynı değerler olduğu için sınıfta init fonksiyonunu kullanmamız gerek.

class Bisiklet():
    def __init__(self,pedal,vites,tekerlek,yaş): #init i kullanırken böyle yapıyoruz.
        print("init fonksiyonu çağırıldı.")
        self.pedal = pedal
        self.vites = vites
        self.tekerlek= tekerlek
        self.yaş= yaş
bisiklet1 = Bisiklet(3, 12, 2, 5) #initteki yerlere sırası ile değer giriyoruz.
print(bisiklet1.pedal)
#METODLAR
class Yazılımcı():
    def __init__(self,isim,soyisim,maaş,numara,diller):
        self.isim= isim
        self.soyisim=soyisim
        self.maaş = maaş
        self.numara =numara
        self.diller= diller
    def BilgileriGöster(self):
        print("""
        Yazılımcı objesinin özellikleri;
        İsim: {}
        Soyisim: {}
        Maaş: {}
        Numara: {}
        Diller: {}
        """.format(self.isim,self.soyisim,self.maaş,self.numara,self.diller))
Yazılımcı1 = Yazılımcı("Harun", "Çetin", 195632,6500,["C#","Python"])
Yazılımcı1.BilgileriGöster()
#KALITIM
class Çalışan():
    def __init__(self,isim,maaş,departman):
        self.isim=isim
        self.maaş=maaş
        self.departman=departman
    def Bilgilergöster(self):
        print("İsim: {}\nMaaş: {}\nDepartman: {}\n".format(self.isim,self.maaş,self.departman))
    def DepartmanDeğiştir(self,yeni_departman):
        self.departman=yeni_departman
class Yönetici(Çalışan): #Çalışan sınıfından miras aldık.
   # pass #Sonradan tanımlanacak demektir.
   def ZamYap(self,ZamMiktarı):
        self.maaş +=ZamMiktarı
yönetici1 = Yönetici("Harun",5000,"Bilişim")
yönetici1.Bilgilergöster()
yönetici1.DepartmanDeğiştir("Robotik")
yönetici1.Bilgilergöster()   
yönetici1.ZamYap(1000)
yönetici1.Bilgilergöster()





