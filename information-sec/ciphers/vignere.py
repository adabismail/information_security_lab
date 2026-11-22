def encrypt(text, key):
    result = ""
    j = 0                                   # position in the key (letters only)
    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % len(key)].upper()) - ord('A')
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
            j += 1
        else:
            result += ch
    return result

def decrypt(text, key):
    result = ""
    j = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % len(key)].upper()) - ord('A')
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base - shift) % 26 + base)
            j += 1
        else:
            result += ch
    return result

message = input("Enter your message: ")
key = input("Enter your key (letters only): ")
cipher = encrypt(message, key)
print("Encrypted Text is:", cipher)
print("Decrypted Text is:", decrypt(cipher, key))