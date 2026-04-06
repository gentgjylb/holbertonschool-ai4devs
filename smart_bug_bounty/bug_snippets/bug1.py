# bug1.py
# Intended behavior: Process a list of sales entries and return
# the top N salespeople by their aggregated total sales.

class SalesDataProcessor:
    def __init__(self, data):
        self.data = data
        self.sales_by_person = {}

    def process_data(self):
        """Aggregate total sales amounts per salesperson."""
        for entry in self.data:
            name = entry.get("name")
            amount = entry.get("amount", 0)

            # Bug 1: Uses `=` instead of `+=`, so each new transaction
            # overwrites the previous total instead of accumulating it.
            if name in self.sales_by_person:
                self.sales_by_person[name] = amount
            else:
                self.sales_by_person[name] = amount

    def get_top_n_salespeople(self, n):
        """Return the top N salespeople sorted by descending total sales."""
        sorted_sales = sorted(
            self.sales_by_person.items(),
            key=lambda item: item[1],
            reverse=True
        )

        # Bug 2: Off-by-one error — returns n+1 elements instead of n.
        return sorted_sales[0:n + 1]


def main():
    raw_data = [
        {"name": "Alice", "amount": 150},
        {"name": "Bob",   "amount": 200},
        {"name": "Alice", "amount": 300},
        {"name": "Charlie", "amount": 50},
        {"name": "Bob",   "amount": 100},
    ]

    processor = SalesDataProcessor(raw_data)
    processor.process_data()

    top_2 = processor.get_top_n_salespeople(2)
    print(f"Top 2 salespeople: {top_2}")


if __name__ == "__main__":
    main()
