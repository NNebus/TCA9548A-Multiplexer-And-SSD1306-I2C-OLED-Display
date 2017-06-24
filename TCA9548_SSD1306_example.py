from luma.core.render import canvas
from luma.oled.device import ssd1306

import smbus2
import time

TCA_ADDR = 0x70 # multiplexer-address. use 'sudo i2cdetect -y 1' to detect device and get address
TCA_PORT_DISPLAY1 = 0 # multiplexer-port (Port of the SSD1306-Display connected to the multiplexer)

def mux_select(bus, tca_port):
    assert(0 <= tca_port <= 7) # check if given port is between 0 and 7 (Multiplexer has 8 Ports from 0-7)
    bus.write_byte(TCA_ADDR, 1 << tca_port) # Selecting Device from Bus + Multiplexer-Port

def main():
    bus = smbus2.SMBus(1) #init bus
    device = ssd1306(mux_select(bus, TCA_PORT_DISPLAY1)) # init device (SSD1306-Display) from bus and Multiplexer using the mux_select-method

    # draw  border and text
    for i in range(100):
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((30, 25), "Hello World " + str(i), fill="white")
        time.sleep(1)

main()