---------PROSEDÜRLER-----------

--Create procedure Hareketler
--As 
--Select HareketId,ÜrünAd,MüsteriAd + ' '+MüsteriSoyad as 'Bilgi',PersonelAdSoyad, Adet, Tutar, Tarih from TblHareket Inner join TblÜrünler
--on TblHareket.Ürün= TblÜrünler.ÜrünId
--inner join TblMüsteri on TblHareket.Müsteri = TblMüsteri.MüsteriId
--inner join TblPersonel on TblHareket.Personel = TblPersonel.PersonelId 

--Execute Hareketler

--Create Procedure DENEME 
--as 
--select * from TblÜrünler where ÜrünStok>10

--exec DENEME

--Drop procedure DENEME

--Alter Procedure ÜrünGetir
--@Deger varchar(50) = 'Buzdolabý'
--as 
--select ÜrünAd,ÜrünStok,ÜrünMarka from TblÜrünler where ÜrünAd=@Deger
--execute  ÜrünGetir @Deger = 'Çamaþýr Makinesi'

-----------------DATE SORGULARI---------------

--select * from TblHareket where datepart (MONTH,Tarih) between 1 and 3
--select * from TblHareket where datepart (DAY,Tarih) between 14 and 30

--select DATENAME(MONTH,GETDATE()),DATENAME(DAY,GETDATE()),DATENAME(WEEKDAY,GETDATE())
--select datename(WEEKDAY,'2019.10.05')
--select DATEDIFF(year,'2016.10.18',GETDATE())
--select datediff(day,'2020.06.04',getdate())

--select dateadd(year,3,'2021.06.04')
--select DATEADD(day,45,'2021.06.04')

--------------ALTSORGU ÖRNEKLERÝ--------------

--select ÜrünAd, count(*) from TblHareket
--inner join TblÜrünler on TblHareket.Ürün= TblÜrünler.ÜrünId
--group by ÜrünAd order by count(*) asc 

--select * from TblHareket where Ürün in (select ÜrünId from TblÜrünler where Kategori=1)
--select * from TblHareket where Müsteri in (select MüsteriId from TblMüsteri where MüsteriSehir ='Ankara')
--select Sum(Tutar) from TblHareket where Müsteri in (select MüsteriId from TblMüsteri where MüsteriSehir= 'Ankara' or MüsteriSehir = 'Ýzmir')

--select * from TblHareket where Ürün=1

--Update TblÜrünler set ÜrünStok= ÜrünStok-(select sum(adet) from TblHareket where Ürün=6) where ÜrünId=6

--Create Table Kasa
--(
--Toplam Decimal(18,2)
--)

--Insert into TblKasa Values(0)
--select * from TblKasa

--Update TblKasa Set Toplam = (Select Sum (Tutar) from TblHareket)

---------------------TETÝKLEYÝCÝLER-----------

--create Table TblSayac
--(
--Islem int
--)
--insert into TblSayac Values(0)
--update TblSayac set Islem = (select count(*) from TblHareket)

--create Trigger IslemArtýs on TblHareket After insert as
--update TblSayac set Islem=Islem+1

--create Table TblToplamKategori
--(
--Adet tinyint
--)

--Update TblToplamKategori set Adet = (Select count(*) from TblKategori)

--create Trigger KategoriArtýs on TblKategori after Insert as
--Update TblToplamKategori Set Adet+=1 

--create trigger KategoriAzalýs on TblKategori after delete as
--update TblToplamKategori set Adet -=1













