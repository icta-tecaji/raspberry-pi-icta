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

Docker nam bo olajšal

[Install Docker Engine on Debian](https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script):
- `DRY_RUN=1`
- `curl -fsSL https://get.docker.com -o get-docker.sh`
- `sudo sh get-docker.sh`
- `sudo systemctl enable docker.service`
- `sudo systemctl enable containerd.service`
- `sudo docker run hello-world`
