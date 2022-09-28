package main

import "fmt"

/// Interfaces \\\   /// Polimorfizm \\\
// type rectangle struct {
// 	a, b float64
// }

// func (r rectangle) area() float64 {
// 	return r.a * r.b
// }

// func (r rectangle) circumference() float64 {
// 	return 2 * (r.a + r.b)
// }

// type shape interface {
// 	area() float64
// 	circumference() float64
// }

// func interfaceFunc(i shape) {
// 	fmt.Println(i)
// 	fmt.Println(i.area())
// 	fmt.Println(i.circumference())
// 	fmt.Printf("%T", i)
// 	fmt.Println()
// }

// func main() {
// 	/// Polimorfizm \\\

// 	r1 := rectangle{3, 8}
// 	fmt.Println("Area: ", r1.area())
// 	fmt.Println("Circumference: ", r1.circumference())

// 	interfaceFunc(r1)
// }

type shape interface {
	area() float64
}

func printArea(shapes ...shape) {
	for _, shape := range shapes {
		fmt.Println("Alan: ", shape.area())
	}
}

type triangle struct {
	a float64
	h float64
}

func (t triangle) area() float64 {
	return (t.a * t.h) / 2
}

type square struct {
	a float64
}

func (s square) area() float64 {
	return (s.a * s.a)
}

type rectangle struct {
	a, b float64
}

func (r rectangle) area() float64 {
	return (r.a * r.b)
}

func main() {
	/// Polimorfizm \\\

	t := triangle{3, 4}
	s := square{5}
	r := rectangle{2, 8}

	printArea(t, s, r)

}
