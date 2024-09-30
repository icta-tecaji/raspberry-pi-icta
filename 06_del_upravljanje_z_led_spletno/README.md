# Del 6: Upravljanje z LED preko spletnega vmesnika

GPIO pine lahko kontroliramo tudi čez spletni vmesnik.

<!-- ## WebIOPi spletni vmesnik (not supported on Raspberry Pi 5)
[WebIOPi](http://webiopi.trouch.com/) is a web application which allows you to control your Raspberry Pi’s GPIO. Just install it on your Pi, and use any browser from your network.
It’s useful to start enjoying GPIOs and also to debug some circuits without writing any line of code. It also allows to control your Pi’s GPIOs over Internet, so it’s a good starting point for home remote control.

**[Namestitev](https://thepiguy.altervista.org/webiopi-rp3/)**:
- `cd ~/raspberry-pi-icta/06_del_upravljanje_z_led_spletno/`
- `tar xvzf WebIOPi-0.7.1.tar.gz`
- `cd WebIOPi-0.7.1/`
- Verzija na uradni strani ima težave z delovanjem na Raspberry Pi 3B+. Zato uporabimo spodnji popravek.
    - `sudo wget https://raw.githubusercontent.com/doublebind/raspi/master/webiopi-pi2bplus.patch`
    - `sudo patch -p1 -i webiopi-pi2bplus.patch`
- `sudo ./setup.sh`
- Do you want to access WebIOPi over Internet ? Select `Yes`.
- Now reboot the Pi.
- Start WebIOPi by running the command: `sudo /etc/init.d/webiopi start`
- If you want WebIOPi to start automatically on boot, run: `sudo update-rc.d webiopi defaults`
- Once WebIOPi is up and running, you can point your browser to `http://<yourraspberryIP>:8000` (replace yourraspberryIP with the actual IP address or domain name of your Raspberry Pi) and log in using the `webiopi` username and the `raspberry` password. -->


## Flask spletni vmesnik

### Namestitev knjižnic in predpriprava
- Namestimo virtualno okolje in Flask knjižnico.: 
    - `cd ~/raspberry-pi-icta/06_del_upravljanje_z_led_spletno`
    - Posodobimo seznam paketov: `sudo apt update`
    - Namestimo Python venv:
        - `sudo apt-get update`
        - `sudo apt-get -y upgrade`
        - `sudo apt-get install python3-pip`
        - `sudo apt install --upgrade python3-setuptools`
        - If you are installing on the Bookworm version of Raspberry Pi OS, you will need to install your python modules in a virtual environment:
        - `sudo apt install python3-venv`
        - `python3 -m venv .venv --system-site-packages`
        - `source .venv/bin/activate`
        - Namestimo Flask: `pip install Flask`
            - Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.
            - https://flask.palletsprojects.com/en/3.0.x/
- Odpremo port `8080` na požarnem zidu, da lahko dostopamo do Flask serverja.
    - Zaženemo: `sudo ufw allow 8080`

### Zagon programa
1. Program: `01_hello_world`:
    - V tem programu zaženemo Flask server, ki vrne "Hello World" ob obisku strani.
    - Premik v mapo: `cd 01_hello_world`
    - Zagon: `python3 hello_world.py`
    - Obisk strani: `<IP_NAPRAVE>:8080`
    - Ugasnite Flask server: `Ctrl+C` in se premaknimo mapo višje: `cd ..`

2. Program: `02_datetime_templates`:
    - V tem programu zaženemo Flask server, ki vrne trenuten datum in čas na serverju.
    - Premik v mapo: `cd 02_datetime_templates`
    - Zagon: `python3 main.py`
    - Obisk strani: `<IP_NAPRAVE>:8080`
    - Ugasnite Flask server: `Ctrl+C` in se premaknimo mapo višje: `cd ..`

3. Program: `03_GPIO_remote_control`:
    - Povežemo 2 LEDici na 17 in 27 pin. S pomočjo spletnega vmesnika lahko nadzorujemo pine.
    - Premik v mapo: `cd 03_GPIO_remote_control`
    - Zagon: `flask --app main run --host=0.0.0.0 --port=8080`
    - Obisk strani: `<IP_NAPRAVE>:8080/interface`
    - Ugasnite Flask server: `Ctrl+C`
    - Gremo iz sudo na običajnega uporabnika: `exit`

Po končanih vajah deaktiviramo virtualno okolje: `deactivate`
