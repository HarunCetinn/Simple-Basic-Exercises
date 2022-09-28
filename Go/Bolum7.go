package main

import "fmt"

type employee struct {
	name      string
	age       int
	isMarried bool
}

type engineer struct {
	employee
	// name      string
	// age       int
	// isMarried bool
	hasDegree bool
}

func main() {
	//// Struct (Yapı) \\\\

	// var employee struct {
	// 	age       int
	// 	name      string
	// 	isMarried bool
	// }

	// fmt.Println(employee)
	// fmt.Println(employee.age)

	// employee.name = "Harun"
	// employee.age = 23
	// employee.isMarried = false
	// fmt.Println(employee)

	var e1 employee
	e1.name = "Mustafa"
	e1.age = 19
	e1.isMarried = false

	var e2 employee
	e2.name = "Harun"
	e2.age = 23
	e2.isMarried = false

	fmt.Println(e1, "\n", e2)

	e3 := e2
	fmt.Println(e3)
	e3.name = "Timur"
	fmt.Println(e3)
	fmt.Println(e2) //pass by value

	var e4 engineer
	e4.name = "Harun"
	e4.age = 25
	e4.isMarried = false
	e4.hasDegree = true

	fmt.Println(e4)

}
