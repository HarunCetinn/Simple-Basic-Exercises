--Update Tblogrenciler set ogrkul�p= 1 where ogrkul�p='Futbol'
--Update Tblogrenciler set ogrkul�p= 2 where ogrkul�p='Basketbol'
--Update Tblogrenciler set ogrkul�p= 3 where ogrkul�p='Voleybol'
--Update Tblogrenciler set ogrkul�p= 4 where ogrkul�p='Tiyatro'
--Update Tblogrenciler set ogrkul�p= 5 where ogrkul�p='Satran�'

--select Notid,ograd+ ' '+ogrsoyad as 'Ad Soyad',DersAd�,S�nav1,S�nav2,S�nav3,Ortalama,Durum from TblNotlar
--Inner join TblDersler
--on TblNotlar.Ders = TblDersler.Dersid
--inner join Tblogrenciler
--on TblNotlar.Ogrenci = Tblogrenciler.ogrid

--select * from TblNotlar where Ders = (select Dersid from TblDersler where DersAd� = 'Fizik')

--select * from TblNotlar
--left join Tblogrenciler
--on Tblogrenciler.ogrid = TblNotlar.Ogrenci

--select * from TblNotlar
--right join Tblogrenciler
--on Tblogrenciler.ogrid = TblNotlar.Ogrenci

--select * from TblNotlar
--full join Tblogrenciler
--on Tblogrenciler.ogrid = TblNotlar.Ogrenci

--select * from TblKul�pler Union Select * from TblDersler

--select * from TblNotlar
--select abs(-90) 
--select power(2,5)
--select sqrt(144)
--select floor(4.79)




