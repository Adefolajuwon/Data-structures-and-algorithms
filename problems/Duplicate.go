package main

import "fmt"

// Function to check if any value appears more than once in the array
func containsDuplicate(nums []int) bool {
	set := make(map[int]bool)

	for _, number := range nums {
		if set[number] {
			return true
		}
		set[number] = true
	}

	return false
}

func main() {
	nums := []int{1, 2, 3, 3}
	fmt.Println(containsDuplicate(nums))
}
