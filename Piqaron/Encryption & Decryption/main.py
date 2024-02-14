import os
import string
from colorama import Fore, Style

def encrypt_text(text, key):
    encrypted_text = ""
    for char in text:
        if char in string.ascii_lowercase:
            index = (string.ascii_lowercase.index(char) + key) % 26
            encrypted_text += string.ascii_lowercase[index]
        elif char in string.ascii_uppercase:
            index = (string.ascii_uppercase.index(char) + key) % 26
            encrypted_text += string.ascii_uppercase[index]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_text(text, key):
    return encrypt_text(text, -key)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_terminal()
    print(Fore.GREEN + "Welcome to the Encryption/Decryption Program" + Style.RESET_ALL)

    choice = input("\nPlease select an operation:\n1. " + Fore.YELLOW + "Decrypt\n" + Style.RESET_ALL +
                   "2. " + Fore.RED + "Encrypt\n" + Style.RESET_ALL + "Your choice: ")

    if choice == "1":
        clear_terminal()
        ciphertext = input("Enter the ciphertext you want to decrypt: ")
        key = int(input("Enter the encryption key: "))
        decrypted_text = decrypt_text(ciphertext, key)
        print("\nDecrypted text:", Fore.CYAN + decrypted_text + Style.RESET_ALL)
    elif choice == "2":
        clear_terminal()
        plaintext = input("Enter the plaintext you want to encrypt: ")
        key = int(input("Enter the encryption key: "))
        encrypted_text = encrypt_text(plaintext, key)
        print("\nEncrypted text:", Fore.CYAN + encrypted_text + Style.RESET_ALL)
    else:
        clear_terminal()
        print("\nInvalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()
