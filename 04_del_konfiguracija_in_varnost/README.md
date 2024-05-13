# Del 4: Konfiguracija, omrežne nastavitve in varnost

## Pridobimo kodo za tečaj iz računa Github
Da boste lahko lažje sledili tečaju lahko vsebino in kodo naložite na RaspberryPi s kloniranjem pripravljenega Github repozitorija.
- se premaknemo v mapo uporabnika pi: `cd /home/pi`
- Preverimo ali imamo nameščen git: `git --version`
    - Namestimo git v primeru, da ga nimamo nameščenega z ukazom: `sudo apt update -y` in `sudo apt install -y git`
- Zaženemo: `git clone https://github.com/icta-tecaji/raspberry-pi-icta.git`

## Nastavitev statičnega IP naslova
Če uporabljamo RaspberryPi prek oddaljenega dostopa (SSH), ali kot strežnik, ali pa ga le želimo imeti bolj pod kontrolo, moramo nastaviti statični IP naslov.

Z ukazom `ifconfig` preverimo trenutne omrežne nastavitve.

Statični IP nastavljamo s pomočjo orodja `nmcli`:
- Get connection name: `sudo nmcli c`
- Dodeljen vam bo IP iz 192.168.0.100/24 - 192.168.0.150/24 obsega (pazite da ne uporabite istega kot kdo drug v skupini).
- `sudo nmcli c mod preconfigured ipv4.addresses 192.168.0.X/24 ipv4.method manual`
- `sudo nmcli con mod preconfigured ipv4.gateway 192.168.0.1`
- `sudo nmcli con mod preconfigured ipv4.dns "192.168.0.1"`
- `sudo nmcli c down preconfigured && sudo nmcli c up preconfigured` (povezava se bo prekinila)
- V novem terminalu preverimo povezljivost z novim IP naslovom (`ssh pi@192.168.0.X`)
- Po ponovni prijavi z ukazom `ifconfig` preverimo, če je nastavljen pravilen IP.
- Povezljivost lahko preveri tudi sosed z ukazom ping: `ping <vaš IP naslov>`

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

Omogočimo dostop za SSH, HTTP in HTTPS za vse IPje:
- Pravila se izvajajo v vrstnem redu, kot so napisana.
- `sudo ufw allow 22`
- `sudo ufw allow 80`
- `sudo ufw allow 443`
- `sudo ufw allow 9443` (dostop do Portainer nadzorne plošče)

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
- `sudo ufw insert <RULE_NUMBER> deny from [ip-to-block] to any`

Brisanje pravil:
- `sudo ufw status numbered`
- `sudo ufw delete 2`

Z sosedom lahko preverite delovanje pravil.

## Varnost
- Sprememba privzetega gesla
    - Vsak RP, ki ima nameščen Raspbian ima default uporabniško ime (pi) in geslo (raspberry)
    - S tem imamo root dostop do RPja
    - Spremenimo geslo: `sudo passwd pi`
- Dodajanje novega uporabnika
- Zahtevamo geslo za sudo za vsako operacijo
- Preverimo posodobitve sistema
- Avtomatizacija opravil (Avtomatsko posodabljanje)
- Uporaba [Fail2ban](https://www.fail2ban.org/wiki/index.php/Main_Page)
    - Fail2ban je program, ki pregleduje log datoteke in na podlagi našega filtra blokira sumljive IP naslove.
