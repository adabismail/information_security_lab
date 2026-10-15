
import hashlib
import secrets
import math

# GENERATE KEYS
def generate_keys(p, g):
    # Private key
    x = secrets.randbelow(p - 2) + 1

    # Public key
    y = pow(g, x, p)

    return (p, g, y), x


# Convert a message into an integer hash
def hash_message(message):
    digest = hashlib.sha256(message.encode("utf-8")).digest()
    return int.from_bytes(digest, "big")


# SIGN THE MESSAGE
def sign_message(message, p, g, x):
    m = hash_message(message)

    while True:
        k = secrets.randbelow(p - 2) + 1
        if math.gcd(k, p - 1) == 1:
            break

    r = pow(g, k, p)

    k_inverse = pow(k, -1, p - 1)

    s = (k_inverse * (m - x * r)) % (p - 1)

    return r, s


# VERIFY THE SIGNATURE
def verify_signature(message, signature, public_key):
    p, g, y = public_key
    r, s = signature

    if not (1 <= r < p and 0 <= s < p - 1):
        return False

    m = hash_message(message)

    left = pow(g, m, p)
    right = (pow(y, r, p) * pow(r, s, p)) % p

    return left == right


# DEMO
p = 23
g = 5

public_key, private_key = generate_keys(p, g)

message = "Hello Twin"

signature = sign_message(
    message, p, g, private_key
)

print("Message:", message)
print("Public key:", public_key)
print("Private key:", private_key)
print("Signature (r, s):", signature)

print(
    "Valid signature:",
    verify_signature(message, signature, public_key)
)

tampered_message = "Hello Enemy"

print(
    "Tampered message valid:",
    verify_signature(tampered_message, signature, public_key)
)
