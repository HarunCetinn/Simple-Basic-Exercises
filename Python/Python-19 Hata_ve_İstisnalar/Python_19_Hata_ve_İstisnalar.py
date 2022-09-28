def main():

#try: 
  #  Hata çıkarabilecek kodlar buraya yazılıyor.
 #   Eğer hata çıkarsa program uygun olan except bloğuna girecek.
#    Hata oluşursa try bloğunun geri kalanındaki işlemler çalışmayacak.
#except Hata1:
#    Hata1 oluştuğunda burası çalışacak.
#except Hata2:
#    Hata2 oluştuğunda burası çalışacak.
    try: 
        a = int("asdfsfvcd35632")
        print("Program burada.")
    except:
        print("Bir hata oluştu.")
        print("Bloklar sona erdi.")
    print("***********************************************************")
    try: 
        b = int("asdfsfvcd35632")
        print("Program burada.")
    except ValueError:
        print("Bir hata oluştu.")
        print("Bloklar sona erdi.")

    

    try: 
        d = int(input("Bir sayı giriniz:"))
        f = int(input("Bir sayı giriniz:"))
        print(d/f)
    except ValueError:
        print("10'luk tabanda bir sayı giriniz.")
    except ArithmeticError:
        print("Matematiksel bir hata oluştu.")
    
    finally:
        print("Bloklar sona erdi.")

    #raise HataAdı(opsiyonel hata mesajı)

    def Ters_Cevir(s):
        if(type(s) !=str):
            raise ValueError("Lütfen string bir değer gönderin.") #Hata fırlatmaymış, pek anlamadım.
        else:
            return set[::-1]
    print(Ters_Cevir("Python"))
main()
