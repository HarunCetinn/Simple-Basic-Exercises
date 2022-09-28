--create database SatýþVT
--use SatýþVT
--create Table TblKategoriN
--(
--KategoriId tinyint identity(1,1) primary key,
--KategoriAd varchar(50)
--)
--Create Table TblÜrünler
--(
--ÜrünId int identity(1,1) primary key,
--ÜrünAd varchar(50),
--ÜrünMarka varchar(50),
--Kategori tinyint,
--ÜrünAlýþFiyat decimal(18,2),
--ÜrünSatýsFiyat decimal(18,2),
--ÜrünStok smallint check(ÜrünStok>0),
--ÜrünDurum bit default '1',
--)

--create Table TblPersonel
--(
--PersonelId smallint identity(1,1) primary key,
--PersonelAdSoyad Varchar(50)
--)

--Create table TblMüsteri 
--(
--MüsteriId int identity(1,1) primary key,
--MüsteriAd varchar(50),
--MüsteriSoyad varchar(50),
--MüsteriSehir varchar(15),
--MüsteriBakiye decimal(18,2)
--)

--Create Table TblHareket 
--(
--HareketId int primary key identity(1,1),
--Ürün int, 
--Müsteri int,
--Personel smallint,
--Adet int,
--Tutar Decimal(18,2),
--Tarih smalldatetime,
--)

--Truncate Table TblÜrünler

--insert into TblKategori(KategoriAd) values('Bilgisayar')
--insert into TblKategori(KategoriAd) values('Koltuk Takýmý')
--insert into TblKategori(KategoriAd) values('Çamaþýr Makinesi')
--insert into TblKategori(KategoriAd) values('Buzdolabý')

--insert into TblÜrünler(ÜrünAd,ÜrünMarka,Kategori,ÜrünAlýþFiyat,ÜrünSatýsFiyat,ÜrünStok) values('Bilgisayar', 'Lenovo',1,2500,5000,200)

--SELECT * FROM TblÜrünler

--Update TblÜrünler set ÜrünAd = 'Lcd' where ÜrünAd = 'LED'

--select KategoriAd, count(*) from TblÜrünler inner join TblKategoriN
--on TblÜrünler.Kategori = TblKategoriN.KategoriId group by KategoriAd

--Update TblÜrünler set ÜrünSatýsFiyat+=500 where Kategori=(select KategoriId from TblKategoriN where KategoriAd = 'Bilgisayar')
--select * from TblÜrünler







