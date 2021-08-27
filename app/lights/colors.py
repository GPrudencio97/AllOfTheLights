from rpi_ws281x import *
import time, random



# LED strip configuration
LED_COUNT      = 30      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

global strip
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

def red(brightness):
    new_brightness(brightness)
    solid_color(strip, Color(255, 0, 0))

def orange(brightness):
    new_brightness(brightness)
    solid_color(strip, Color(255, 165, 0))

def yellow(brightness):
    new_brightness(brightness)
    solid_color(strip, Color(255, 255, 0))

def green(brightness):
    new_brightness(brightness)
    solid_color(strip, Color(0, 255, 0))

def blue(brightness):
    new_brightness(brightness)
    solid_color(strip, Color(0, 0, 255))

def indigo(brightness):
    new_brightness(brightness)
    solid_color(strip, Color(75, 0, 130))

def violet(brightness):
    new_brightness(brightness)
    solid_color(strip, Color(238, 130, 238))

def lights_off():
    solid_color(strip, Color(0, 0, 0))

def lights_on(brightness):
    new_brightness(brightness)
    solid_color(strip, Color(255, 255, 255))

def solid_color(strip, color,wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbow(brightness, wait_ms=20, iterations=1):
    new_brightness(brightness)
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)
    
    status = "DONE"
    return status 

def rainbowCycle(brightness, wait_ms=20, iterations=1):
    new_brightness(brightness)
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

    status = "DONE"
    return status

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
    new_brightness(brightness)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(255, 255, 255))
        strip.show()
        x = 0
        for j in range(strip.numPixels()):
            x += 1
        
        z = round(x/30)                            #edit to effect color lights/meter
        var1 = random.randrange(0, x)           #edit to effect color lights/meter
        var2 = random.randrange(1, 4)
        color_array = []
        color_array.append(var1) 

        while len(color_array) < z:
            color_array.append(color_array[len(color_array) - 1] + 30)

        print(color_array)

        if var2 == 1:
            y = 0
            for y in range(x):
                if y in color_array:
                    strip.setPixelColor(y, Color(255, 0, 0))

                else: 
                    strip.setPixelColor(y, Color(255,255,255))
                              
            strip.show()
            
        elif var2 == 2:
            y = 0
            for y in range(x):
                if y in color_array:
                    strip.setPixelColor(y, Color(0, 255, 0))

                else: 
                    strip.setPixelColor(y, Color(255,255,255))
                    
            strip.show()
            
        elif var2 == 3:
            y = 0
            for y in range(x):
                if y in color_array:
                    strip.setPixelColor(y, Color(0, 0, 255))

                else: 
                    strip.setPixelColor(y, Color(255,255,255))
                    
            strip.show()
            
        status = "DONE"
        time.sleep(wait_s)
        return status

def new_brightness(brightness):
    #print(LED_BRIGHTNESS)
    brightness = int(brightness)
    new_brightness = int(255 * (brightness/100))
    #print(new_brightness)
    if new_brightness != LED_BRIGHTNESS:
        #print(new_brightness)
        light_strips(new_brightness)
    else:
        return

def light_strips(new_brightness):
    global strip
    global LED_BRIGHTNESS
    #print(LED_BRIGHTNESS)
    #print(new_brightness)
    if new_brightness != LED_BRIGHTNESS:
        LED_BRIGHTNESS = new_brightness
        #print(LED_BRIGHTNESS)
        #strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.setBrightness(new_brightness)
        