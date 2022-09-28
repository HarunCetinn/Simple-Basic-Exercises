--Declare @Sayi int
--set @Sayi = 15
--select @Sayi as 'Sonuç'

--declare @kisi1 varchar(20)
--set @kisi1 ='Harun'
--select @kisi1 as 'Kiþi'

--declare @sayi1 int,@sayi2 int, @toplam int
--set @sayi1 = 12 
--set @sayi2 = 36
--set @toplam = @sayi1+@sayi2
--select @toplam as 'Toplam'

--declare @sayi int, @birler int, @onlar int, @yüzler int, @toplam int
--set @sayi = 456
--set @birler=@sayi%10
--set @onlar = (@sayi/10) %10
--set @yüzler = @sayi/100
--set @toplam = @birler + @onlar + @yüzler

--select @birler , @onlar ,@yüzler, @toplam

--use SatýþVT
--select * from TblMüsteri
--declare @bakiye int
--set @bakiye =(select MAX(MüsteriBakiye)from TblMüsteri)
--select @bakiye

--select @@SERVERNAME, @@VERSION

--print'Selam'
--print'**************'

--Declare @kisiler table 
--(
--KisiID int identity(1,1),
--KisiAd varchar(10),
--KisiSehir varchar(15)
--)
--insert into @kisiler (KisiAd, KisiSehir) values ('Harun','Ýstanbul')

--select * from @kisiler

--if(10<5)
--print('hi')
--else
--print('blabla')  pythondakinin aynýsý gibi

--select ÜrünAd, ÜrünMarka, ÜrünDurum = 
--case ÜrünDurum
--when '1' then 'Stokta var'
--when '0' then 'Stokta yok'
--end
--from TblÜrünler

--select ÜrünAd, ÜrünMarka, ÜrünStok, ÜrünStok=
--case 
--when ÜrünStok >=1 and ÜrünStok<=5 then 'Acil takviye'
--when ÜrünStok >=6 and ÜrünStok<=10 then 'Ýdeal'
--when ÜrünStok >=11 then 'Ürün fazlasý'
--end
--from TblÜrünler

--declare @repeat int
--set @repeat =1
--while @repeat<=5
--begin print(@repeat)
--set @repeat+=1
--end

--waitfor delay '00:00:05'
--select * from TblÜrünler








