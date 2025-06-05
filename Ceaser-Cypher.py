def encrypt(text, shift):
    """
    Encrypts text using Caesar cipher with specified shift value.
    
    Args:
        text (str): The plain text to encrypt
        shift (int): The shift value (key) for encryption
    
    Returns:
        str: The encrypted text
    """
    result = ""
    
    # Traverse through each character in the text
    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            # Apply shift (with modulo to handle wrap-around)
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        # Check if character is a lowercase letter
        elif char.islower():
            # Apply shift (with modulo to handle wrap-around)
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        # Keep non-alphabetic characters unchanged
        else:
            result += char
    
    return result

def decrypt(text, shift):
    """
    Decrypts text encrypted with Caesar cipher.
    
    Args:
        text (str): The encrypted text
        shift (int): The shift value (key) used for encryption
    
    Returns:
        str: The decrypted text
    """
    # Decryption is just encryption with negative shift
    return encrypt(text, -shift)

def main():
    print("==== Caesar Cipher Tool ====")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    
    # Get user's choice
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        # Encryption
        message = input("Enter the message to encrypt: ")
        try:
            shift = int(input("Enter the shift value (1-25): "))
            if not 1 <= shift <= 25:
                print("Shift value must be between 1 and 25.")
                return
        except ValueError:
            print("Please enter a valid number for shift.")
            return
            
        encrypted = encrypt(message, shift)
        print("\nEncrypted message:", encrypted)
        
    elif choice == '2':
        # Decryption
        message = input("Enter the message to decrypt: ")
        try:
            shift = int(input("Enter the shift value used for encryption (1-25): "))
            if not 1 <= shift <= 25:
                print("Shift value must be between 1 and 25.")
                return
        except ValueError:
            print("Please enter a valid number for shift.")
            return
            
        decrypted = decrypt(message, shift)
        print("\nDecrypted message:", decrypted)
        
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
