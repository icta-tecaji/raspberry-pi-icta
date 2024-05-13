from gpiozero import LED
from time import sleep

led_01 = LED(17)

led_01.on()
print("LED on")
sleep(2)
led_01.off()
print("LED off")
sleep(2)
