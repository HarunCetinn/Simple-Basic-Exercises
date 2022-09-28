--Select Count(*) As 'Toplam Kayýt' from Tblogrenciler

--Select Sum(Sýnav1),Sum(Sýnav2),Sum(Sýnav3) from TblNotlar
--Select AVG(Sýnav1),Avg(Sýnav2),Avg(Sýnav3)from TblNotlar
--Select Max(Sýnav2) from TblNotlar
--select min(sýnav1) from TblNotlar

--select ogrcinsiyet, Count(*) as 'Toplam' from Tblogrenciler group by ogrcinsiyet

--Select Durum, Count(*) as 'Durum' from TblNotlar where Ortalama>=50 group by Durum

--Select ogrkulüp,count(*) from Tblogrenciler group by ogrkulüp

--Select ogrsehir,count(*) from Tblogrenciler group by ogrsehir having count(*)=3

--Select * from Tblogrenciler where ograd like '%a%' or ograd like '%t%'

--select * from Tblogrenciler where ograd like 'a%'

--select distinct ogrsehir from Tblogrenciler

--select * from Tblogrenciler order by ograd 

--select distinct ogrsehir from Tblogrenciler order by ogrsehir desc

--Select * from Tblogrenciler where ograd like '%[A,Ý]%'

--select * from Tblogrenciler where ogrkulüp like '%[f-l]' 

--select top 5 * from Tblogrenciler 

--select * from Tblogrenciler where ogrsehir in('Ýstanbul', 'Ýzmir')
--select * from TblNotlar where Sýnav1 not in (60,65,70,75)

--select * from TblNotlar where sýnav1 between 60 and 75 
--select * from Tblogrenciler where ograd between 'a' and 'k'





