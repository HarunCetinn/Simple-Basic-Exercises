--select upper('merhaba') as 'Sütun'

--select lower(ograd) as 'Öðrenci ad', upper(ogrsoyad) as 'Öðrenci Soyad' from Tblogrenciler

--select SUBSTRING(ograd,1,1)+ '.'+upper(ogrsoyad) as 'Ad Soyad' from Tblogrenciler
--Inner join TblKulüpler 
--on 
--Tblogrenciler.ogrkulüp = TblKulüpler.Kulüpid

--select left ('Merhaba dünya',7), right('Merhaba Ýstanbul',8)
--select left (ograd,1)+'.'+left(ogrsoyad,15) from Tblogrenciler

--select DersAdý,avg(ortalama) from TblNotlar 
--inner join TblDersler
--on TblDersler.Dersid = TblNotlar.Ders
--group by DersAdý

--select ograd,Len(ograd) from Tblogrenciler

--select * from Tblogrenciler where len(ograd) = 4 or len(ograd)=3

--ltrim ve rtrim komutlarý satýrdaki boþluklarý siler

--select REPLACE('Harun çetin','harun çetin', 'H. ÇETÝN')
-- 1)Ana kelime 2)Bulunancak deðer 3)Yeni deðer
--select replace('Merhaba benim adým harun','a','e')

--select charindex('e','Sql derslerine devam',15)
--15. karakterden itibaren e harfini bul
--select CHARINDEX('a',ograd) as 'Karakter sayýsý' from Tblogrenciler
--select reverse('anan')









