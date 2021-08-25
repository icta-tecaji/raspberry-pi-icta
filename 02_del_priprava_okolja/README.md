# Del 2: Priprava okolja in prva uporaba

## Namestitev Raspbian Linux

Namestitev Raspbian ni podobna namestitvi klasičnega operacijskega sistema (vstavitev instalacijskega medija, grafično instalacijsko okolje, nastavitve, ter ponovni zagon v novi sistem) - namestitev opravimo z prenosom pripravljene slike na SD kartico. Pripravljena slika vsebuje celotno kopijo “izvorne” sd kartice (vsebuje tudi podatke o morebitnih particijah, MBR, ter vso vsebino datotečnega sistema). Za kopiranje slike na kartico moramo prepisati celotno kartico (tudi datotečni sistem), zato potrebujemo poseben program, ki direktno prepisuje kartico.

1. Prenesemo sliko z operacijskim sistemom iz strani: https://www.raspberrypi.org/software/operating-systems/
    - Na spletni strani obstajata dve verziji - celotna in minimalna. Celotna vsebuje več programske opreme in celoten grafični vmesnik - taka je primerna za direktno uporabo. Minimalna vsebuje samo minimalni nabor programske opreme, in je namenjena za strežnike in/ali zahtevnejše uporabnike, ki želijo sami izbirati dodatno programsko opremo.
    - Izberemo `Raspberry Pi OS with desktop and recommended software`.
    - Datoteko shranimo na računalnik.
2. Namestimo orodje **Raspberry Pi Imager** iz strani https://www.raspberrypi.org/software/, ki nam omogoča pisanje slike na SD kartico.
3. Vstavimo SD kartico v računalnik.
4. Zaženemo Raspberry Pi Imager in namestimo OS.
    - Izberemo možnost, da počistimo vsebino celotne kartice pred pisanjem.

## Zagon
1. Po končanem kopiranju nadaljujemo z zagonom RP.
2. SD kartico vstavite v RaspberryPi.
3. Priklopite HDMI kabel (adapter in kabel do monitorja), tipkovnico, miško (2x USB) in še napajanje (Micro USB kabel).
4. Če je vse potekalo pravilno, bi se moral na monitorju pojaviti najprej potek zagona (tekstovni način + ikone v izgledu malin), ter čez nekaj časa še grafični vmesnik.
5. Sprehodimo se čez osnovne nastavitve:
    - Nastavitve države in tipkovnice
    - Geslo
    - Izberemo WiFi
    - Namestimo posodobitve
    - Reboot
6. Namestitev tipkovnice
    - Privzet razpored tipkovnice je angleški. Če želite, ga nastavite na Slovenskega, tako da v Menu-ju izberete `Mouse and keyboard settings`, v jezičku `Keyboard` izberete `Keyboard layout`, in znotraj tega izberete `Slovenian - Slovenian`.


