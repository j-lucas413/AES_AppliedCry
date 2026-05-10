#****************************************
#
#  Mix columns - perform a matrix multiplication
#  in GF(2^8) modulus x^8 + x^4 + x^3 + x + 1
#
#****************************************

def mix_columns(state_matrix):
  aes_mix_column_matrix = [
    [0b10, 0b11, 0b1, 0b1],
    [0b1, 0b10, 0b11, 0b1],
    [0b1, 0b1, 0b10, 0b11],
    [0b11, 0b1, 0b1, 0b10]
  ]

  result = gf_matrix_mult(aes_mix_column_matrix, state_matrix)

  return result

#****************************************
#
#  Multiply two numbers under GF(2^8)
#
#****************************************

def gf_mult(a, b):
  result = 0

  for _ in range(8):
    # If the current bit is 1, add the result
    if b & 1:
        result = result ^ a

    # See if x^8 bit is set in factor
    high_bit = a & 0x80

    # Multiply the result by x for the next round
    a = a << 1

    # Take modulus of new factor
    if high_bit:
        a = a ^ 0b100011011
    
    # We only want 8 bits of it
    a = a & 0xFF

    # Advance to the next bit of b (corresponds with multiplying by x)
    b = b >> 1

  return result

#****************************************
#
#  Multiply two 4x4 matricies under GF(2^8)
#
#****************************************

def gf_matrix_mult(A, B):
  # 4x4 result matrix
  result = [[], [], [], []]

  for i in range(4):
    result[i] = [0, 0, 0, 0]
    for ii in range(4):
      value = 0
      for iii in range(4):
        value ^= gf_mult(A[i][iii], B[iii][ii])

      result[i][ii] = value

  return result