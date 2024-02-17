from PIL import Image, ImageDraw
import math
import colorsys

imageSize = 600

imageCenter = (300, 300)

image = Image.new("RGB", (imageSize, imageSize), (255, 255, 255))

draw = ImageDraw.Draw(image)
# Drawing a cirlce
radius = (imageSize // 2) - 10


for x in range(imageSize):
    for y in range(imageSize):
        d_center = math.sqrt((x - imageCenter[0]) ** 2 + (y - imageCenter[1]) ** 2)
        if d_center <= radius:
            angle = math.atan2(y - imageCenter[1], x - imageCenter[0])
            hue = angle / (2 * math.pi) + 0.5
            saturation = d_center / radius
            value = 1.0
            r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
            draw.point((x, y), fill=(int(g * 255), int(r * 255), int(b * 255)))


image.save("vanitha.png")
