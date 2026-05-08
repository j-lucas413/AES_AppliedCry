from sub_byte import sub_byte, transform
from mix_columns import mix_the_columns
from shift_row import shift_row
from key import xor_key

#****************************************
#
#  Encrypt a message using the AES algorithm,
#  10 rounds of encryption for AES-128
#
#****************************************

def aes_encrypt(block, key_bytes):
    # Convert the 16-byte block and key into 4x4 state matrices
    state = transform(list(block))
    key_matrix = transform(list(key_bytes))

    # Initial Round
    state = xor_key(state, key_matrix) 

    # 9 Rounds
    for _ in range(10):
        state = sub_byte(state)
        state = shift_row(state)
        state = mix_the_columns(state)
        state = xor_key(state, key_matrix)
    
    # 10th Round (No MixColumns)
    state = sub_byte(state)
    state = shift_row(state)
    state = xor_key(state, key_matrix)

    # Flatten the 4x4 matrix back to a 1D list of bytes
    encrypted_block = []
    for r in range(4):
        for c in range(4):
            encrypted_block.append(state[r][c])
            
    return bytes(encrypted_block)
