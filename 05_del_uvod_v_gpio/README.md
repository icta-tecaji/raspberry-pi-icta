# Del 5: Uvod v GPIO

Za lažje delo s Raspberry Pi pini lahko uporabimo [spletna orodja](https://pinout.xyz/), ki podpirajo interaktivni opis pinov.

## Uporaba GPIO pinov
1. RaspberryPi izklopite (odklopite USB napajalni kabel). Pazite na statično elektriko (dotaknite se nečesa ozemljenega, naprimer kovinskega dela mize), in zatem USB-A konektorja na RaspberryPi. LED diodo priklopite med Ground pin (09) in GPIO17 (GPIO GEN0) (11). To sta peti in šesti pin v levi vrsti.
2. Pazite na polariteto - na pozitivni strani (anodi) diode je vezan upor - povezava gre z GPIO17 (/Pin11/GPIO GEN0) prek upora na led diodo in nazaj na ground.
3. RaspberryPi prižgite nazaj.

Stanje in pregled pinov lahko preverimo z ukazom:
- `sudo pinctrl`
- Pomoč: `sudo pinctrl help`

GPIO17 pin (interna številka 0) nastavimo na output - tako da nastavljamo logično stanje (napetost3.3V ali 0V) - pri input jo beremo.
- `sudo pinctrl set 17 op`

Nastavimo stanje na 1 (3.3V):
- `sudo pinctrl set 17 dh`
- LED dioda se prižge.

Stanje nastavimo nazaj na 0 (0V):
- `sudo pinctrl set 17 dl`

Ukaza lahko uporabimo tudi v skripti (utripanje):
- `while true; do sudo pinctrl set 17 dh; sleep 0.5; sudo pinctrl set 17 dl; sleep 0.5; done`
- `sudo pinctrl set 17 dl`


### Vaja 1: Led osnovno
- Premaknemo se v mapo `cd ~/raspberry-pi-icta/05_del_uvod_v_gpio`
- Za vaje bomo uporabili knjižnico `gpiozero`. [Primeri](https://gpiozero.readthedocs.io/en/latest/recipes.html).

> GPIO Zero is installed by default in the Raspberry Pi OS desktop image, Raspberry Pi OS Lite image, and the Raspberry Pi Desktop image for PC/Mac, all available from raspberrypi.org. This library uses Broadcom (BCM) pin numbering for the GPIO pins, as opposed to physical (BOARD) numbering. Unlike in the RPi.GPIO library, this is not configurable.

- Uporabimo program: `cat 01_led_osnovno.py`
- Zagon:
    - `python3 01_led_osnovno.py`

### Vaja 2: Led blink
- Utrip na vsake dve sekundi.
- Uporabimo program: `02_led_blink.py`
- Zagon:
    - `python3 02_led_blink.py`

### Vaja 3: Led PWM
- Uporabimo program: `03_led_pwm.py`
- Zagon:
    - `python3 03_led_pwm.py`
