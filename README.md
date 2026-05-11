BEE499 Vemuri Spring 2026 
Raspberry Pi and LED Screen Guide via SPI

Materials:
-Raspberry pi 4
-3.2 TFT SPI 240x320 V1.0 LED Screen (HR4 86375)

Pin layout:
TFT LED Screen Pin  RP Pin	        Description
VCC	                3.3V (pin 1)	  Power
GND	                GND	            Ground
CS	                15	            Chip select. Tells the LED screen to listen to the SPI communication.
RESET	              22 (GPIO 25)	  Toggled on or off during initialization 
DC	                18 (GPIO 24)	  Data/Command. The raw pixel data.
SDI	                19 (SPI0 MOSI)	Serial data in. Uses SPI to carry the pixel data from the PI to the LED screen.
SCK	                23 (SPIO SCLK)	Serial clock. 24Mhz bit rate timing between the PI and LED screen.
LED	                Pin 17 (3.3V)	  Power for the LED screen.
SDO (MISO)	        Pin 21	        Serial data out. Communication between LED screen to PI.
T_CLK	              Unconnected 	  SPI clock for the touch controller.
T_CS	              Unconnected 	  Touch chip select
T_DIN	              Unconnected 	  Touch data in
T_DO	              Unconnected	    Touch data out
T_IRQ	              Unconnected 	  Touch interrupt request
