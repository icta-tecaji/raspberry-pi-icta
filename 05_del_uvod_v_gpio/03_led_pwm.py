from gpiozero import PWMLED
import time

led_01 = PWMLED(17)

try:
    print("Press CTRL+C to stop the program!")
    print()
    while True:
        for dc in range(0, 100, 5):
            led_01.value = dc / 100
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            led_01.value = dc / 100
            time.sleep(0.1)
except KeyboardInterrupt:
    print("Stopping!")
    led_01.off()
