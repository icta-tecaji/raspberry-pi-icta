import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

p = GPIO.PWM(17, 0.5)
p.start(1)
input('Press enter to stop!')  
print("Stopping!")
p.stop()
GPIO.cleanup()