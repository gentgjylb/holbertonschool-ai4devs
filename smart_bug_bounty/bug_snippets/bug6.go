// bug6.go
// Intended behavior: Simulate a bank account that receives many concurrent
// deposits from multiple goroutines and finishes with the correct total
// balance (numGoroutines * depositAmount).

package main

import (
	"fmt"
	"sync"
)

// BankAccount holds an owner name and a running balance.
// Bug: There is no sync.Mutex protecting the `balance` field.
// Concurrent goroutines perform un-synchronized read-modify-write
// operations (`a.balance += amount`), causing a data race whose result
// is unpredictable — the final balance will typically be less than expected.
type BankAccount struct {
	name    string
	balance int
}

// Deposit adds amount to the balance (NOT thread-safe as written).
func (a *BankAccount) Deposit(amount int) {
	a.balance += amount
}

// GetBalance returns the current balance.
func (a *BankAccount) GetBalance() int {
	return a.balance
}

// simulateDeposits fires numDeposits goroutines, each depositing amount.
func simulateDeposits(account *BankAccount, numDeposits, amount int) {
	var wg sync.WaitGroup
	for i := 0; i < numDeposits; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			account.Deposit(amount)
		}()
	}
	wg.Wait()
}

func main() {
	account := &BankAccount{name: "Corporate Reserves", balance: 0}

	const numDeposits  = 1000
	const depositAmount = 10

	fmt.Printf("Starting balance for %s: $%d\n", account.name, account.GetBalance())
	simulateDeposits(account, numDeposits, depositAmount)
	fmt.Printf("Final balance   for %s: $%d  (expected $%d)\n",
		account.name, account.GetBalance(), numDeposits*depositAmount)
}
