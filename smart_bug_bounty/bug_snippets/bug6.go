// Bug 6 - Integer overflow in factorial
// Intended behavior: compute the factorial of n and return it.
// Issue: uses int32 which overflows for n >= 13; should use int64 or big.Int.

package main

import "fmt"

func factorial(n int) int32 {
	if n < 0 {
		return -1 // sentinel for invalid input
	}
	if n == 0 {
		return 1
	}

	var result int32 = 1 // BUG: int32 overflows for n >= 13
	for i := 1; i <= n; i++ {
		result *= int32(i)
	}
	return result
}

func main() {
	for _, v := range []int{5, 10, 13, 20} {
		// 13! = 6227020800, which exceeds int32 max (2147483647)
		fmt.Printf("factorial(%d) = %d\n", v, factorial(v))
	}
}
