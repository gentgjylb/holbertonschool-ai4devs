def process_data_and_get_last_n(data_list, n):
    """
    Processes a list of numbers by doubling them.
    Returns the last n elements from the processed list.
    """
    if not isinstance(data_list, list):
        raise ValueError("Input must be a list.")
    
    if n < 0:
        raise ValueError("n must be non-negative.")
        
    print(f"Starting processing for list of size {len(data_list)}.")
    
    # Process data: double each number
    processed_list = []
    for item in data_list:
        doubled = item * 2
        processed_list.append(doubled)
        
    print("Finished processing all items.")
    
    # BUG: If n is 0, processed_list[-0:] returns the whole list 
    # instead of an empty list
    # The fix would be: return processed_list[-n:] if n > 0 else []
    
    length = len(processed_list)
    if n > length:
        print(f"Warning: requested {n} items, only {length} available.")
        return processed_list
        
    # Potential off-by-one or unexpected behavior when n=0
    result = processed_list[-n:] 
    
    return result

if __name__ == '__main__':
    test_data = [1, 2, 3, 4, 5]
    print("Testing with n=2:", process_data_and_get_last_n(test_data, 2))
    print("Testing with n=0:", process_data_and_get_last_n(test_data, 0))

