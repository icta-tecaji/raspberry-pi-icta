from gpiozero import LED
from time import sleep

led_01 = LED(17)

try:
    print("Press CTRL+C to stop the program!")
    print()
    while True:
        led_01.on()
        print("LED on")
        sleep(2)
        led_01.off()
        print("LED off")
        sleep(2)
except KeyboardInterrupt:
    print("Stopping!")
    led_01.off()
