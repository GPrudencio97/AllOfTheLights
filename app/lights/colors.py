import time, random, io

try:
    with io.open('/sys/firmware/devicetree/base/model', 'r') as m:
        if 'raspberry pi' in m.read().lower():
            from rpi_ws281x import *

            global strip

            # LED strip configuration
            LED_COUNT      = 30      # Number of LED pixels.
            LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
            #LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
            LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
            LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
            LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
            LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
            LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

            strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS,
                                      LED_CHANNEL)
            check = True
            strip.begin()

except Exception:
    check = False
    pass


def set_color(status_array):
    if check == True:
        if status_array[1] == 0 and status_array[2] == 0 and status_array[3] == 0:
            solid_color(strip, Color(int(status_array[1]), int(status_array[2]), int(status_array[3])))
        else:
            new_brightness(status_array[0])
            solid_color(strip, Color(int(status_array[1]), int(status_array[2]), int(status_array[3])))
    else:
        print("brightness:", status_array[0])
        print("color code:", int(status_array[1]), int(status_array[2]), int(status_array[3]))


def solid_color(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def rainbow(brightness, wait_ms=20, iterations=1):
    if check == True:
        new_brightness(brightness)
        for j in range(256*iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel((i+j) & 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
    else:
        print("Running Rainbow")


def rainbow_cycle(brightness, wait_ms=20, iterations=1):
    if check == True:
        new_brightness(brightness)
        for j in range(256*iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
    else:
        print("Running Rainbow Cycle")


def wheel(pos):
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rgb_twinkle(brightness, wait_s=1):
    if check == True:
        new_brightness(brightness)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(255, 255, 255))
            strip.show()
            x = 0
            for j in range(strip.numPixels()):
                x += 1

            z = round(x/15)                     #edit to effect color lights/meter
            w = round(x/2)
            var1 = random.randrange(0, w)
            var2 = random.randrange(1, 4)
            color_array = []
            color_array.append(var1)

            while len(color_array) < z:
                color_array.append(color_array[len(color_array) - 1] + w)

            if var2 == 1:
                y = 0
                for y in range(x):
                    if y in color_array:
                        strip.setPixelColor(y, Color(255, 0, 0))
                    else:
                        strip.setPixelColor(y, Color(255,255,255))
                strip.show()

            if var2 == 2:
                y = 0
                for y in range(x):
                    if y in color_array:
                        strip.setPixelColor(y, Color(0, 255, 0))
                    else:
                        strip.setPixelColor(y, Color(255,255,255))
                strip.show()

            if var2 == 3:
                y = 0
                for y in range(x):
                    if y in color_array:
                        strip.setPixelColor(y, Color(0, 0, 255))
                    else:
                        strip.setPixelColor(y, Color(255,255,255))
                strip.show()
            time.sleep(wait_s)
    else:
        print("Runninng RGB Twinkle")


def new_brightness(brightness):
    if check == True:
        global strip
        global LED_BRIGHTNESS

    brightness = int(brightness)
    new_brightness = int(255 * (brightness/100))
    if check == True:
        if new_brightness != LED_BRIGHTNESS:
            LED_BRIGHTNESS = new_brightness
            strip.setBrightness(new_brightness)
            print("LED BRIGHTNESS:", LED_BRIGHTNESS)
        else:
            print("LED BRIGHTNESS:", LED_BRIGHTNESS)
            return
    else:
        print("brightness:", brightness)
        print("new brightness:", new_brightness)


def color_changer(r, g, b):
     if check == True:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(r, g, b))
        strip.show()
     else:
        print("Changing Color Changer")

