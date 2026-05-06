import time
from PIL import Image, ImageDraw
import ST7789 
# Change to ILI9341 if that is your specific driver

# 1. Initialize Display
disp = ST7789.ST7789(port=0, cs=0, dc=24, rst=25, width=320, height=240, rotation=0)
disp.begin()

# 2. Create Canvas (Black background)
canvas = Image.new("RGB", (disp.width, disp.height), "BLACK")
draw = ImageDraw.Draw(canvas)

# 3. Draw Simple Shapes
# Square: [x0, y0, x1, y1]
draw.rectangle([20, 20, 80, 80], outline="red", fill="blue")

# Circle: [x0, y0, x1, y1] (it draws inside this bounding box)
draw.ellipse([100, 20, 160, 80], outline="white", fill="green")

# Hexagon: List of (x, y) coordinates
hexagon = [(220, 50), (240, 20), (280, 20), (300, 50), (280, 80), (240, 80)]
draw.polygon(hexagon, outline="yellow", fill="purple")

# 4. Write to Screen
disp.display(canvas)
