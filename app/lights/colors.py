import time, random, io
from rpi_ws281x import *

    global strip

    # LED strip configuration
    LED_COUNT      = 150      # Number of LED pixels.
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


def set_color(status_array):
    new_brightness(status_array[0])
    if check is True:
        if status_array[1] == 'WIPE':
            wipe_color(strip, Color(int(status_array[2]), int(status_array[3]), int(status_array[4])))
        elif status_array[1] == 'SOLID':
            solid_color(strip, Color(int(status_array[2]), int(status_array[3]), int(status_array[4])))
    else:
        print("current state:", status_array[1])
        print("color code:", int(status_array[2]), int(status_array[3]), int(status_array[4]))


def wipe_color(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def solid_color(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()


def rainbow(brightness, wait_ms=20, iterations=1):
    new_brightness(brightness)
    if check is True:
        for j in range(256*iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel((i+j) & 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
    else:
        print("Running Rainbow")
        time.sleep(1)


def rainbow_cycle(brightness, wait_ms=20, iterations=1):
    new_brightness(brightness)
    if check is True:
        for j in range(256*iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
    else:
        print("Running Rainbow Cycle")
        time.sleep(1)


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
    z = 2                                       #Lights/meter edit this to increase or decrease the amount of twinkling lights per meter
    r = random.randrange(0, 3)
    y = random.randrange(1, ((30/z) + 1))
    new_y = y
    if check is True:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(255, 255, 255))
        x = strip.numPixels()
        if r == 0:
            while new_y <= x:
                if new_y <= x:
                    strip.setPixelColor(new_y, Color(255, 0, 0))
                    new_y = new_y + y
                else:
                    break
        elif r == 1:
            while new_y <= x:
                if new_y <= x:
                    strip.setPixelColor(new_y, Color(0, 128, 0))
                    new_y = new_y + y
                else:
                    break
        elif r == 2:
            while new_y <= x:
                if new_y <= x:
                    strip.setPixelColor(new_y, Color(0, 0, 255))
                    new_y = new_y + y
                else:
                    break
        strip.show()
        time.sleep(wait_s)
    else:
        print("Runninng RGB Twinkle")
        x = 150
        if r == 0:
            while new_y <= x:
                if new_y <= x:
                    print(f' set pixel {new_y} to Red')
                    print("old y:", new_y)
                    new_y = new_y + y
                    print("new y:", new_y)
                    print()
                else:
                    print("break")
                    break
        elif r == 1:
            while new_y <= x:
                if new_y <= x:
                    print(f' set pixel {new_y} to Green')
                    print("old y:", new_y)
                    new_y = new_y + y
                    print("new y:", new_y)
                    print()
                else:
                    print("break")
                    break
        elif r == 2:
            while new_y <= x:
                if new_y <= x:
                    print(f'set pixel {new_y} to Blue')
                    print("old y:", new_y)
                    new_y = new_y + y
                    print("new y:", new_y)
                    print()
                else:
                    print("break")
                    break
        time.sleep(wait_s)


def num_pattern(status_array):
    new_brightness(status_array[0])
    num = int(status_array[1])
    code1 = status_array[2]
    code2 = status_array[3]
    if check is True:
        i = 1
        j = 1 + num
        new_num = num
        while i < int(strip.numPixels()):
            while i <= new_num:
                strip.setPixelColor(i, Color(code1[0], code1[1], code1[2]))
                i += 1
            new_num = (new_num + num + num)
            i = i + num
            while j <= (new_num - num):
                if j <= int(strip.numPixels()):
                    strip.setPixelColor(j, Color(code2[0], code2[1], code2[2]))
                    j += 1
                else:
                    break
            j = j + num
        strip.show()
    else:
        print("Pattern Number:", num)
        print("First Color:", code1)
        print("Second Color:", code2)
        print()

        items = 150
        i = 1
        j = 1 + num
        new_num = num
        while i < items:
            while i <= new_num:
                print("code1:", i)
                i += 1
            print()
            print("old num:", new_num)
            new_num = (new_num + num + num)
            print("new num:", new_num)
            i = i + num
            print("new i:", i)
            print()

            while j <= (new_num - num):
                if j <= items:
                    print("code2:", j)
                    j += 1
                else:
                    break
            j = j + num
            print()
            print("new j:", j)
            print()


def new_brightness(brightness):
    if check is True:
        global strip
        global LED_BRIGHTNESS

    brightness = int(brightness)
    new_brightness = int(255 * (brightness/100))
    if check is True:
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
    if check is True:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(r, g, b))
        strip.show()
    else:
        print("Changing Color Changer")


def rainbow_theater_chase(brightness, speed, wait_ms=50):
    new_brightness(brightness)
    if check is True:
        for j in range(256):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, wheel((i+j) % 255))
                strip.show()
                if speed == 'SLOW':
                    time.sleep(wait_ms/100.0)
                elif speed == 'MEDIUM-SLOW':
                    time.sleep(wait_ms/200.0)
                elif speed == 'MEDIUM':
                    time.sleep(wait_ms/80)
                elif speed == 'MEDIUM-FAST':
                    time.sleep(wait_ms/500.0)
                else:
                    time.sleep(wait_ms/1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, 0)
    else:
        print("Running Rainbow Theater Chase")
        print(f'Current speed is {speed}')
        time.sleep(wait_ms/10)


def rainbow_cycle_theater_chase(brightness, speed, wait_ms=50):
    new_brightness(brightness)
    if check is True:
        for j in range(256):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
                strip.show()
                if speed == 'SLOW':
                    time.sleep(wait_ms / 100.0)
                elif speed == 'MEDIUM-SLOW':
                    time.sleep(wait_ms / 200.0)
                elif speed == 'MEDIUM':
                    time.sleep(wait_ms / 80)
                elif speed == 'MEDIUM-FAST':
                    time.sleep(wait_ms / 500.0)
                else:
                    time.sleep(wait_ms / 1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, 0)
    else:
        print("Running Rainbow Cycle Theater Chase")
        print(f'Current speed is {speed}')
        time.sleep(wait_ms/10)


def color_theater_chase(status_array, wait_ms=50):
    new_brightness(status_array[0])
    speed = status_array[1]
    code1 = status_array[2]
    code2 = status_array[3]
    if check is True:
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, Color(code1[0], code1[1], code1[2]))
            strip.show()
            if speed == 'SLOW':
                time.sleep(wait_ms / 100.0)
            elif speed == 'MEDIUM-SLOW':
                time.sleep(wait_ms / 200.0)
            elif speed == 'MEDIUM':
                time.sleep(wait_ms / 80)
            elif speed == 'MEDIUM-FAST':
                time.sleep(wait_ms / 500.0)
            else:
                time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, Color(code2[0], code2[1], code2[2]))
    else:
        print("Running Color Theater Chase")
        print(f'Current speed is {speed}')
        time.sleep(wait_ms/10)


