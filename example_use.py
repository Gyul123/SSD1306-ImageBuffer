import display_image
import board
import busio
import adafruit_ssd1306
import adafruit_framebuf

DISPLAY_WIDTH = 0
DISPLAY_HEIGHT = 0

#This example is for i2c!!!
i2c = busio.I2C(board.GP1, board.GP0)
display = adafruit_ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c, addr=0x3C)
bgColor=0
display.fill(bgColor)

fb = adafruit_framebuf.FrameBuffer(bytearray('INSERT YOUR BYTEARRY!!!!!!'),DISPLAY_WIDTH, DISPLAY_HEIGHT, buf_format=adafruit_framebuf.MVLSB)


display_image.print_buffer(display_image.fb)
#Yup thats it...
