--select upper('merhaba') as 'S�tun'

--select lower(ograd) as '��renci ad', upper(ogrsoyad) as '��renci Soyad' from Tblogrenciler

--select SUBSTRING(ograd,1,1)+ '.'+upper(ogrsoyad) as 'Ad Soyad' from Tblogrenciler
--Inner join TblKul�pler 
--on 
--Tblogrenciler.ogrkul�p = TblKul�pler.Kul�pid

--select left ('Merhaba d�nya',7), right('Merhaba �stanbul',8)
--select left (ograd,1)+'.'+left(ogrsoyad,15) from Tblogrenciler

--select DersAd�,avg(ortalama) from TblNotlar 
--inner join TblDersler
--on TblDersler.Dersid = TblNotlar.Ders
--group by DersAd�

--select ograd,Len(ograd) from Tblogrenciler

--select * from Tblogrenciler where len(ograd) = 4 or len(ograd)=3

--ltrim ve rtrim komutlar� sat�rdaki bo�luklar� siler

--select REPLACE('Harun �etin','harun �etin', 'H. �ET�N')
-- 1)Ana kelime 2)Bulunancak de�er 3)Yeni de�er
--select replace('Merhaba benim ad�m harun','a','e')

--select charindex('e','Sql derslerine devam',15)
--15. karakterden itibaren e harfini bul
--select CHARINDEX('a',ograd) as 'Karakter say�s�' from Tblogrenciler
--select reverse('anan')









