import board
import busio
import adafruit_ssd1306
import adafruit_framebuf

def print_buffer(the_fb):
    for y in range(the_fb.height):
        for x in range(the_fb.width):
            if fb.pixel(x, y):
                display.pixel(x, y, 1)
            else:
                pass
    display.show()
