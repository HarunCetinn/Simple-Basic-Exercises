--Update Tblogrenciler set ogrkulüp= 1 where ogrkulüp='Futbol'
--Update Tblogrenciler set ogrkulüp= 2 where ogrkulüp='Basketbol'
--Update Tblogrenciler set ogrkulüp= 3 where ogrkulüp='Voleybol'
--Update Tblogrenciler set ogrkulüp= 4 where ogrkulüp='Tiyatro'
--Update Tblogrenciler set ogrkulüp= 5 where ogrkulüp='Satranç'

--select Notid,ograd+ ' '+ogrsoyad as 'Ad Soyad',DersAdý,Sýnav1,Sýnav2,Sýnav3,Ortalama,Durum from TblNotlar
--Inner join TblDersler
--on TblNotlar.Ders = TblDersler.Dersid
--inner join Tblogrenciler
--on TblNotlar.Ogrenci = Tblogrenciler.ogrid

--select * from TblNotlar where Ders = (select Dersid from TblDersler where DersAdý = 'Fizik')

--select * from TblNotlar
--left join Tblogrenciler
--on Tblogrenciler.ogrid = TblNotlar.Ogrenci

--select * from TblNotlar
--right join Tblogrenciler
--on Tblogrenciler.ogrid = TblNotlar.Ogrenci

--select * from TblNotlar
--full join Tblogrenciler
--on Tblogrenciler.ogrid = TblNotlar.Ogrenci

--select * from TblKulüpler Union Select * from TblDersler

--select * from TblNotlar
--select abs(-90) 
--select power(2,5)
--select sqrt(144)
--select floor(4.79)




