##This is where the main code will be, 
# it will call the other files and run the program.
## EXPLODE THE CODE

##Put you're name here to test that this works'
#Lucas Johnson

import secrets


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
    encrypted_message = encrypt_message(message, key)
    print("Encrypted Message: ", encrypted_message)


def generate_key():
    key = secrets.token_hex(16) #128 bit key generation
    return key

def encrypt_message(message, key):
    #for i in range(10): #10 rounds of encryption
        

    encrypted_message = "encrypted_" + message  # This is just a dummy implementation
    return encrypted_message

def decrypt_message(encrypted_message, key):

    decrypted_message = encrypted_message.replace("encrypted_", "")
    return decrypted_message

if __name__ == "__main__":
    main()