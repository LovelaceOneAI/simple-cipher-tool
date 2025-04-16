def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    print("Caesar Cipher Tool")
    choice = input("Encrypt or Decrypt? (e/d): ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (e.g. 3): "))

    if choice == 'e':
        print("Encrypted:", caesar_encrypt(message, shift))
    elif choice == 'd':
        print("Decrypted:", caesar_decrypt(message, shift))
    else:
        print("Invalid choice.")
