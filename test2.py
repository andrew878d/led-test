import board
import busio
import digitalio
from PIL import Image, ImageDraw
from adafruit_rgb_display import ili9341

# 1. Setup Pins (Using the same ones as your current code)
cs_pin = digitalio.DigitalInOut(board.D7) # GPIO 7 is CE1
dc_pin = digitalio.DigitalInOut(board.D24)
reset_pin = digitalio.DigitalInOut(board.D25)

# 2. Setup SPI
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# 3. Initialize Display
disp = ili9341.ILI9341(
    spi,
    rotation=90,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=24000000,
)

# 4. Create Canvas & Draw
image = Image.new("RGB", (320, 240), "BLACK")
draw = ImageDraw.Draw(image)
draw.rectangle([20, 20, 80, 80], outline="red", fill="blue")

# 5. Push to Screen
disp.image(image)
print("ILI9341 Test Sent.")
