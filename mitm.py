# Public Diffie-Hellman parameters
p = 23
g = 5


alice_private = 6
alice_public = pow(g, alice_private, p)


bob_private = 15
bob_public = pow(g, bob_private, p)

eve_private_for_alice = 13
eve_public_for_alice = pow(g, eve_private_for_alice, p)
eve_private_for_bob = 7
eve_public_for_bob = pow(g, eve_private_for_bob, p)

alice_shared_secret = pow(
    eve_public_for_bob,
    alice_private,
    p
)


eve_shared_secret_with_alice = pow(
    alice_public,
    eve_private_for_bob,
    p
)

bob_shared_secret = pow(
    eve_public_for_alice,
    bob_private,
    p
)


eve_shared_secret_with_bob = pow(
    bob_public,
    eve_private_for_alice,
    p
)



print("Public parameters")
print("p =", p)
print("g =", g)

print("\nAlice")
print("Private key =", alice_private)
print("Public key  =", alice_public)

print("\nBob")
print("Private key =", bob_private)
print("Public key  =", bob_public)

print("\nEve")
print("Private key for Alice =", eve_private_for_alice)
print("Public key for Alice  =", eve_public_for_alice)
print("Private key for Bob   =", eve_private_for_bob)
print("Public key for Bob    =", eve_public_for_bob)

print("\nShared secrets")

print("Alice's secret with Eve =", alice_shared_secret)
print("Eve's secret with Alice =", eve_shared_secret_with_alice)

print("Bob's secret with Eve   =", bob_shared_secret)
print("Eve's secret with Bob   =", eve_shared_secret_with_bob)