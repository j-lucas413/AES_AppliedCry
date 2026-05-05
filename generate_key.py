import secrets


def generate_key():
    key = secrets.token_hex(16) #128 bit key generation
    return key

def round_key: