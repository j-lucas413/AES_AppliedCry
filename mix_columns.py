#****************************************
#
#  Generate a random key
#
#****************************************

import copy

def galois_mult(a, b):
    """
    Multiplication in the Galois field GF(2^8).
    """
    p = 0
    hi_bit_set = 0
    for i in range(2):
        if b & 1 == 1: p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set == 0x80: a ^= 0x1b
        b >>= 1
    return p % 256

def mixcolumn(column):
    """
    Mix one column by by considering it as a polynomial and performing
    operations in the Galois field (2^8).
    """
    # XOR is addition in this field
    temp = copy.copy(column) # Store temporary column for operations
    column[0] = galois_mult(temp[0], 2) ^ galois_mult(temp[1], 3) ^ \
                galois_mult(temp[2], 1) ^ galois_mult(temp[3], 1)
    column[1] = galois_mult(temp[0], 1) ^ galois_mult(temp[1], 2) ^ \
                galois_mult(temp[2], 3) ^ galois_mult(temp[3], 1)
    column[2] = galois_mult(temp[0], 1) ^ galois_mult(temp[1], 1) ^ \
                galois_mult(temp[2], 2) ^ galois_mult(temp[3], 3)
    column[3] = galois_mult(temp[0], 3) ^ galois_mult(temp[1], 1) ^ \
                galois_mult(temp[2], 1) ^ galois_mult(temp[3], 2)

def mix_the_columns(state):
    """
    Perform a mixing operation which operates on the columns of the states,
    combining the four bytes in each column.
    """
    for i in range(len(state)):
        # Create column from the corresponding array positions
        column = copy.copy(state[i])

        # Mix the extracted column
        mixcolumn(column)

        # Set the new column in the state
        state[i] = column
    return state
