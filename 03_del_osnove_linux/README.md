# Del 3: Osnove uporabe Linux terminala

## Pregled ukazov
- `ls`
- `pwd`
- `cd`
- `exit`
- `mv`
- `cp`
- `rm`
- `mkdir`
- `man`
- `touch`
- `nano`
- `chmod`
- `htop`
- `apt`
- `cat`
- `grep`
- [`shutdown`](https://www.computerhope.com/unix/ushutdow.htm): command shuts down or reboots the system
- `ifconfig`: used to configure, or view the configuration of, a network interface
- `iwconfig`: configures a wireless network interface

## Namestitev Docker

Docker nam bo olajšal namestitev programske opreme, ki jo bomo potrebovali skozi tečaj.

[Install Docker Engine on Debian](https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script):
- `DRY_RUN=1`
- `curl -fsSL https://get.docker.com -o get-docker.sh`
- `sudo sh get-docker.sh`
- `sudo systemctl enable docker.service`
- `sudo systemctl enable containerd.service`
- `sudo docker run hello-world`


## Namestitev Portainer

[Portainer](https://www.portainer.io/) nam omogoča enostaven pregled in upravljanje z Docker kontejnerji.

[Namestitev](https://docs.portainer.io/start/install/server/docker/linux) je zelo enostavna. Vse kar potrebujemo so naslednji ukazi:
- `sudo docker volume create portainer_data`
- `sudo docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest`
- `sudo docker ps`

Odpremo povezavo URL: `https://<RPI_IP>:9443/` in ustvarimo nov uporabniški račun.
