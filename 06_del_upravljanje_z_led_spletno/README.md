# Del 6: Upravljanje z LED preko spletnega vmesnika

GPIO pine lahko kontroliramo tudi čez spletni vmesnik.

## Namestitev knjižnic in predpriprava
- Posodobimmo Flask knjižnico: `python3 -m pip install flask --upgrade`
    - Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.
    - https://flask.palletsprojects.com/en/2.0.x/
- Odpremo port `8080` na požarnem zidu, da lahko dostopamo do Flask serverja.
    - Zaženemo: `sudo ufw allow 8080`

## Zagon programa
1. Program: `01_hello_world`:
    - V tem programu zaženemo Flask server, ki vrne "Hello World" ob obisku strani.
    - Zagon: `python3 hello_world.py`
    - Obisk strani: `<IP_NAPRAVE>:8080`

2. Program: `02_datetime_templates`:
    - V tem programu zaženemo Flask server, ki vrne trenuten datum in čas na serverju.
    - Zagon: `python3 main.py`
    - Obisk strani: `<IP_NAPRAVE>:8080`

3. Program: `03_GPIO_remote_control`:
    - Povežemo 2 LED na 11 in 13 pin. S pomočjo spletnega vmesnika lahko nadzorujemo pine.
    - Zagon: `python3 main.py`
    - Obisk strani: `<IP_NAPRAVE>:8080/interface`


