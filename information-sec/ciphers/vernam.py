def vernam(text, key):
    return "".join(chr(ord(t) ^ ord(k)) for t, k in zip(text, key))

message = input("Enter your message: ")
key = input("Enter key (same length as message): ")

if len(key) != len(message):
    print("ERROR: key length is not the same as the message length")
else:
    cipher = vernam(message, key)
    print("Encrypted Text (hex) is:", cipher.encode("latin-1").hex())
    print("Decrypted Text is:", vernam(cipher, key))   # XOR again = original