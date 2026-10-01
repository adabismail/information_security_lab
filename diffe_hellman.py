#public agreed p-> prime and g-> generator
p = 23
g = 5

# alice private key
a = 6

# bob private key
b = 15

# Alice public key
A = pow(g, a, p)

# Bob public key
B = pow(g, b, p)


# alice shared secret using Bob's public key
alice_shared_secret = pow(B, a, p)

# bob shared secret using Alice's public key
bob_shared_secret = pow(A, b, p)


print("Public values:")
print("p =", p)
print("g =", g)

print("\nAlice:")
print("Private key =", a)
print("Public key =", A)

print("\nBob:")
print("Private key =", b)
print("Public key =", B)

print("\nShared secrets:")
print("Alice's shared secret =", alice_shared_secret)
print("Bob's shared secret =", bob_shared_secret)