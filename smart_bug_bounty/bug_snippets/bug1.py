# A script to process sales data and find the top N salespeople
# and their total sales.

class SalesDataProcessor:
    def __init__(self, data):
        self.data = data
        self.sales_by_person = {}

    def process_data(self):
        # Data format: [{"name": "Alice", "amount": 100}, ...]
        for entry in self.data:
            name = entry.get("name")
            amount = entry.get("amount", 0)
            
            # Bug: using = instead of += will overwrite previous sales
            if name in self.sales_by_person:
                self.sales_by_person[name] = amount
            else:
                self.sales_by_person[name] = amount

    def get_top_n_salespeople(self, n):
        # Sort salespeople by their total sales in descending order
        sorted_sales = sorted(
            self.sales_by_person.items(), 
            key=lambda item: item[1], 
            reverse=True
        )
        
        # Bug: off-by-one error or something? If we want top N. Let's just return sorted_sales[0:n]
        # Actually, let's make an off-by-one bug here: returning n+1 
        return sorted_sales[0:n+1]

def main():
    raw_data = [
        {"name": "Alice", "amount": 150},
        {"name": "Bob", "amount": 200},
        {"name": "Alice", "amount": 300},
        {"name": "Charlie", "amount": 50},
        {"name": "Bob", "amount": 100}
    ]
    processor = SalesDataProcessor(raw_data)
    processor.process_data()
    top_2 = processor.get_top_n_salespeople(2)
    print(f"Top 2 salespeople: {top_2}")

if __name__ == "__main__":
    main()
