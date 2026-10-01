import random
import math


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def gen_p_q():
    p = random.randint(10, 100)
    while not is_prime(p):
        p = random.randint(10, 100)
    q = random.randint(10, 100)
    while not is_prime(q) or q == p:
        q = random.randint(10, 100)
    return p, q

def gen_e(phi):
    for e in range(2, phi):
        if math.gcd(e, phi) == 1:
            return e

def gen_d(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d

p, q = gen_p_q()
n = p * q
phi = (p - 1) * (q - 1)
e = gen_e(phi)
d = gen_d(e, phi)

print("p =", p)
print("q =", q)
print("n =", n)
print("phi =", phi)
print("e =", e)
print("d =", d)

print("\nPublic Key =", (e, n))
print("Private Key =", (d, n))



#encryption

message = int(input(f"Enter message (0 to {n - 1}): "))

if message < 0 or message >= n:
    print(f"Invalid message. Message must satisfy 0 <= message < {n}")
else:
    ciphertext = pow(message, e, n)
    print("Original message:", message)
    print("Encrypted message:", ciphertext)


    #decryption

    decrypted_message = pow(ciphertext, d, n)

    print("Decrypted message:", decrypted_message)