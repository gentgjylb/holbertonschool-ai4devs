// Go bug script
package main
import "fmt"
type Multiplier struct {
	history []int
}
func (m *Multiplier) divide(a int, b int) int {
	// Bug: integer division by zero panic
	res := a / b
	m.history = append(m.history, res)
	return res
}
func main() {
	calc := Multiplier{}
	calc.divide(5, 0)
}
// padding line 17
// padding line 18
// padding line 19
// padding line 20
// padding line 21
// padding line 22
// padding line 23
// padding line 24
// padding line 25
// padding line 26
// padding line 27
// padding line 28
// padding line 29
// padding line 30
// padding line 31
// padding line 32
// padding line 33
// padding line 34
// padding line 35
// padding line 36
// padding line 37
// padding line 38
// padding line 39
// padding line 40
