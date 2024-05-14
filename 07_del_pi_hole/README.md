# Del 7: Pi-hole

Pi-hole je DNS *sinkhole* (črna luknja), ki varuje naprave pred nezaželeno vsebino, brez namestive dodatne programske opreme na odjemalce v lokalnem omrežju. Še nekaj glavnih značilnosti:
- **Easy-to-install**: our versatile installer walks you through the process and takes less than ten minutes
- **Resolute**: content is blocked in non-browser locations, such as ad-laden mobile apps and smart TVs
- **Responsive**: seamlessly speeds up the feel of everyday browsing by caching DNS queries
- **Lightweight**: runs smoothly with minimal hardware and software requirements
- **Robust**: a command-line interface that is quality assured for interoperability
- **Insightful**: a beautiful responsive Web Interface dashboard to view and control your Pi-hole
- **Versatile**: can optionally function as a DHCP server, ensuring all your devices are protected automatically
- **Scalable**: capable of handling hundreds of millions of queries when installed on server-grade hardware
- **Modern**: blocks ads over both IPv4 and IPv6
- **Free**: open-source software which helps ensure you are the sole person in control of your privacy

Gradiva:
- [Uradna spletna stran](https://pi-hole.net/)
- [Navodila za Docker namestitev](https://github.com/pi-hole/docker-pi-hole/#running-pi-hole-docker)
- [Dokumentacija](https://docs.pi-hole.net/)

## Namestitev

Pred namestitvijo moramo pripraviti sledeče zadeve katere lahko najdete [tukaj](https://docs.pi-hole.net/main/prerequisites/):
- Določiti RPi statičen IP naslov (to smo storili že v delu 4)
- Na požarnem zidu odpremo naslednja vrata (pazimo, da je RPi v lokalnem omrežju!):
    - `sudo ufw allow 80/tcp`
    - `sudo ufw allow 53/tcp`
    - `sudo ufw allow 53/udp`

Pi-hole lahko [namestimo na več različnih načinov](https://docs.pi-hole.net/main/basic-install/). V našem primeru bomo uporabili Docker saj omogoča najenostavnejšo namestitev:
- Premaknemo se v mapo: `cd ~/raspberry-pi-icta/07_del_pi_hole`
- Zaženemo Pi-hole: `sudo docker compose up -d`
- Preverimo ali je Pi-hole zagnan: `sudo docker compose ps`
- Preverimo loge: `sudo docker compose logs`

Če je Pi-hole uspešno zagnan lahko na naslovu `http://<RP_IP>/admin/index.php` vidimo Pi-hole nadzorno ploščo (geslo za dostop je *delavnica*).

Ker Pi-hole zaganjamo v Dockerju moramo v nastavitvah spremeniti naslednje: `Settings -> DNS -> Interface settings -> Potentially dangerous options -> Permit all origins`.

Naslednji korak je da napravam na lokalnem omrežju omogočimo uporabo Pi-Hole. To lahko naredimo na [več načinov](https://docs.pi-hole.net/main/post-install/). 

> [Podrobnejši opis nastavitev naprav](https://discourse.pi-hole.net/t/how-do-i-configure-my-devices-to-use-pi-hole-as-their-dns-server/245)

Ponavadi najpogosteje nastavimo IP naslov Pi-hole kot edini DNS vnos na ruterju, kar omogoča da nam ni potrebno nastavljati posameznih naprav. V našem primeru pa bomo ročno nastavili vsako izmed naprav. Dodali bomo IP RPi-ja kot [statični DNS vnos na naši napravi](https://discourse.pi-hole.net/t/how-do-i-configure-my-devices-to-use-pi-hole-as-their-dns-server/245#setup-11).

## Uporaba

Na prvi strani nadzorne plošče lahko spremljamo statistiko.

Lahko dodamo tudi lastne sezname domen, ki jih želimo blokirati. Na internetu najdemo veliko [primerov](https://github.com/blocklistproject/Lists). 

Postopek:
1. Dodamo URL v blocklisto (Login > Adlists > Paste list URL in "Address" field, add comment > Click "Add")
2. Posodobimo Gravity (Tools > Update Gravity > Click "Update")

Po končani uporabi Pi-hole ustavimo z ukazom: `sudo docker compose down -v`

