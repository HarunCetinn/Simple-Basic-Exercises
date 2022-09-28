def main():
    liste= ["12345", "abcd456","698224aaa" , "12345678900", "123abcd"]
    for i in liste:
        try: 
            i = int(i) #Hata alırsak print fonksiyonu çalışmayacak.
            print(i)
        except:
            pass #pass bloğu bir şey yapılmadığını beliritr.

    print("\n****************************\n")

    def Sayi_Cift_mi(x):
        if (x%2==0):
            return x
        else:
            raise ValueError
    liste = [33,20,29,10,17,38,63]

    for i in liste:
        try:
            print(Sayi_Cift_mi(i))
        except ValueError:
            pass


main()
