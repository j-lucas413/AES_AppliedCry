from sub_byte import sub_byte
from mix_columns import mix_columns
from shift_row import shift_row
from generate_round_key import generate_round_key

#****************************************
#
#  XOR every entry between two 4x4 matricies
#
#****************************************

def xor_blocks(matrix_a, matrix_b):
  result = [[], [], [], []]
  for i in range(4):
    result[i] = [0, 0, 0, 0]
    for ii in range(4):
      result[i][ii] = matrix_a[i][ii] ^ matrix_b[i][ii]

  return result

#****************************************
#
#  Encrypt a message using the AES algorithm,
#  10 rounds of encryption for AES-128
#
#****************************************

def aes_encrypt(block_bytes, key_bytes):
  # Convert the 16-byte block and key into 4x4 arrays
  state_matrix = [[], [], [], []]
  key_matrix = [[], [], [], []]
  for i in range(4):
    state_matrix[i] = [0, 0, 0, 0]
    key_matrix[i] = [0, 0, 0, 0]
    for ii in range(4):
      state_matrix[i][ii] = block_bytes[ii * 4 + i]
      key_matrix[i][ii] = key_bytes[ii * 4 + i]

  # Generate the full key schedule
  round_keys = [key_matrix]
  for rnum in range(1, 11):
    next_key = generate_round_key(round_keys[-1], rnum)
    round_keys.append(next_key)

  state_matrix = xor_blocks(state_matrix, round_keys[0])

  # First 9 rounds
  for rnum in range(1, 10):
    state_matrix = sub_byte(state_matrix)
    state_matrix = shift_row(state_matrix)
    state_matrix = mix_columns(state_matrix)
    state_matrix = xor_blocks(state_matrix, round_keys[rnum])

  # In the 10th round mix columns is omitted
  state_matrix = sub_byte(state_matrix)
  state_matrix = shift_row(state_matrix)
  state_matrix = xor_blocks(state_matrix, round_keys[10])

  # Flatten the 4x4 matrix back to a 1D list of bytes
  ciphertext_bytes = []
  for i in range(4):
    for ii in range(4):
      ciphertext_bytes.append(state_matrix[ii][i])
          
  return ciphertext_bytes
