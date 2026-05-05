##This is where the main code will be, 
# it will call the other files and run the program.
## EXPLODE THE CODE

##Put you're name here to test that this works'
#Lucas Johnson

import generate_key
import column_mix
import shift_row
import sub_byte


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
    message = 10101010101010101010xb



    for int i in range(amt_block) i < amt_block
        encrypted_message = encrypt_message(message, key)
    print("Encrypted Message Block " i ": ", encrypted_message)



def encrypt_message(message, key):
    for i in range(10): #10 rounds of encryption

        

    encrypted_message = "encrypted_" + message  # This is just a dummy implementation
    return encrypted_message

def sub_byte(s)



def row_shift(s)




def column_mix(s)


def xor_key(k, s)

if __name__ == "__main__":
    main()