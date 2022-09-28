package main

import "fmt"

// type circle struct {
// 	r float64
// }

// func (c circle) display() {
// 	fmt.Println("A Circle")
// 	wg.Done()
// }

// func (c circle) area() float64 {
// 	return math.Pi * c.r * c.r
// }

// var wg sync.WaitGroup

// func main() {
// 	/// GO Routine \\\ //Sanırım asenkron çalışma mantığı var
// 	//Eş zamanlı çalışıyorlarmış

// 	go printX()
// 	//fmt.Println()
// 	wg.Wait()
// 	printY()

// 	//time.Sleep(time.Second)

// 	wg.Add(1)

// 	/// Chanels \\\

// 	wg.Add(1)
// 	c1 := circle{5}

// 	area1 := c1.area()
// 	fmt.Printf("%.2f\n", area1)
// 	go c1.display()
// 	wg.Wait()
// }

// func printX() {
// 	for i := 0; i < 2000; i++ {
// 		fmt.Print("X")
// 	}
// 	wg.Done()
// }

// func printY() {
// 	for i := 0; i < 20; i++ {
// 		fmt.Print("Y")
// 	}
// }

func main() {

	// go routiinelerde return yapamayız, o yüzden
	// channelları kullanırız.
	myChannel := make(chan string)

	go merhaba(myChannel)
	fmt.Println(myChannel)
	fmt.Println(<-myChannel)
}

func merhaba(chan1 chan string) {
	chan1 <- "Merhaba"
}
