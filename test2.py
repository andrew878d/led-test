import board
import busio
import digitalio
from adafruit_rgb_display import ili9341
from PIL import Image, ImageDraw

# 1. Pin Setup
cs_pin = digitalio.DigitalInOut(board.D7)  # Physical Pin 26
dc_pin = digitalio.DigitalInOut(board.D24) # Physical Pin 18
reset_pin = digitalio.DigitalInOut(board.D25) # Physical Pin 22

# 2. SPI Setup (Slower speed for stability)
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# 3. Initialize
disp = ili9341.ILI9341(spi, rotation=90, cs=cs_pin, dc=dc_pin, rst=reset_pin, baudrate=8000000)

# 4. Draw a test Square
image = Image.new("RGB", (disp.width, disp.height), "BLUE") # Should turn the whole screen blue
disp.image(image)
print("Screen should now be Blue!")
