import time
from lcd import LCD

lcd = LCD(i2c_addr=0x3f)

lcd.message("Hello World!", 1) # display 'Hello World!' on line 1 of LCD

time.sleep(5) # wait 5 seconds

lcd.clear() # clear LCD display
