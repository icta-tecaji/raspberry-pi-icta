# Del 9: Smart house platforma

V zadnji nalogi bomo izdelali pametno vremensko postajo s pomočjo senzorja DHT11 (temperatura in vlaga) in pridobljenje podatke preko Flask serverja pošiljali v Prometheus in jih nato prikazali v Grafani.

Pred začetkom vaje moramo odpreti sledeča vrata:
- `sudo ufw allow 5000`
- `sudo ufw allow 5001`
- `sudo ufw allow 5002`

## Povezava senzorja DHT11

Prvi korak je [povezava senzorja DHT11](https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/) na Raspberry Pi. Pomagate si lahko s spodnjo sliko.

![DHT11](./dht11.png)

Uporabimo upor z 10 kOhm med Vcc in signal pinom. Povezave:
- Rdeča žička: 5V (pin 2)
- Črna žička: GND (pin 6)
- Modra žička: signal (pin 7/GPIO4)

Podatke bomo iz senzorja brali s pomočjo Python skripte `main.py`. Pred zagonom skripte moramo namestiti dodatno knjižnico, ki nam nudi povezavo s senzorjem DHT11:
- Premaknemo se v mapo: `cd ~/raspberry-pi-icta/09_del_smart_house_platforma`
- `sudo apt-get update`
- `sudo apt-get -y upgrade`
- `sudo apt-get install python3-pip`
- `sudo apt install --upgrade python3-setuptools`
- If you are installing on the Bookworm version of Raspberry Pi OS, you will need to install your python modules in a virtual environment:
    - `sudo apt install python3-venv`
    - `python3 -m venv .venv --system-site-packages`
    - `source .venv/bin/activate`
- Blinka Install:
    - `pip3 install --upgrade adafruit-python-shell`
    - `wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py`
    - `sudo -E env PATH=$PATH python3 raspi-blinka.py`
- Reboot the Raspberry Pi
- `cd ~/raspberry-pi-icta/09_del_smart_house_platforma`
- `source .venv/bin/activate`
- The script will automatically enable I2C and SPI. You can run the following command to verify: `ls /dev/i2c* /dev/spi*`
- Blinka Test: `python3 blinkatest.py`
- Installing the CircuitPython-DHT Library:
    - `pip3 install adafruit-circuitpython-dht`
    - `sudo apt-get install libgpiod2`
    - `pip3 install Flask`



- `pip install Adafruit_Python_DHT`

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

Prijavimo se v Grafana nadzorno ploščo in ustvarimo nov `Data source` (Connections -> Data Sources -> Add data source -> Prometheus). Poimenujemo ga `DHT11` in dodamo URL do Prometheus-a. Izberemo gumb `Save & test`

Naslednji korak je prikaz izmerjenih podatkov na nadzorni plošči. Ustvarimo nov objekt `Dashboard` (Dashboards -> New Dashboard -> Add visualization) in dodamo podatke za temperaturo in vlago v ločena *panela*. Na koncu dashboard shranimo.

Po končanem delu lahko zadeve odstranimo z ukazom `sudo docker compose down -v` in ustavimo Python skripto.
