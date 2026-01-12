
def secret_code(char):
    """
    Generate a secret numeric code for a character.
    Formula: (ASCII value * 7) + 13
    You can change the multiplier and shift to make it more unique.
    """
    ascii_val = ord(char)
    return (ascii_val * 7) + 13

def ascii_checker():
    print("=== ASCII Value Checker ===")
    print("Type 'exit' to quit.\n")
    
    while True:
        user_input = input("Enter a character: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        if len(user_input) != 1:
            print("Please enter exactly one character.\n")
            continue
        
        ascii_val = ord(user_input)
        secret_val = secret_code(user_input)
        
        print(f"Character: {user_input}")
        print(f"ASCII Value: {ascii_val}")
        print(f"Secret Numeric Code: {secret_val}\n")

# Run the checker
if __name__ == "__main__":
    ascii_checker()
