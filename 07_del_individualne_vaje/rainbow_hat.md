# Rainbow HAT

![alt text](./images/rainbow.png)


Rainbow HAT je dodatk za RaspberryPi z 8x8 RGB LED matriko. Omogoča prikazovanje raznih simoblov z barvami, barvno osvetlitev, ter prikaz enostavnih animacij.
- https://github.com/allocom/Rainbow-HAT


Navodila za namestitev (tudi na linku zgoraj za copy-paste):
```bash
git clone https://github.com/allocom/rainbow-hat
cd rainbow-hat/
sudo apt-get install python-dev python-setuptools
cd library/RainbowHat
sudo python setup.py install
cd ../..
cd library/rpi-ws281x
sudo python setup.py install
cd ../..
```
Pomaknite se v enega izmed direktorijev z primeri in poženite primere (primere poženemo s `sudo
python ime_primera.py`):
```bash
cd ./examples
#...ali...
cd ./examples/hat
```

Na ekran lahko rišete tudi ročno, tako da poženete python (sudo python) in uporabite naslednje ukaze:
```python
import rainbowhat as rainbow
import time
rainbow.set_layout(rainbow.HAT)
rainbow.set_pixel(X,Y,R,G,B)
rainbow.show()
time.sleep(10)
```

Prvi dve vrstici vključita knjižnico za HAT in časovne funkcije, tretja inicializira objekt, v četrti nastavimo barvo/svetlost vsake pike (X, Y koordinate - od 0 do 7 - 0,0 = levo zgoraj, 7,7 je desno spodaj; R,G,B so barvne komponente, od 0 do 255), v predzadnji vrstici nastavljene pike prikažemo na displayu, potem pa sledi še sleep (toliko časa ostanejo pike prižgane).

Primer:
- `rainbow.set_pixel(2,3,255,0,0)`
