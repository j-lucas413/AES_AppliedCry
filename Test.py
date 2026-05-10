from aes_algorithm import aes_encrypt

#****************************************
#
#  Static test case definitions
#
#****************************************

test_block_bytes = [
  [65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65 ,65],
  [0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, 0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34],
  [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]
]

test_key_bytes = [
  [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000],
  [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c],
  [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]
]

test_expected_results = [
  0xb49cbf19d357e6e1f6845c30fd5b63e3,
  0x3925841d02dc09fbdc118597196a0b32,
  0x69c4e0d86a7b0430d8cdb78070b4c55a
]

#****************************************
#
#  Run each test
#
#****************************************

for testnum in range(len(test_block_bytes)):
  # Test case performance code...
  block_bytes = test_block_bytes[testnum]
  key_bytes = test_key_bytes[testnum]
  output = aes_encrypt(block_bytes, key_bytes)
  expected = test_expected_results[testnum]

  # Reformat output as a consolidated hex-string
  output_hex = ""
  for i in range(16):
    output_hex += f"{output[i]:02x}"

  # Reformat expected output into byte-array format
  expected_bytes = list(expected.to_bytes(16, byteorder="big"))
  
  print("----------------------------------")
  print("\n")
  print(f"        TEST CASE : {testnum}")
  print(f"        PLAINTEXT : {block_bytes}")
  print(f"              KEY : {key_bytes}")
  print("\n")
  print(f"       OUTPUT HEX : 0x{output_hex}")
  print(f"     EXPECTED HEX : {hex(expected)}")
  print("\n")
  print(f"     OUTPUT BYTES : {output}")
  print(f"   EXPECTED BYTES : {expected_bytes}")
  print("\n")
  print(f"BYTE ARRAYS MATCH : {output == expected_bytes}")
  print("\n")