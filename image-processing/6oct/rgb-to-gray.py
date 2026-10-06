from PIL import Image

img = Image.open(__file__.replace("rgb-to-gray.py", "rgb.jpg")).convert("RGB")

width, height = img.size

gray = Image.new("L", (width, height))

for i in range(width):
    for j in range(height):

        R, G, B = img.getpixel((i, j))

        value = (R + G + B) // 3

        gray.putpixel((i, j), value)

gray.show()
