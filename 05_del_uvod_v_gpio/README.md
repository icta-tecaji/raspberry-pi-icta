# Del 5: Uvod v GPIO

## GPIO



## Uporaba GPIO pinov
1. RaspberryPi izklopite (odklopite USB napajalni kabel). Pazite na statično elektriko (dotaknite se nečesa ozemljenega, naprimer kovinskega dela mize), in zatem USB-A konektorja na RaspberryPi. LED diodo priklopite med Ground pin (09) in GPIO17 (GPIO GEN0) (11). To sta tretji in četrti pin v levi vrsti.
2. Pazite na polariteto - na pozitivni strani (anodi) diode je vezan upor - povezava gre z GPIO17 (/Pin11/GPIO GEN0) prek upora na led diodo in nazaj na ground.
3. RaspberryPi prižgite nazaj.

Stanje in pregled pinov lahko preverimo z ukazom:
- `gpio readall`

GPIO17 pin (interna številka 0) nastavimo na output - tako da nastavljamo logično stanje (napetost3.3V ali 0V) - pri input jo beremo.
- `gpio mode 0 out`

Nastavimo stanje na 1 (3.3V):
- `gpio write 0 1`
- LED dioda se prižge.

Stanje nastavimo nazaj na 0 (0V):
- `gpio write 0 0`

Ukaza lahko uporabimo tudi v skripti:
- `while true; do gpio write 0 1; sleep 0.5; gpio write 0 0; sleep 0.5; done`


### Vaja 1: Led osnovno
- Uporabimo program: `01_led_osnovno.py`
- Zagon:
    - premaknemo se v mapo s skripto
    - `sudo python3 01_led_osnovno.py`

### Vaja 2: Led blink
- Utrip na vsake dve sekundi.
- Uporabimo program: `02_led_blink.py`
- Zagon:
    - premaknemo se v mapo s skripto
    - `sudo python3 02_led_blink.py`

### Vaja 3: Led PWM
- Uporabimo program: `03_led_pwm.py`
- Zagon:
    - premaknemo se v mapo s skripto
    - `sudo python3 03_led_pwm.py`
