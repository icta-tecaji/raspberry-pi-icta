# LCD zaslon

- Tutorials:
    - https://github.com/sterlingbeason/LCD-1602-I2C
    - https://nerdcave.xyz/raspberrypi/module-and-sensors/tutorial-lcd-1602/
    - https://www.youtube.com/watch?v=V8J33fvCIUs

## Vezava LCD zaslona

Vezava:
- VCC -> 5V
- GND -> GND
- SDA -> SDA
- SCL-> SCL

I2C komunikacija mora biti vklopljena.

Preverimo I2C naslov:
- Check for connected device addresses:
- `sudo apt-get update`
- `sudo apt-get install -y i2c-tools`
- `sudo i2cdetect -y 1`
- Naslov je 0x27 ali 0x3f


## Python koda

- Naredimo novo datoteko `lcd_hello.py` in vnesemo naslednjo kodo:

```python
import time
from lcd import LCD

lcd = LCD(i2c_addr=0x3f)

lcd.message("Hello World!", 1) # display 'Hello World!' on line 1 of LCD

time.sleep(5) # wait 5 seconds

lcd.clear() # clear LCD display
```

- Zaženemo program: `python3 lcd_hello.py`
