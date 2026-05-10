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

#Draw circle at center to start
#bottom left point (x1,y1,...) top right point (,...x2,y2)
RADIUS = 20
cx = WIDTH // 2  # Center X (Start at 160)
cy = HEIGHT // 2 # Center Y (Start at 120)
STEP_SIZE = 10   # Move 10 pixels per turn
draw.ellipse([cx - RADIUS, cy - RADIUS, cx + RADIUS, cy + RADIUS], outline="red", fill="blue")
disp.image(canvas, rotation=90)
print("Initial centered circle drawn")

#If the user enters WASD, a new circle will be drawn using its center values

#Detect keyboard input
try:
    while True:
        key = input("Enter WASD or q to quit").lower()
        
        if key =='q':
            #then quit
            break

        new_cx = x
        new_cy = y
        
        #Switch statement to move object. Border is 320x240
        match key:
            case 'w':
                new_cy = cy - STEP_SIZE
            case 'a':
                new_cx = cx - STEP_SIZE
            case 's':
                new_cy = cy + STEP_SIZE
            case 'd':
                new_cx = cx + STEP_SIZE
                
        #first detect if object is at the border:
      
        if (new_cx - RADIUS) >= 0 and (new_cx + RADIUS) <= WIDTH:
            cx = new_cx # It's safe to move horizontally

        if (new_cy - RADIUS) >= 0 and (new_cy + RADIUS) <= HEIGHT:
            cy = new_cy # It's safe to move vertically

        #re-draw screen with new update

        #clear screen
        draw.rectangle((0, 0, WIDTH, HEIGHT), fill="BLACK")

        #draw new circle
        draw.ellipse([cx - RADIUS, cy - RADIUS, cx + RADIUS, cy + RADIUS], outline="red", fill="blue")
        disp.image(canvas, rotation=90)


except KeyboardInterrupt:
    print("\nStopping python script...")

