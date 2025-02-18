package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	// your code goes here

	// Read file
	file, err := os.Open("input.txt")

	if err != nil {
		fmt.Errorf("Error occurred %v", err)
		return
	}

	defer file.Close()

	sum := 0

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		num, err := strconv.Atoi(scanner.Text())
		if err != nil {
			fmt.Errorf("Error occurred %v", err)
			return
		}
		sum += num
	}

	if err := scanner.Err(); err != nil {
		fmt.Errorf("Error occurred %v", err)
		return
	}

	fmt.Println(sum)

	output, err := os.OpenFile("output.txt", os.O_WRONLY|os.O_CREATE|O_APPEND, 0600)
	if err != nil {
		fmt.Errorf("Error occurred %v", err)
		return
	}

	defer output.Close()

	_, err = output.Write(strconv.Itoa(sum))
	if err != nil {
		fmt.Errorf("Error occurred %v", err)
		return
	}

}
