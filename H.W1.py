
        
        ascii_val = ord(user_input)
        secret_val = secret_code(user_input)
        
        print(f"Character: {user_input}")
        print(f"ASCII Value: {ascii_val}")
        print(f"Secret Numeric Code: {secret_val}\n")

# Run the checker
if __name__ == "__main__":
    ascii_checker()

