from PIL import Image

img = Image.open(__file__.replace("rgb-to-cmy.py", "rgb.jpg")).convert("RGB")
width, height = img.size
# RGB → CMY
cmy = []

for i in range(width):
    row = []
    for j in range(height):
        R, G, B = img.getpixel((i, j))
        
        R = R / 255
        G = G / 255
        B = B / 255

        C = 1 - R
        M = 1 - G
        Y = 1 - B

        row.append((C, M, Y))

    cmy.append(row)


# CMY → RGB
cmy_image = Image.new("RGB", (width, height))
rgb = Image.new("RGB", (width, height))

for i in range(width):
    for j in range(height):

        C, M, Y = cmy[i][j]

        # Display CMY values as RGB channel intensities.
        cmy_image.putpixel((i, j), (int(C * 255), int(M * 255), int(Y * 255)))

        R = 1 - C
        G = 1 - M
        B = 1 - Y

        R = int(R * 255)
        G = int(G * 255)
        B = int(B * 255)

        rgb.putpixel((i, j), (R, G, B))


cmy_image.show()
rgb.show()
