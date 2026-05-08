import secrets

#****************************************
#
#  Generate a random key
#
#****************************************


def generate_key():
    return secrets.token_bytes(16)

#****************************************
#
#  Perform the XOR operation between the key and the message
#
#****************************************

def xor_key(state_matrix, key_matrix):
    # Performs XOR on two 4x4 matrices of integers
    for r in range(4):
        for c in range(4):
            state_matrix[r][c] ^= key_matrix[r][c]
    return state_matrix
