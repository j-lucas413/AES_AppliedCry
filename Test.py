from aes_algorithm import aes_encrypt

test_block_bytes =[
  [65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65 ,65],
  [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]
]

test_key_bytes = [
  [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000],
  [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]
]

test_expected_results = [
  0xb49cbf19d357e6e1f6845c30fd5b63e3,
  0x69c4e0d86a7b0430d8cdb78070b4c55a
]

for testnum in range(len(test_block_bytes)):
  block_bytes = test_block_bytes[testnum]
  key_bytes = test_key_bytes[testnum]
  output = aes_encrypt(block_bytes, key_bytes)
  expected = test_expected_results[testnum]

  fout = ""
  for i in range(16):
    fout += f"{output[i]:02x}"
  
  print("Test case", testnum)
  print("plaintext", block_bytes)
  print("key", key_bytes)
  print("0x" + fout)
  print(output)
  print(hex(expected))
  expected_bytes = expected.to_bytes(16, byteorder="big")
  print(list(expected_bytes))
  print("MATCH:", output == list(expected_bytes))