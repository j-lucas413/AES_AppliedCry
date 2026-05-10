
from sub_byte import S_BOX

#****************************************
#
#  AES round key constants, statically define instead
#  of calculating every time
#
#****************************************

RCON = [
    0x00,
    0x01,
    0x02,
    0x04,
    0x08,
    0x10,
    0x20,
    0x40,
    0x80,
    0x1B,
    0x36
]

#****************************************
#
#  XOR every entry in two key columns
#
#****************************************

def xor_key_col(W_a, W_b):
  result = [0, 0, 0, 0]
  for i in range(4):
    result[i] = W_a[i] ^ W_b[i]

  return result

#****************************************
#
#  Generate the next round key from the current round
#  key and round number
#
#****************************************

def generate_round_key(round_key, from_round):
  result = [[], [], [], []]

  # Naming conventions have the from_round assumed to be 0
  W_0 = [0, 0, 0, 0]
  W_1 = [0, 0, 0, 0]
  W_2 = [0, 0, 0, 0]
  W_3 = [0, 0, 0, 0]

  for i in range(4):
    W_0[i] = round_key[i][0]
    W_1[i] = round_key[i][1]
    W_2[i] = round_key[i][2]
    W_3[i] = round_key[i][3]
  
  TW_3 = [0, 0, 0, 0]
  TW_3[0] = S_BOX[W_3[1]] ^ RCON[from_round]
  TW_3[1] = S_BOX[W_3[2]]
  TW_3[2] = S_BOX[W_3[3]]
  TW_3[3] = S_BOX[W_3[0]]

  W_4 = xor_key_col(W_0, TW_3)
  W_5 = xor_key_col(W_1, W_4)
  W_6 = xor_key_col(W_2, W_5)
  W_7 = xor_key_col(W_3, W_6)

  for i in range(4):
    result[i] = [0, 0, 0, 0]
    result[i][0] = W_4[i]
    result[i][1] = W_5[i]
    result[i][2] = W_6[i]
    result[i][3] = W_7[i]

  return result