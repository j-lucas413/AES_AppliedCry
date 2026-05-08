from aes_algorithm import aes_encrypt
from key import generate_key
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

#****************************************
#
#  Main method
#
#****************************************

def main():
    print("Welcome to Super Secure AES ENCRYPTION PROGRAM!")
    choice = input("Would you like to generate a new key? (yes/no): ").strip().lower()
    
    if choice == "yes":
        key = generate_key()
        print("Generated Key (hex):", key.hex())
    else:
        print("Not Secure at all...")
        key = generate_key()
        print("Here is your newly generated key anyway (hex):", key.hex())

    message = input("Enter the message you want to encrypt: ")
    
    # 1. Convert string to raw bytes
    message_bytes = message.encode('utf-8')
    
    # 2. Pad to ensure the message is a multiple of 16 bytes
    pad_len = 16 - (len(message_bytes) % 16)
    padded_message = message_bytes + bytes([pad_len] * pad_len)

    # 3. Split into 16-byte blocks cleanly
    blocks = [padded_message[i:i+16] for i in range(0, len(padded_message), 16)]
    
    # 4. Encrypt each block using your custom algorithm
    encrypted_blocks = []
    for block in blocks:
        encrypted_blocks.append(aes_encrypt(block, key))

    encrypted_message = b''.join(encrypted_blocks)
    print("\nEncrypted Message (Custom hex):", encrypted_message.hex())

    # Python AES for comparison
    cipher = AES.new(key, AES.MODE_ECB)
    test_encrypted_message = cipher.encrypt(padded_message)
    print("Encrypted message (Test hex):  ", test_encrypted_message.hex())

if __name__ == "__main__":
    main()
