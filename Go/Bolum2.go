package main

import "fmt"

var packVar = "Package Scope"

//fonksiyon dışında kısa yazım hata verir.

func main() {

	/* var studentName = "John Doe"
	var grade = 77
	var isPassed = true */

	/* var studentName string = "John Doe"
	var grade int = 77
	var isPassed bool = true */

	studentName := "John Doe"
	grade := 77
	isPassed := true

	fmt.Println(studentName)
	fmt.Println(grade)
	fmt.Println(isPassed)
	//////////	////////// Scope Kavramı ////////  ///////////

	if true {
		var blockVar = "Block Scope"
		fmt.Println(blockVar)
	}

	var funcVar = "Func Scope"
	fmt.Println(funcVar)
	fmt.Println(packVar)

	//myFunc()

	var name = "Harun"
	name, lastname := "Çetin", "software"
	fmt.Println(name, lastname)
	/////// Veri Tipi Dönüştürme //////////

	x := 15
	y := 10.0
	//z :="5"

	//type conversion type(value) => int(y) 10.0 =>10 covert
	fmt.Println(x + int(y))
	// fmt.Println(x+int(z)) string değerler int değere döndürülemez.
	// lakin int değerler ascii tablosuna göre stringe çevrilebilirler.
	// %v ise değerini yazdırır %T tipini yazdırır.

	// bazı sayı tabanlarında sayı yazdırmak için %b, %d, %o vs kullanarak yazabiliriz.

	// x,y = y,x burada çoklu atama yaptık

	shadowint := 5

	if true {
		shadowint = 10
		shadowint++
		fmt.Println(shadowint)
	}

	fmt.Println(shadowint)

}

/* func myFunc(){
	fmt.Println(funcVar) Kendi scopenun dışında çapırılan değişkenler erişilebilir değildir.
} */
