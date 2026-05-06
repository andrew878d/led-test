import time
import board
import busio
import digitalio
from PIL import Image, ImageDraw
from adafruit_rgb_display import ili9341 # Use the ILI9341 driver

# 1. Initialize Display Pins
cs_pin = digitalio.DigitalInOut(board.D22)    # RP Pin 26 
dc_pin = digitalio.DigitalInOut(board.D24)   # RP Pin 18
reset_pin = digitalio.DigitalInOut(board.D25)# RP Pin 22

# Setup SPI bus
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialize the ILI9341 driver (Removed rotation here to keep native 240x320 bounds)
disp = ili9341.ILI9341(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=24000000
)

# 2. Create Canvas (Using disp.width/height to match rotation)
canvas = Image.new("RGB", (320, 240), "BLACK")
draw = ImageDraw.Draw(canvas)

# 3. Draw Simple Shapes
draw.rectangle([20, 20, 80, 80], outline="red", fill="blue")
draw.ellipse([100, 20, 160, 80], outline="white", fill="green")
hexagon = [(220, 50), (240, 20), (280, 20), (300, 50), (280, 80), (240, 80)]
draw.polygon(hexagon, outline="yellow", fill="purple")

# 4. Write to Screen (Rotate the 320x240 image 90 degrees to fit the 240x320 hardware limit)
disp.image(canvas, rotation=90)

print("Shapes successfully drawn! Check the screen.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping python code...")
