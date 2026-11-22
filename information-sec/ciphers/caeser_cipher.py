SHIFT = 3

def encrypt(text):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + SHIFT) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + SHIFT) % 26 + ord('a'))
        else:
            result += ch          # spaces, digits, symbols stay unchanged
    return result

def decrypt(text):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') - SHIFT) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') - SHIFT) % 26 + ord('a'))
        else:
            result += ch
    return result

message = input("Enter the message: ")
cipher = encrypt(message)
print("Encrypted Text is:", cipher)
print("Decrypted Text is:", decrypt(cipher))