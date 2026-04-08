def filter_invalid_users(user_database):
    """
    Validates users in the database and removes invalid ones.
    A user is invalid if they don't have an email or are marked inactive.
    Returns the cleaned database.
    """
    if not isinstance(user_database, dict):
        print("Error: Input is not a valid user database.")
        return {}
        
    print(f"Starting validation for {len(user_database)} users.")
    removed_count = 0
    
    try:
        # FIXED: Wrapped .items() with list() to iterate over a static snapshot
        for user_id, user_info in list(user_database.items()):
            is_valid = True
            if 'email' not in user_info or not user_info['email']:
                print(f"User {user_id} missing email.")
                is_valid = False
            elif user_info.get('status') == 'inactive':
                print(f"User {user_id} is inactive.")
                is_valid = False
            if not is_valid:
                del user_database[user_id]
                removed_count += 1
    except Exception as e:
        print(f"An error occurred during filtering: {e}")
        
    print(f"Filtering complete. Removed {removed_count} users.")
    return user_database

if __name__ == '__main__':
    db = {"u1": {"email": "a@x.com", "status": "active"},
          "u2": {"status": "active"},
          "u3": {"email": "b@x.com", "status": "inactive"}}
    print("Cleaned DB:", filter_invalid_users(db))



