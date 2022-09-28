package main

import "fmt"

func main() {
	//fmt.Println("deneme")

	// Çeşitli paketler ile daha az kod yazabiliriz, fmt de pakettir mesela.

	/// DİZİLER \\\

	// city1 := "İstanbul"
	// city2 := "Roma"
	// city3 := "Ankara"
	// city4 := "Bursa"

	// fmt.Println(city1,city2,city3,city4)

	//cities := [4]string{"İstanbul", "Ankara", "Roma", "Bursa"}
	//köşeli parantezin içini boş bırakırsak ya da 3 nokta koyarsak
	//yine diziyi istediğimiz uzunlukta alabiliriz.
	//fmt.Println(cities)
	//fmt.Println(cities[0])

	// var myArr [5]int
	// fmt.Println(myArr)

	// myArr[0] = 99
	// myArr[len(myArr)-1] = 199
	// fmt.Println(myArr)

	// // for i := 0; i < len(myArr); i++ {
	// // 	fmt.Println(i, cities[i])
	// // }

	// myArr = mySquare(myArr)

	// fmt.Println(myArr)

	/////// SLİCES \\\\\\
	//Slice'lar, array özelliklerinin genişletilmiş versiyonu olarak karşımıza çıkıyor.
	//Arrayler ile aynı gösterime sahiptir.
	//Program içerisinde tanımlarken tek farkı arraylerde uzunluk belirtirken, slicelarda belirtilmez.

	// Arr55 := [3]int{1, 2, 3}
	// Arr66 := [...]int{1, 2, 3, 4} //Slice
	// fmt.Println(Arr55)
	// fmt.Println(Arr66)

	// underArray := [...]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

	// fmt.Println(underArray)
	// mySlc1 := underArray[2:5]
	// fmt.Println(mySlc1)

	///// Maps \\\\\\

	myMap := map[string]int{
		"Ahmet":  40,
		"Mehmet": 25,
		"Ali":    34,
	}

	fmt.Println(myMap)
	fmt.Println(myMap["Ahmet"], myMap["Mehmet"])

}

// func mySquare(arr [5]int) [5]int {
// 	for i := 0; i < len(arr); i++ {
// 		arr[i] = arr[i] * arr[i]
// 	}
// 	return arr
// }
