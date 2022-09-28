package main

import "fmt"

func main() {
	///////Karşılaştırma ve Mantıksal Operatörler////////
	//== , != , < , > , <= , >=
	// && , || , !

	///////// İf Yapısı /////////

	x := 27

	if x := 22; x%2 == 0 { //tek satırda iki atama yapacaksak ; kullanılmalıdır.
		fmt.Println(x, " çift sayıdır.")
	} else if x%2 != 0 {
		fmt.Println(x, " tek sayıdır.")
	} else {
		fmt.Println("Naptın kardeş bu sayı değil.")
	}

	fmt.Println(x)

	///////// Switch Yapısı /////////

	grade := 4

	switch grade := 3; grade {
	case 5:
		fmt.Println("Pekiyi")
	case 4:
		fmt.Println("İyi")
	case 3:
		fmt.Println("Orta")
	case 2:
		fmt.Println("Kötü")
	case 1:
		fmt.Println("Kaldı")
	default:
		fmt.Println("Geçersiz Not")
	}

	fmt.Println(grade)

	/////// For Döngüsü ////////

	for i := 1; i <= 10; i++ {
		fmt.Println(i, "Bir döngüdür.")
	}

	fmt.Println()

}
