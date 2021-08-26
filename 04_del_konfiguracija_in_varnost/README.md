# Del 4: Konfiguracija, omrežne nastavitve in varnost

## Upravljanje na daljavo (SSH)
Omogočimo SSH povezavo:
- Odpremo novi terminal
- Vnesemo `sudo raspi-config`
- Izberemo: `Interfacing Options -> SSH -> Yes -> Ok -> Finish`

Za upravljanje na daljavo uporabimo protokol SSH, primer:
`ssh <uporabnisko ime>@<IP naslov>`

> Naprimer: `ssh pi@10.60.60.123`

Pri povezavi nas vpraša za geslo. 

> Pazimo, da imamo močno geslo! 

Sejo prekinemo z ukazom exit. Protokol SSH uporablja TCP port 22.

### Konfugracija SSH brez dodatnega ekrana
- @Balki TODO
- Na hitr midva pokaževa kako se usposobi RP, če nimaš ekrana (.ssh datoteko nrdiš in pol sshajat gor itd..)..
- Ampak ne rabjo vsi takrt z nama sledit temu..
- Kle bi rabl dodatno SD kartico da jo lahko tm takoj formatiramo in na sveže naložimo sistem

## Pridobimo kodo za tečaj iz računa Github
Da boste lahko lažje sledili tečaju lahko vsebino in kodo naložite na RaspberryPi s kloniranjem pripravljenega Github repozitorija.
- se premaknemo v mapo uporabnika pi: `cd /home/pi`
- Zaženemo: `git clone https://github.com/leon11s/raspberry-pi-icta.git`


## Nastavitev statičnega IP naslova
Če uporabljamo RaspberryPi prek oddaljenega dostopa (SSH), ali kot strežnik, ali pa ga le želimo imeti bolj pod kontrolo, moramo nastaviti statični IP naslov.

Z ukazom `ifconfig` preverimo trenutne omrežne nastavitve.

Statični IP (za razliko od ostalih Linux distribucij baziranih na Debian-u) nastavljamo v dhcpcd.conf datoteki:
- `sudo nano /etc/dhcpcd.conf`

Vpraša nas za geslo, nato se odpre datoteka z mrežnimi nastavitvami. Večina vsebine je zakomentirane. Dodeljen vam bo IP iz 192.168.1.2/24 - 192.168.1.20/24 obsega (pazite da ne uporabite istega kot kdo drug v skupini). Za statično nastavitev IPja na začetek datoteke vpišemo:

```bash
interface wlan0
static ip_address=192.168.1.X/24
static routers=192.168.1.1
static domain_name_servers=8.8.8.8
```

RaspberryPi ponovno zaženemo (ukaz `sudo reboot`), in z ukazom `ifconfig` preverimo, če je nastavljen pravilen IP.
Povezljivost lahko preveri tudi sosed z ukazom ping:
- `ping <vaš IP naslov>`

## Požarni zid
Za nastavljanje požarnega zidu uporabljamo UFW (Uncomplicated Firewall), ki vpredstavlja enostaven vmesnik za program `iptables`. `iptables` je zelo močno in fleksibilno orodje, vendar lahko predstavlja težavo začetnikom.

Namestimo UFW:
- `sudo apt update -y`
- `sudo apt install -y ufw`

Preverimo stanje (trenutno je program UFW še neaktiven):
- `sudo ufw status`

Nastavimo privzete možnosti:
- `sudo ufw default deny incoming`
- `sudo ufw default allow outgoing`

Omogočimo dostop za SSH in HTTP za vse IPje:
- Pravila se izvajajo v vrstnem redu, kot so
napisana.
- `sudo ufw allow 22`
- `sudo ufw allow 80`

Omogočimo UFW:
- `sudo ufw enable`
- Preverimo stanje: `sudo ufw status`

Ostali primeri konfiguracije:
- `sudo ufw allow from 203.0.113.4`
- `sudo ufw allow from 203.0.113.4 to any port 22`
- `sudo ufw allow from 203.0.113.0/24`
- `sudo ufw allow from 203.0.113.0/24 to any port 22`
- `sudo ufw deny http`
- `sudo ufw deny from 203.0.113.4`

Brisanje pravil:
- `sudo ufw status numbered`
- `sudo ufw delete 2`

Z sosedom lahko preverite delovanje pravil.

## Varnost
- Sprememba privzetega gesla
- Dodajanje novega uporabnika
- Zahtevamo geslo za sudo za vsako operacijo
- Preverimo posodobitve sistema
- Avtomatizacija opravil (Avtomatsko posodabljanje)
- Uporaba [Fail2ban](https://www.fail2ban.org/wiki/index.php/Main_Page)
    - Fail2ban je program, ki pregleduje log datoteke in na podlagi našega filtra blokira sumljive IP naslove.

