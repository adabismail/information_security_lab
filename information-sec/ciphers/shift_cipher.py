def encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        else:
            result += ch
    return result

def decrypt(text, key):
    return encrypt(text, -key)    # decrypting is just shifting backwards

message = input("Enter the message: ")
key = int(input("Enter the shift key: "))
cipher = encrypt(message, key)
print("Encrypted Text is:", cipher)
print("Decrypted Text is:", decrypt(cipher, key))