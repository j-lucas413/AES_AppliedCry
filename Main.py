from aes_algorithm import aes_encrypt
from key import generate_key

#****************************************
#
#  Main method
#
#****************************************

def main():
    print("Welcome to Super Securue AES ENCRYPTION PROGRAM!")
    print("Would you like to generate a new key? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        key = generate_key()
        print("Generated Key: ", key)
    else:
        print("No key generated.")
        key = input("Enter the key you want to use for encryption: ")
        print("Not Secure at all...")
        key = generate_key()
        print("Here is your key: ", key)
    print("Enter the message you want to encrypt: ")
    
    message = input()
    for char in message:
        binary_message = ''.join(format(ord(char), '08b')) #Converts message to decimal and then binary using 08b

    block_size = 16 #16 byte or 128 bit blocks
    block_message = []
    for i in range(len(binary_message)):
        block_message.append(binary_message[i:i+block_size]) #Split binary message into 16 byte blocks
    
    encrypted_blocks = []
    for block in block_message: #Encrypt each block
        encrypted_blocks.append(encrypt_message(block, key))

    encrypted_message = ''.join(encrypted_blocks)
    print("Encrypted Message: ", encrypted_message)

if __name__ == "__main__":
    main()