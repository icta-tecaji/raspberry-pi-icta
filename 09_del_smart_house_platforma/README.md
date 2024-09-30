# Del 9: Smart house platforma

V zadnji nalogi bomo izdelali pametno vremensko postajo s pomočjo senzorja BMP280 (temperatura in tlak) in pridobljenje podatke preko Flask serverja pošiljali v Prometheus in jih nato prikazali v Grafani.

Pred začetkom vaje moramo odpreti sledeča vrata:
- `sudo ufw allow 5000`
- `sudo ufw allow 5001`
- `sudo ufw allow 5002`

## Povezava senzorja BMP280

Senzor za komunikacijo z Raspberry Pi uporablja I2C komunikacijo. Na RPi 5 po defaultu protokol I2C ni vklopljen. Naredimo naslednje korake:
- V terminalu: `sudo raspi-config` 
- Interface Options -> I2C -> ENABLE -> ok -> Finish
- `sudo reboot`

Naslednji  korak je **povezava senzorja** BMP280  na Raspberry Pi. Pine povežemo na naslednji način:
* VCC -> 3.3V
* GND -> GND
* SCL -> SCL (GPIO 3)
* SDA -> SDA (GPIO 2)

> **SDO (Serial Data Out) Pin Functionality**: The SDO pin is used to configure the I2C address of the BMP280. By connecting the SDO pin to ground (GND), the device defaults to an I2C address of 0x76. Connecting the SDO pin to the 3.3V supply sets the device address to 0x77. Default Address: The BMP280 module is shipped with the SDO pin connected to ground by default, setting the I2C address to 0x76.

Preverimo, če je senzor pravilno povezan:
- `sudo apt-get update`
- `sudo apt-get install -y i2c-tools`
- `sudo i2cdetect -y 1`
- Kazati bi moralo številko "76" ali "77".

## Python skripta
Podatke bomo iz senzorja brali s pomočjo Python skripte `main.py`. Pred zagonom skripte moramo namestiti dodatno knjižnico, ki nam nudi povezavo s senzorjem BMP280:
- Premaknemo se v mapo: `cd ~/raspberry-pi-icta/09_del_smart_house_platforma`
- Ustvarimo virtualno okolje: 
    - `python3 -m venv .venv --system-site-packages`
    - `source .venv/bin/activate`
- Blinka Install:
    - `pip3 install --upgrade adafruit-python-shell`
    - `wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py`
    - `sudo -E env PATH=$PATH python3 raspi-blinka.py`
- Reboot the Raspberry Pi: `sudo reboot`
- Po ponovnem zagonu se premaknemo v mapo:
    - `cd ~/raspberry-pi-icta/09_del_smart_house_platforma`
- `rm raspi-blinka.py`
- `source .venv/bin/activate`
- The script will automatically enable I2C and SPI. You can run the following command to verify: `ls /dev/i2c* /dev/spi*`
- Installing the CircuitPython-BMP280 Library:
    - `pip3 install adafruit-circuitpython-bmp280`
    - `pip3 install Flask`
- V skripti prilagodimo zračni tlak po potrebi.
- Zaženemo program: `python3 main.py`
- Po zagonu bi morali na URL nalsovu `http://<RPI_IP>:5000/metrics` videti izpis trenutnih metrik.

## Prometheus in Grafana

[Prometheus](https://prometheus.io/) je monitoring sistem, ki lahko zbira metrike iz različnih URLjev v nastavljenih intervalih. Zbrane podatke nato s pomočjo [Grafane](https://grafana.com/) prikažemo na nadzorni plošči.
 
Konfiguracija za Prometheus je shranjena v datoteki `prometheus.yml`. Pred zagonom moramo nadomestiti IP spremenljivke `targets` z IP-jem lastnega RPI-ja.

V naslednjem koraku v novem terminalu zaženemo Prometheus in Grafano:
- `sudo docker compose up -d`
- `sudo docker compose ps`

Do nadzorne plošče lahko dostopimo na naslovu:
- Prometheus `http://<RPI_IP>:5001/`
- Grafana `http://<RPI_IP>:5002/`

Prijavimo se v Grafana nadzorno ploščo in ustvarimo nov `Data source` (Connections -> Data Sources -> Add data source -> Prometheus). Poimenujemo ga `BMP280` in dodamo URL do Prometheus-a. Izberemo gumb `Save & test`

Naslednji korak je prikaz izmerjenih podatkov na nadzorni plošči. Ustvarimo nov objekt `Dashboard` (Dashboards -> New Dashboard -> Add visualization) in dodamo podatke za temperaturo in pritisk v ločena *panela*. Na koncu dashboard shranimo.

Po končanem delu lahko zadeve odstranimo z ukazom `sudo docker compose down -v` in ustavimo Python skripto.

Izklopimo skripto in deaktiviramo virtualno okolje: `deactivate`
