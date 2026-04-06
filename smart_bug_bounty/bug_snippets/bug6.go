package main

import (
	"fmt"
	"sync"
)

// BankAccount simulates a simple bank account with concurrent deposits.
type BankAccount struct {
	balance int
	name    string
    // Bug: missing a sync.Mutex to protect balance during concurrent writes
}

func (a *BankAccount) Deposit(amount int) {
	// A deliberate short sleep to increase likelihood of race condition
	// time.Sleep(10 * time.Millisecond)
	a.balance += amount
}

func (a *BankAccount) GetBalance() int {
	return a.balance
}

// simulateDeposits simulates multiple users making deposits concurrently
func simulateDeposits(account *BankAccount, numDeposits int, amount int) {
	var wg sync.WaitGroup

	for i := 0; i < numDeposits; i++ {
		wg.Add(1)
		// Bug: Loop variable 'i' is captured by the closure, though it doesn't 
        // necessarily break the deposit logic, it is a common go bug if we used 'i'.
        // But the main bug is lack of mutex.
		go func() {
			defer wg.Done()
			account.Deposit(amount)
		}()
	}

	wg.Wait()
}

func main() {
	account := &BankAccount{
		balance: 0,
		name:    "Company Reserves",
	}

	numDeposits := 1000
	depositAmount := 10

	fmt.Printf("Starting balance for %s: $%d\n", account.name, account.GetBalance())

	// Expected final balance: 1000 * 10 = 10000
	simulateDeposits(account, numDeposits, depositAmount)

	fmt.Printf("Final balance for %s: $%d\n", account.name, account.GetBalance())
}
