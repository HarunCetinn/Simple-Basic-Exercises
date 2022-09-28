package main

import (
	"fmt"
	"math"
)

func main() {

	///////// Basit Matematik İşlemleri/////////
	x, y := 15, 10

	fmt.Println(x + y)
	fmt.Println(x - y)
	fmt.Println(x * y)
	fmt.Println(x / y)
	fmt.Println(x % y)

	z := 5.0 / 2
	fmt.Println(z)

	t := 5
	t = t + 1
	fmt.Println(t)
	t++
	fmt.Println(t)
	t = t - 1
	fmt.Println(t)
	t--
	fmt.Println(t)

	///////değişken ve sabitler

	const pi float64 = 3.14
	r := 3.0
	areaOfCircle := pi * (math.Pow(r, 2))
	fmt.Println(areaOfCircle)

	//pi = pi+1 hata verir çünkü sabitleri
	//değiştiremeyiz.
	//const ----> compile(derleme) time
	//var ----> run(çalışma) time

	// a :=3
	// const b = a
	//derleme zamanında çalışan şeye run timeda
	//çalışan şeyi atayamayız. Yani sabitlere
	//değişken atayamayız.

	///////Veri Tipi Olmayan Sabitler//////

	//Go tipi olmayan sabitler için kullanmadığında
	//default bir veri tipi atar ve işlem için
	//kullanılacaksa çevirme yapar ama işlem yoksa sabiti gösterir.

	const h = 3
	var p int16 = 12

	fmt.Println(h + p)
	fmt.Printf("%T , %v\n", h, h)

	F := -40
	K := float64(F-32)/1.8 + 273

	fmt.Println(K, F)

}
