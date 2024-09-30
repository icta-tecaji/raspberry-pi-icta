# Del 2: Priprava okolja in prva uporaba

## Namestitev Raspbian Linux

Namestitev Raspbian ni podobna namestitvi klasičnega operacijskega sistema (vstavitev instalacijskega medija, grafično instalacijsko okolje, nastavitve, ter ponovni zagon v novi sistem) - namestitev opravimo z prenosom pripravljene slike na SD kartico. Pripravljena slika vsebuje celotno kopijo “izvorne” sd kartice (vsebuje tudi podatke o morebitnih particijah, MBR, ter vso vsebino datotečnega sistema). Za kopiranje slike na kartico moramo prepisati celotno kartico (tudi datotečni sistem), zato potrebujemo poseben program, ki direktno prepisuje kartico.

1. Namestimo orodje **Raspberry Pi Imager** iz strani https://www.raspberrypi.org/software/, ki nam omogoča pisanje slike na SD kartico.
2. Vstavimo SD kartico v računalnik.
3. Zaženemo Raspberry Pi Imager in namestimo OS.
    - Izberemo preneseno sliko (lahko uporabimo tudi opcijo, da Raspberry Pi Imager samodejno prenese želeno sliko).
        - Obstajajo tri osnovne verzije - *with desktop*, *Lite* in *with desktop and recommended software*. Desktop verzija vsebuje več programske opreme in celoten grafični vmesnik - taka je primerna za direktno uporabo. V našem primeru izberemo Lite verzijo, saj ne bomo potrebovali grafičnega vmesnika.
        - Izberemo 64-bitno verzijo `Raspberry Pi OS (64-bit) - Raspberry Pi OS Lite, Debian version: 12 (bookworm)`.
    - Izberemo SD kartico na katero želimo zapisati podatke.
    - S klikom na spodnji kolešček za natavitve pripravimo RP za prvo uporabo (določimo hostname, vklopimo SSH, nastavimo uporabniško ime in geslo, nastavimo wifi, izberemo tipkovnico).
    - Izberemo možnost, da počistimo vsebino celotne kartice pred pisanjem.

## Nastavitev Wifi
- **Opcija 1: S uporabo Raspberry Pi Imager**: V nastavitvah pred namestitvijo OS-ja na SD kartico lahko vnesemo podatke WiFi-omrežja na katerga se bomo povezali.
- **Opcija 2: Ethernet kabel + Raspi-config orodje**: Raspberry Pi povežemo preko Ethernet kabla v ruter. poiščemo IP naprave in se preko SSH povezave povežemo na RPi. Izvedemo ukaz `sudo raspi-config` in nato izberemo `System Options` ter `Wireless LAN`. Sledimo navodilom in dodamo novo WiFi omrežje. 

> Privzeto je v našem primeru WiFI SSID ime `rpi-delavnica` in geslo `rpi-delavnica`.

## Zagon
1. Po končanem kopiranju nadaljujemo z zagonom RP.
2. SD kartico vstavite v RaspberryPi.
3. Priklopite napajanje (Micro USB kabel) in po potrebi Ethernet kabel.
4. Če je vse potekalo pravilno, bi se moral RPi zagnati v kakšni minuti.

## Upravljanje na daljavo (SSH)
Za upravljanje na daljavo uporabimo protokol SSH: `ssh <uporabnisko ime>@<IP naslov>`. V našem primeru je uporabniško ime `pi` in IP naslov najdemo na ruterju.

> Primer: `ssh pi@192.168.0.53`

Pri povezavi nas vpraša za geslo (za naš primer: raspberry). 

> Pazimo, da imamo močno geslo! 

Sejo prekinemo z ukazom `exit`. Protokol SSH uporablja TCP port 22.
