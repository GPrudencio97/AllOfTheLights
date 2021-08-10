import time
import argparse

# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def red():
    return Color(255, 0, 0)
def orange():
    return Color(255, 128, 0)
def yellow():
    return Color(255, 255, 0)
def green():
    return Color(0, 255, 0)
def blue():
    return Color(0, 0, 255)
def indigo():
    return Color(75, 0, 130)
def violet():
    return Color(238, 130, 238)