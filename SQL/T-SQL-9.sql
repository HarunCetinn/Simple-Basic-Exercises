--Declare @Sayi int
--set @Sayi = 15
--select @Sayi as 'Sonu�'

--declare @kisi1 varchar(20)
--set @kisi1 ='Harun'
--select @kisi1 as 'Ki�i'

--declare @sayi1 int,@sayi2 int, @toplam int
--set @sayi1 = 12 
--set @sayi2 = 36
--set @toplam = @sayi1+@sayi2
--select @toplam as 'Toplam'

--declare @sayi int, @birler int, @onlar int, @y�zler int, @toplam int
--set @sayi = 456
--set @birler=@sayi%10
--set @onlar = (@sayi/10) %10
--set @y�zler = @sayi/100
--set @toplam = @birler + @onlar + @y�zler

--select @birler , @onlar ,@y�zler, @toplam

--use Sat��VT
--select * from TblM�steri
--declare @bakiye int
--set @bakiye =(select MAX(M�steriBakiye)from TblM�steri)
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
--insert into @kisiler (KisiAd, KisiSehir) values ('Harun','�stanbul')

--select * from @kisiler

--if(10<5)
--print('hi')
--else
--print('blabla')  pythondakinin ayn�s� gibi

--select �r�nAd, �r�nMarka, �r�nDurum = 
--case �r�nDurum
--when '1' then 'Stokta var'
--when '0' then 'Stokta yok'
--end
--from Tbl�r�nler

--select �r�nAd, �r�nMarka, �r�nStok, �r�nStok=
--case 
--when �r�nStok >=1 and �r�nStok<=5 then 'Acil takviye'
--when �r�nStok >=6 and �r�nStok<=10 then '�deal'
--when �r�nStok >=11 then '�r�n fazlas�'
--end
--from Tbl�r�nler

--declare @repeat int
--set @repeat =1
--while @repeat<=5
--begin print(@repeat)
--set @repeat+=1
--end

--waitfor delay '00:00:05'
--select * from Tbl�r�nler








