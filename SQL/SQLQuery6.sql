---------PROSED�RLER-----------

--Create procedure Hareketler
--As 
--Select HareketId,�r�nAd,M�steriAd + ' '+M�steriSoyad as 'Bilgi',PersonelAdSoyad, Adet, Tutar, Tarih from TblHareket Inner join Tbl�r�nler
--on TblHareket.�r�n= Tbl�r�nler.�r�nId
--inner join TblM�steri on TblHareket.M�steri = TblM�steri.M�steriId
--inner join TblPersonel on TblHareket.Personel = TblPersonel.PersonelId 

--Execute Hareketler

--Create Procedure DENEME 
--as 
--select * from Tbl�r�nler where �r�nStok>10

--exec DENEME

--Drop procedure DENEME

--Alter Procedure �r�nGetir
--@Deger varchar(50) = 'Buzdolab�'
--as 
--select �r�nAd,�r�nStok,�r�nMarka from Tbl�r�nler where �r�nAd=@Deger
--execute  �r�nGetir @Deger = '�ama��r Makinesi'

-----------------DATE SORGULARI---------------

--select * from TblHareket where datepart (MONTH,Tarih) between 1 and 3
--select * from TblHareket where datepart (DAY,Tarih) between 14 and 30

--select DATENAME(MONTH,GETDATE()),DATENAME(DAY,GETDATE()),DATENAME(WEEKDAY,GETDATE())
--select datename(WEEKDAY,'2019.10.05')
--select DATEDIFF(year,'2016.10.18',GETDATE())
--select datediff(day,'2020.06.04',getdate())

--select dateadd(year,3,'2021.06.04')
--select DATEADD(day,45,'2021.06.04')

--------------ALTSORGU �RNEKLER�--------------

--select �r�nAd, count(*) from TblHareket
--inner join Tbl�r�nler on TblHareket.�r�n= Tbl�r�nler.�r�nId
--group by �r�nAd order by count(*) asc 

--select * from TblHareket where �r�n in (select �r�nId from Tbl�r�nler where Kategori=1)
--select * from TblHareket where M�steri in (select M�steriId from TblM�steri where M�steriSehir ='Ankara')
--select Sum(Tutar) from TblHareket where M�steri in (select M�steriId from TblM�steri where M�steriSehir= 'Ankara' or M�steriSehir = '�zmir')

--select * from TblHareket where �r�n=1

--Update Tbl�r�nler set �r�nStok= �r�nStok-(select sum(adet) from TblHareket where �r�n=6) where �r�nId=6

--Create Table Kasa
--(
--Toplam Decimal(18,2)
--)

--Insert into TblKasa Values(0)
--select * from TblKasa

--Update TblKasa Set Toplam = (Select Sum (Tutar) from TblHareket)

---------------------TET�KLEY�C�LER-----------

--create Table TblSayac
--(
--Islem int
--)
--insert into TblSayac Values(0)
--update TblSayac set Islem = (select count(*) from TblHareket)

--create Trigger IslemArt�s on TblHareket After insert as
--update TblSayac set Islem=Islem+1

--create Table TblToplamKategori
--(
--Adet tinyint
--)

--Update TblToplamKategori set Adet = (Select count(*) from TblKategori)

--create Trigger KategoriArt�s on TblKategori after Insert as
--Update TblToplamKategori Set Adet+=1 

--create trigger KategoriAzal�s on TblKategori after delete as
--update TblToplamKategori set Adet -=1













