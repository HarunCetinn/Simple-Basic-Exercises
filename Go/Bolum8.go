package main

import "fmt"

func main() {
	//// Pointer \\\\ başka bir değişkenin adresini tutar.
	name := "deneme"

	fmt.Println(&name) //name değişkeninin hafızadaki adresi

	// x1 := 10
	// x2 := x1
	// fmt.Println(x1, x2)
	// x1 = 5
	// fmt.Println(x1, x2)

	x1 := 10
	x2 := &x1
	fmt.Println(x1, x2)
	fmt.Println(x1, *x2)

	*x2 = 3
	fmt.Println(x1, *x2)

	y1 := []int{1, 10, 100, 1000}
	y2 := y1
	fmt.Println(y1, y2)

	y2[0] = 7
	fmt.Println(y2)
	fmt.Println(y1) /// slicelar da pointer gibi referans tutar.

	z := 5
	fmt.Println(z)
	double(&z)
	fmt.Println(z)
}

func double(num *int) {

	fmt.Println(num)
	*num *= 2
	fmt.Println(*num)
}
