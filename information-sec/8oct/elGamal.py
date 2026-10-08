import random
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def modular_inverse(a, m):
    return pow(a, -1, m)


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def primitive_root(p):
    for g in range(2, p):
        values = set()

        for i in range(1, p):
            values.add(pow(g, i, p))

        if len(values) == p - 1:
            return g

    return None


def generate_keys(p):
    g = primitive_root(p)

    x = random.randint(2, p - 2)
    y = pow(g, x, p)

    public_key = (p, g, y)
    private_key = x

    return public_key, private_key


def encrypt(message, public_key):
    p, g, y = public_key
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    c2 = (message * pow(y, k, p)) % p

    ciphertext = (c1, c2)

    return ciphertext

def decrypt(ciphertext, private_key, p):
    c1, c2 = ciphertext

    shared_secret = pow(c1, private_key, p)
    inverse = modular_inverse(shared_secret, p)
    message = (c2 * inverse) % p

    return message


p = 467

public_key, private_key = generate_keys(p)

print("Public Key :", public_key)
print("Private Key:", private_key)
message = 123

print("\nOriginal Message:", message)

# Encryption
ciphertext = encrypt(message, public_key)
print("Ciphertext:", ciphertext)

# Decryption
decrypted_message = decrypt(
    ciphertext,
    private_key,
    public_key[0]
)

print("Decrypted Message:", decrypted_message)