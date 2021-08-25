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

Sejo prekinemo z ukazom exit. Protokol SSH uporablja TCP port 22


## Požarni zid


- namestimo git
- poberemo iz gita vso kodo





## Konfugracija SSH brez dodatnega ekrana
- @Balki TODO
- Na hitr midva pokaževa kako se usposobi RP, če nimaš ekrana (.ssh datoteko nrdiš in pol sshajat gor itd..)..
- Ampak ne rabjo vsi takrt z nama sledit temu..
- Kle bi rabl dodatno SD kartico da jo lahko tm takoj formatiramo in na sveže naložimo sistem

