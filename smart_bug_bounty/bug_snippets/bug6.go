// bug6.go – BankAccount with data race (missing sync.Mutex)
package main
import (
	"fmt"
	"sync"
)
// Bug: no sync.Mutex guards the balance field. Concurrent goroutines
// perform un-synchronized read-modify-write on a.balance, causing a
// data race; the final balance is unpredictable (detectable with -race).
type BankAccount struct {
	name    string
	balance int
}

func (a *BankAccount) Deposit(amount int) {
	a.balance += amount // not thread-safe
}

func (a *BankAccount) GetBalance() int {
	return a.balance
}

func simulateDeposits(acct *BankAccount, n, amount int) {
	var wg sync.WaitGroup
	for i := 0; i < n; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			acct.Deposit(amount)
		}()
	}
	wg.Wait()
}

func main() {
	acc := &BankAccount{name: "Reserves", balance: 0}
	fmt.Printf("Start:    $%d\n", acc.GetBalance())
	simulateDeposits(acc, 1000, 10)
	fmt.Printf("Expected: $%d  Got: $%d\n", 10000, acc.GetBalance())
}
