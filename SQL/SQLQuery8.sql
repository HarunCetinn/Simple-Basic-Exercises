-------------Northwind Denemeleri--------
--select * from Urunler

--select * from urunler where KategoriID=1

--select * from urunler where KategoriID=(select KategoriID from Kategoriler where KategoriAdi='Produce') and HedefStokDuzeyi>20
--or TedarikciID=(select TedarikciID from Tedarikciler where Adres='Paris')

--create view test1
--as
--select PersonelId,SirketAdi,Adi,SoyAdi,Unvan from Personeller
--inner join Musteriler on Personeller.PersonelID=Musteriler.MusteriID

--select * from Faturalar

select * from view_2





