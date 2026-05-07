import time
import board
import busio
import digitalio
from PIL import Image, ImageDraw

#use the ILI9341 driver
from adafruit_rgb_display import ili9341

#initialize pins
cs_pin = digitalio.DigitalInOut(board.D22)    # RP Pin 26 
dc_pin = digitalio.DigitalInOut(board.D24)   # RP Pin 18
reset_pin = digitalio.DigitalInOut(board.D25)# RP Pin 22

#Setup SPI
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)

#initialize the ILI9341 driver
disp = ili9341.ILI9341(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=24000000
)

#Create Canvas
canvas = Image.new("RGB", (320, 240), "BLACK")
draw = ImageDraw.Draw(canvas)

#Draw Shapes as test
draw.rectangle([20, 20, 80, 80], outline="red", fill="blue")
draw.ellipse([100, 20, 160, 80], outline="white", fill="green")
hexagon = [(220, 50), (240, 20), (280, 20), (300, 50), (280, 80), (240, 80)]
draw.polygon(hexagon, outline="yellow", fill="purple")

#Write to Screen 
disp.image(canvas, rotation=90)

print("Shapes drawn!")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping python code...")
