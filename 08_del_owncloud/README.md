# Del 8: Owncloud

[ownCloud](https://owncloud.com/) je odprtokodna storitev, ki omogoča, da naša naprava postane strežnik za deljenje in shranjevanje datotek, podobno kot Google Drive ali Dropbox.

## Namestitev in uporaba

Na naslednji [povezavi](https://doc.owncloud.com/server/10.14/) lahko najdemo vse informacije o ownCloud Classic Server.

V našem primeru bomo ownCloud namestili s pomočjo Docker-ja. 

> Natančna navodila za Docker namestitev lahko najdete [tukaj](https://doc.owncloud.com/server/10.14/admin_manual/installation/docker/).

Namestitev poteka na sledeči način:
1. Premaknemo se v mapo: `cd ~/raspberry-pi-icta/08_del_owncloud`
2. Odpremo datoteko: `nano .env` in spremenimo `OWNCLOUD_DOMAIN` in `OWNCLOUD_TRUSTED_DOMAINS` glede na IP, ki ga ima RPi.
3. Zaženemo ukaz: `sudo docker compose up -d`

Po uspešni namestitvi preverimo ali so vsi kontejnerji zagnani z ukazom: `sudo docker compose ps`. V primeru, da ima še kakšen kontejner status `running (starting)` lahko preverimo podrobnejše loge s ukazom `sudo docker compose logs --follow owncloud`.

Gremo na naslov `http://<RPI_IP>:8080` v brskalniku in se prijavimo v ownCloud (usr: admin, pass: admin).

> V realnih primerih moramo uporabiti varnejše geslo!

Se spregodimo po spletni strani in preizkusimo različne funkcionalnosti (nalaganje dokumentov, deljenje dokumentov, dodajanje uporabnikov...).

Po končanem delu lahko zadeve odstranimo z ukazom `sudo docker compose down -v`
