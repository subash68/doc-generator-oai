# Documentation for the Sum of Integers from a File Program

## Overview
This Go program reads integers from a file named `input.txt`, calculates their sum, and then writes the result to a file named `output.txt`. It handles errors during file operations and conversions to ensure robustness. The program demonstrates basic file I/O, error handling, and the use of scanners in Go.

## Dependencies
The program uses the following standard library packages:
- `bufio`: For buffered I/O operations, specifically reading the file line by line.
- `fmt`: For formatted I/O.
- `os`: For file handling operations.
- `strconv`: For converting strings to integers.

## Functionality
1. **File Reading**: The program opens `input.txt` for reading. If the file cannot be opened, an error message is printed, and the program exits.
2. **Summation**: It initializes a variable `sum` to zero and reads each line of the file. Each line is expected to contain a single integer. The program converts these string representations of integers to actual integers and adds them to `sum`.
3. **Error Handling**: If an error occurs during reading or conversion, an error message is printed and the program exits gracefully.
4. **File Writing**: After calculating the total sum, the program opens (or creates) `output.txt` in append mode. If successful, it writes the sum to this file and handles any errors that may occur.
5. **Resource Management**: The program ensures that files are properly closed after their operations are complete using the `defer` statement.

## Code Breakdown

### Main Function
The entry point of the program.

```go
func main() {
    // Your code goes here
```

### Opening the Input File
Attempt to open `input.txt`.
```go
file, err := os.Open("input.txt")
if err != nil {
    fmt.Errorf("Error occurred %v", err)
    return
}
defer file.Close()
```

### Reading and Summing Integers
Initialize `sum` and use a scanner to read each line from the input file:
```go
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
```

### Error Checking for Scanner
Check for errors during scanning:
```go
if err := scanner.Err(); err != nil {
    fmt.Errorf("Error occurred %v", err)
    return
}
```

### Outputting the Sum
Attempt to open (or create) `output.txt` and write the sum:
```go
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
```

### Conclusion
This program effectively calculates the sum of integers from a text file and demonstrates fundamental aspects of file I/O and error management in Go. It can be extended or modified to accommodate additional functionality such as input validation, support for different number formats, or handling more complex files.

## Usage
1. Create a text file named `input.txt` in the same directory as the program with one integer per line.
2. Run the program.
3. The result will be written to `output.txt`, creating the file if it does not exist or appending to it if it does.

## Example
Assuming `input.txt` contains:
```
5
10
15
```
Running the program will produce an `output.txt` file with:
```
30
```