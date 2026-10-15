
def sha1(message):
    if isinstance(message, str):
        message = message.encode("utf-8")

    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    original_length = len(message) * 8
    message += b"\x80"

    while len(message) % 64 != 56:
        message += b"\x00"

    message += original_length.to_bytes(8, "big")

    for offset in range(0, len(message), 64):
        block = message[offset:offset + 64]

        w = [
            int.from_bytes(block[i:i + 4], "big")
            for i in range(0, 64, 4)
        ]

        for t in range(16, 80):
            value = (
                w[t - 3] ^ w[t - 8]
                ^ w[t - 14] ^ w[t - 16]
            )
            value = ((value << 1) | (value >> 31)) & 0xFFFFFFFF
            w.append(value)

        a, b, c, d, e = h0, h1, h2, h3, h4

        for t in range(80):
            if t < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif t < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif t < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = ((a << 5) | (a >> 27)) & 0xFFFFFFFF

            temp = (
                temp + f + e + k + w[t]
            ) & 0xFFFFFFFF

            # Update working variables
            e = d
            d = c
            c = ((b << 30) | (b >> 2)) & 0xFFFFFFFF
            b = a
            a = temp

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    return "".join(
        f"{h:08x}" for h in (h0, h1, h2, h3, h4)
    )


# Test cases
print("SHA-1 of abc:", sha1("abc"))
print("SHA-1 of hello:", sha1("hello"))
print("SHA-1 of empty string:", sha1(""))
