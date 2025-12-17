import board
import busio
import adafruit_ssd1306
import adafruit_framebuf

#Dont forget to change this to yours screen specification
DISPLAY_WIDTH = 0
DISPLAY_HEIGHT = 0

fb = adafruit_framebuf.FrameBuffer(bytearray('INSERT YOUR BYTEARRY!!!!!!'),DISPLAY_WIDTH, DISPLAY_HEIGHT, buf_format=adafruit_framebuf.MVLSB)

# Make sure to change the pins
i2c = busio.I2C(board.GP1, board.GP0)
display = adafruit_ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c, addr=0x3C)
bgColor=0
display.fill(bgColor)


def print_buffer(the_fb):
    for y in range(the_fb.height):
        for x in range(the_fb.width):
            if fb.pixel(x, y):
                display.pixel(x, y, 1)
            else:
                pass
    display.show()
