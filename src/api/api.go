package main

import (
	"fmt"
	"io"
	"strings"
)

func main() {
	reader := strings.NewReader("Let us catch up over a cup of coffee")

	byt := make([]byte, 5) // Read in chunks of 5 bytes
	for {
		n, err := reader.Read(byt) // Read into byt
		if err != nil {
			if err == io.EOF {
				fmt.Printf("%v EOF\n", string(byt[:n])) // Print the final chunk correctly
				break
			}
			fmt.Println("Error reading:", err)
			break
		}
		fmt.Printf("%v <nil>\n", string(byt[:n])) // Only print the read bytes
	}
}
