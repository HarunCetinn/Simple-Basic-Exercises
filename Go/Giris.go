package main

import "fmt"

func main() {

	var sayi int = 5
	varsızdegisken := 22
	var isim, soyisim string = "Harun", "Çetin"
	çokbicimli_değsken, çokbicimli_değsken2 := 5, "deneme" //direkt olarak değişken adıyla da veri tutabiliriz
	sayi = 10                                              //ayrıca ard arda farklı türklerde verileri de tutabiliriz.
	var (
		degisken1 = 66
		degisken2 = 77
		sayi99    int //default değer, zero values int string fark etmez aynı boş gelir
	)

	fmt.Println(sayi)
	fmt.Println("Hoş geldin " + isim + " " + soyisim)
	fmt.Println(çokbicimli_değsken, çokbicimli_değsken2)
	fmt.Println(varsızdegisken)
	fmt.Println(degisken1, degisken2)
	fmt.Println(sayi99)

	fmt.Printf("%T", isim) //½T değikenin tipini belirtir

}
