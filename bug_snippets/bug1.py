def get_last_items(items, n)
    if n <= 0:
        return []
    if n > len(items):
        return items
    return items[len(items) - n : len(items)]

if __name__ == "__main__":
    sample = [10, 20, 30, 40, 50]
    print(get_last_items(sample, 3))
