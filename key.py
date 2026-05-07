import secrets

#****************************************
#
#  Generate a random key
#
#****************************************

def generate_key():
    key = secrets.token_hex(16) #128 bit key generation
    return key

#****************************************
#
#  Perform the XOR operation between the key and the message
#
#****************************************

def xor_key(key, message):
    message = ''.join(format(ord(char), '08b') for char in message) #Converts message to decimal and then binary using 08b
    key = ''.join(format(ord(char), '08b') for char in key) #
    xor_result = ''.join(str(int(a) ^ int(b)) for a, b in zip(message, key)) #XOR operation between message and key
    return xor_result