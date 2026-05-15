#python code for Raspberry Pi 4
#Author: Andrew Dale
#BEE499 Vemuri Spring 2026

import time
import board
import busio
import digitalio
from PIL import Image, ImageDraw
import math
import adafruit_mpu6050

#use the ILI9341 driver
from adafruit_rgb_display import ili9341

#initialize pins
cs_pin = digitalio.DigitalInOut(board.D22)    # RP Pin 26 
dc_pin = digitalio.DigitalInOut(board.D24)   # RP Pin 18
reset_pin = digitalio.DigitalInOut(board.D25)# RP Pin 22

#Setup SPI
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)

#setup I2C for mpu6050
i2c = busio.I2C(board.SCL, board.SDA)

#initialize the ILI9341 driver
disp = ili9341.ILI9341(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=24000000
)

#initialize mpu6050
mpu = adafruit_mpu6050.MPU6050(i2c)

WIDTH=320
HEIGHT=240

#Create Canvas
canvas = Image.new("RGB", (320, 240), "BLACK")
draw = ImageDraw.Draw(canvas)

#Draw circle at center to start
#bottom left point (x1,y1,...) top right point (,...x2,y2)
RADIUS = 20
cx = WIDTH // 2  #center x
cy = HEIGHT // 2 #center y 
#STEP_SIZE = 10   #move 10 pixels per movement
#the circle is really just using the ellipse shape.
draw.ellipse([cx - RADIUS, cy - RADIUS, cx + RADIUS, cy + RADIUS], outline="red", fill="blue")
disp.image(canvas, rotation=90)
print("Initial centered circle drawn")

#If the mpu6050 moves, a new circle will be drawn with new centered x or y values

try:
    while True:
      
      #get tilt forces from the mpu6050
      accel_x, accel_y, accel_z = mpu.acceleration

      #duplicate variables of previous x and y values 
      new_cx = cx
      new_cy = cy

      #use polar coordinates
        
      #magnitude r = sqrt(a^2 + b^2)
      #r will be like the new STEP SIZE. 
      r = math.sqrt(accel_x**2 + accel_y**2)

      #theta: angle of tilt to tell us which direction in the x and y direction. - or +.
      #theta = arctan(y and x)
      theta = math.atan2(accel_y, accel_x)

      #only if magnitude of tilt is big enough will the circle move.
      #this allows the circle to stay if the sensor is flat.
      if r > 1.0:

        #convert magnitude r back to X and Y values so we know how much to change the circle movement. 
        #X = r * cos(theta)
        #Y = r * sin(theta)
        new_cx = cx + (r * math.cos(theta))
        new_cy = cy + (r * math.sin(theta))
        
        #detect if new x or y values will be equal to the border. Nothing new here from WASD code.
        #Border is width 320 pixels by height 240 pixels.
        if (new_cx - RADIUS) >= 0 and (new_cx + RADIUS) <= WIDTH:
            #then safe to move horizontally
            cx = new_cx 

        if (new_cy - RADIUS) >= 0 and (new_cy + RADIUS) <= HEIGHT:
            #then safe to move vertically
            cy = new_cy 

        #re-draw screen with new changes:

        #clear screen
        draw.rectangle((0, 0, WIDTH, HEIGHT), fill="BLACK")

        #draw new circle
        draw.ellipse([cx - RADIUS, cy - RADIUS, cx + RADIUS, cy + RADIUS], outline="red", fill="blue")
        disp.image(canvas, rotation=90)


except KeyboardInterrupt:
    print("\nStopping python script...")

