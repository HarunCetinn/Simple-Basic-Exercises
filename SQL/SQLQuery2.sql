--Select Count(*) As 'Toplam Kay�t' from Tblogrenciler

--Select Sum(S�nav1),Sum(S�nav2),Sum(S�nav3) from TblNotlar
--Select AVG(S�nav1),Avg(S�nav2),Avg(S�nav3)from TblNotlar
--Select Max(S�nav2) from TblNotlar
--select min(s�nav1) from TblNotlar

--select ogrcinsiyet, Count(*) as 'Toplam' from Tblogrenciler group by ogrcinsiyet

--Select Durum, Count(*) as 'Durum' from TblNotlar where Ortalama>=50 group by Durum

--Select ogrkul�p,count(*) from Tblogrenciler group by ogrkul�p

--Select ogrsehir,count(*) from Tblogrenciler group by ogrsehir having count(*)=3

--Select * from Tblogrenciler where ograd like '%a%' or ograd like '%t%'

--select * from Tblogrenciler where ograd like 'a%'

--select distinct ogrsehir from Tblogrenciler

--select * from Tblogrenciler order by ograd 

--select distinct ogrsehir from Tblogrenciler order by ogrsehir desc

--Select * from Tblogrenciler where ograd like '%[A,�]%'

--select * from Tblogrenciler where ogrkul�p like '%[f-l]' 

--select top 5 * from Tblogrenciler 

--select * from Tblogrenciler where ogrsehir in('�stanbul', '�zmir')
--select * from TblNotlar where S�nav1 not in (60,65,70,75)

--select * from TblNotlar where s�nav1 between 60 and 75 
--select * from Tblogrenciler where ograd between 'a' and 'k'