def theater_chase(brightness, speed, wait_ms=50):
    new_brightness(brightness)
    if check is True:
        if speed == 'SLOW':
            sleep = (wait_ms / 100.0)
        elif speed == 'MEDIUM-SLOW':
            sleep = (wait_ms / 200.0)
        elif speed == 'MEDIUM':
            sleep = (wait_ms / 80)
        elif speed == 'MEDIUM-FAST':
            sleep = (wait_ms / 500.0)
        else:
            sleep = (wait_ms / 1000.0)
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, Color(255, 255, 255))
            strip.show()
            time.sleep(sleep)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)
    else:
        print("Running Theater Chase")
        print(f'Current speed is {speed}')
        time.sleep(wait_ms/10)


def rgb_cycle(brightness, speed, wait_ms=50):
    new_brightness(brightness)
    if check is True:
        if speed == 'SLOW':
            sleep = (wait_ms / 100.0)
        elif speed == 'MEDIUM-SLOW':
            sleep = (wait_ms / 200.0)
        elif speed == 'MEDIUM':
            sleep = (wait_ms / 80)
        elif speed == 'MEDIUM-FAST':
            sleep = (wait_ms / 500.0)
        else:
            sleep = (wait_ms / 1000.0)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(255, 0, 0))
        strip.show()
        time.sleep(sleep)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 255))
        strip.show()
        time.sleep(sleep)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 128, 0))
        strip.show()
        time.sleep(sleep)

    else:
        print("Running rgb_cycle")
        print(f'Current speed is {speed}')
        time.sleep(wait_ms/10)


def random_cycle(brightness, speed, wait_ms=50):
    new_brightness(brightness)
    if check is True:
        if speed == 'SLOW':
            sleep = (wait_ms / 100.0)
        elif speed == 'MEDIUM-SLOW':
            sleep = (wait_ms / 200.0)
        elif speed == 'MEDIUM':
            sleep = (wait_ms / 80)
        elif speed == 'MEDIUM-FAST':
            sleep = (wait_ms / 500.0)
        else:
            sleep = (wait_ms / 1000.0)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)))
        strip.show()
        time.sleep(sleep)

    else:
        print("Running random_cycle")
        print(f'Current speed is {speed}')
        time.sleep(wait_ms/10)
