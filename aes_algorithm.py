from sub_byte import sub_byte
from mix_columns import mix_columns
from shift_row import shift_row
from key import xor_key

#****************************************
#
#  Encrypt a message using the AES algorithm,
#  10 rounds of encryption for AES-128
#
#****************************************

def aes_encrypt(message, key):
    # Perform the first 9 rounds of encryption the same
    for i in range(9):
        sub_byte(message)
        shift_row(message)
        mix_columns(message)
        xor_key(key, message)
    
    # Special case for the 10th (and final) round
    sub_byte(message)
    shift_row(message)
    xor_key(key, message)

    encrypted_message = "encrypted_" + message  # This is just a dummy implementation
    return encrypted_message