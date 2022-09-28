package main

import (
	"bufio"
	"errors"
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	//// Fonksiyonlar ve Hazır Metodlar ////
	// var x, y, sum int
	// x = 5
	// y = 10
	// sum = x + y

	// fmt.Printf("%d ve %d toplamı %d\n", x, y, sum)

	// x = 7
	// y = 11
	// fmt.Printf("%d ve %d toplamı %d", x, y, sum)

	fmt.Println(sum(5, 10))
	fmt.Println(sum(7, 15))
	fmt.Println(sum(3, 20))
	merhaba()
	merhaba2("Harun", 23)
	//merhaba2(23, "Harun") parametreleri sıralı göndermemiz lazım.

	fmt.Println(result(55))

	fmt.Print("Lütfen sınav sonucunu giriniz: ")
	reader := bufio.NewReader(os.Stdin)
	value, _ := reader.ReadString('\n')
	fmt.Println(value)

	result, err := evenNum(11)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("Girdiğiniz sayı: ", result)
	}

	fmt.Println("Lütfen aldığınız notu giriniz: ")
	grade, _ := GetGrade()
	var result2 string

	if grade >= 50 {
		result2 = "geçtiniz."
	} else {
		result2 = "kaldınız"
	}

	fmt.Println(result2)

	target := numRnad(1, 100)

	fmt.Println("1 ile 100 arasındaki sayıyı bulmaya çalışın ")

	reader2 := bufio.NewReader(os.Stdin)

	for attemps := 0; attemps < 10; attemps++ {
		fmt.Println(10-attemps, "hakkınız kaldı. ")
		fmt.Print("Lütfen tahmininizi yazınız: ")

		input, err := reader2.ReadString('\n')
		if err != nil {
			fmt.Println(err)
		}

		input = strings.TrimSpace(input)
		numran, err := strconv.Atoi(input)
		if err != nil {
			fmt.Println(err)
		}

		if numran > target {
			fmt.Println("Daha ufak bir sayı gir. ")
		} else if numran < target {
			fmt.Println("Daha büyük bir sayı gir. ")
		} else {
			fmt.Println("Doğru tahmin", target, "idi", attemps, ". tahminde buldunuz. ")
			break
		}

	}

}

func sum(x, y int) int { //sağdaki parantez dışındaki int dönüş tipini belirtir
	return x + y
}

func merhaba() {
	fmt.Println("Benim adım Harun")
}

func merhaba2(name string, age int) {
	fmt.Printf("Adım %s , yaşım  %d", name, age)
}

func result(grade int) string {
	if grade >= 50 {
		return "geçtiniz"
	}
	return "kaldınız"
}

////// Hata Yakalama /////

func evenNum(num int) (int, error) {
	if num%2 != 0 {
		return 0, errors.New("Hata: Çift sayı girmelisiniz. ")
	}

	return num, nil //nil, null değere eşittir
}

//////Genel ////

func GetGrade() (int, error) {
	reader := bufio.NewReader(os.Stdin)

	input, err := reader.ReadString('\n')
	if err != nil {
		fmt.Println(err)
	}

	input = strings.TrimSpace(input)
	num, err := strconv.Atoi(input)
	if err != nil {
		fmt.Println(err)
	}

	return num, nil
}

func numRnad(min, max int) int {
	rand.Seed(time.Now().Unix())
	return rand.Intn(max-min) + min
}
