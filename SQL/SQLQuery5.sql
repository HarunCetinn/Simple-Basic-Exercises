--create database Sat��VT
--use Sat��VT
--create Table TblKategoriN
--(
--KategoriId tinyint identity(1,1) primary key,
--KategoriAd varchar(50)
--)
--Create Table Tbl�r�nler
--(
--�r�nId int identity(1,1) primary key,
--�r�nAd varchar(50),
--�r�nMarka varchar(50),
--Kategori tinyint,
--�r�nAl��Fiyat decimal(18,2),
--�r�nSat�sFiyat decimal(18,2),
--�r�nStok smallint check(�r�nStok>0),
--�r�nDurum bit default '1',
--)

--create Table TblPersonel
--(
--PersonelId smallint identity(1,1) primary key,
--PersonelAdSoyad Varchar(50)
--)

--Create table TblM�steri 
--(
--M�steriId int identity(1,1) primary key,
--M�steriAd varchar(50),
--M�steriSoyad varchar(50),
--M�steriSehir varchar(15),
--M�steriBakiye decimal(18,2)
--)

--Create Table TblHareket 
--(
--HareketId int primary key identity(1,1),
--�r�n int, 
--M�steri int,
--Personel smallint,
--Adet int,
--Tutar Decimal(18,2),
--Tarih smalldatetime,
--)

--Truncate Table Tbl�r�nler

--insert into TblKategori(KategoriAd) values('Bilgisayar')
--insert into TblKategori(KategoriAd) values('Koltuk Tak�m�')
--insert into TblKategori(KategoriAd) values('�ama��r Makinesi')
--insert into TblKategori(KategoriAd) values('Buzdolab�')

--insert into Tbl�r�nler(�r�nAd,�r�nMarka,Kategori,�r�nAl��Fiyat,�r�nSat�sFiyat,�r�nStok) values('Bilgisayar', 'Lenovo',1,2500,5000,200)

--SELECT * FROM Tbl�r�nler

--Update Tbl�r�nler set �r�nAd = 'Lcd' where �r�nAd = 'LED'

--select KategoriAd, count(*) from Tbl�r�nler inner join TblKategoriN
--on Tbl�r�nler.Kategori = TblKategoriN.KategoriId group by KategoriAd

--Update Tbl�r�nler set �r�nSat�sFiyat+=500 where Kategori=(select KategoriId from TblKategoriN where KategoriAd = 'Bilgisayar')
--select * from Tbl�r�nler







