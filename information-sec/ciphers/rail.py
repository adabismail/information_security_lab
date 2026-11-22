def zigzag_pattern(length, rails):
    """Returns the rail number for each position in the text."""
    pattern, rail, step = [], 0, 1
    for _ in range(length):
        pattern.append(rail)
        if rail == 0:
            step = 1
        elif rail == rails - 1:
            step = -1
        rail += step
    return pattern

def encrypt(text, rails):
    pattern = zigzag_pattern(len(text), rails)
    fence = [[] for _ in range(rails)]
    for ch, r in zip(text, pattern):
        fence[r].append(ch)
    return "".join("".join(row) for row in fence)

def decrypt(cipher, rails):
    pattern = zigzag_pattern(len(cipher), rails)
    # work out which cipher characters belong to which rail
    order = sorted(range(len(cipher)), key=lambda i: pattern[i])
    result = [""] * len(cipher)
    for pos, ch in zip(order, cipher):
        result[pos] = ch
    return "".join(result)

message = input("Enter the message: ")
rails = int(input("Enter number of rails: "))
cipher = encrypt(message, rails)
print("Encrypted Text is:", cipher)
print("Decrypted Text is:", decrypt(cipher, rails))