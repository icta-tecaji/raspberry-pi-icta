# Del 2: Priprava okolja in prva uporaba

## Namestitev Raspbian Linux

Namestitev Raspbian ni podobna namestitvi klasičnega operacijskega sistema (vstavitev instalacijskega medija, grafično instalacijsko okolje, nastavitve, ter ponovni zagon v novi sistem) - namestitev opravimo z prenosom pripravljene slike na SD kartico. Pripravljena slika vsebuje celotno kopijo “izvorne” sd kartice (vsebuje tudi podatke o morebitnih particijah, MBR, ter vso vsebino datotečnega sistema). Za kopiranje slike na kartico moramo prepisati celotno kartico (tudi datotečni sistem), zato potrebujemo poseben program, ki direktno prepisuje kartico.

1. Prenesemo sliko z operacijskim sistemom iz strani: https://www.raspberrypi.com/software/operating-systems/
    - Na spletni strani obstajata dve verziji -  *with desktop* in *Lite*. Desktop verzija vsebuje več programske opreme in celoten grafični vmesnik - taka je primerna za direktno uporabo. V našem primeru izberemo Lite verzijo, saj ne bomo potrebovali grafičnega vmesnika.
    - Izberemo 64-bitno verzijo: `Raspberry Pi OS (64-bit) - Raspberry Pi OS Lite, Debian version: 11 (bullseye)`. 
    - Datoteko shranimo na računalnik.
2. Namestimo orodje **Raspberry Pi Imager** iz strani https://www.raspberrypi.org/software/, ki nam omogoča pisanje slike na SD kartico.
3. Vstavimo SD kartico v računalnik.
4. Zaženemo Raspberry Pi Imager in namestimo OS.
    - Izberemo preneseno sliko (lahko uporabimo tudi opcijo, da Raspberry Pi Imager samodejno prenese želeno sliko).
    - Izberemo SD kartico na katero želimo zapisati podatke.
    - S klikom na spodnji kolešček za natavitve pripravimo RP za prvo uporabo (določimo hostname, vklopimo SSH, nastavimo uporabniško ime in geslo, nastavimo wifi, izberemo tipkovnico).
    - Izberemo možnost, da počistimo vsebino celotne kartice pred pisanjem.

## Nastavitev Wifi
- **Opcija 1: S uporabo Raspberry Pi Imager**: V nastavitvah pred namestitvijo OS-ja na SD kartico lahko vnesemo podatke WiFi-omrežja na katerga se bomo povezali.
- **Opcija 2: Uporaba wpa_supplicant.conf datoteke**: Vstavimo kartico v računalnik in odpremo `boot` mapo na SD kartici. V mapi ustvarimo novo datoteko `wpa_supplicant.conf` v katero skopiramo naslednjo vsebino in nato kartico odstranimo iz računalnika:
```conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=SI

network={
        ssid="SSID"
        psk="GESLO"
}
```
- **Opcija 3: Ethernet kabel + Raspi-config orodje**: Raspberry Pi povežemo preko Ethernet kabla v ruter. poiščemo IP naprave in se preko SSH povezave povežemo na RPi. Izvedemo ukaz `sudo raspi-config` in nato izberemo `System Options` ter `Wireless LAN`. Sledimo navodilom in dodamo novo WiFi omrežje. 

## Zagon
1. Po končanem kopiranju nadaljujemo z zagonom RP.
2. SD kartico vstavite v RaspberryPi.
3. Priklopite napajanje (Micro USB kabel) in po potrebi Ethernet kabel.
4. Če je vse potekalo pravilno, bi se moral RPi zagnati v kakšni minuti.

## Upravljanje na daljavo (SSH)
Za upravljanje na daljavo uporabimo protokol SSH: `ssh <uporabnisko ime>@<IP naslov>`

> Primer: `ssh pi@192.168.3.127`

Pri povezavi nas vpraša za geslo (npr. delavnica). 

> Pazimo, da imamo močno geslo! 

Sejo prekinemo z ukazom `exit`. Protokol SSH uporablja TCP port 22.
