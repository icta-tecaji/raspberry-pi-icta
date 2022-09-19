# Del 8: Pi-hole

- [Uradna spletna stran](https://pi-hole.net/)
- [Navodila za Docker namestitev](https://github.com/pi-hole/docker-pi-hole/#running-pi-hole-docker)
- [Dokumentacija](https://docs.pi-hole.net/)

## Namestitev
sudo ufw allow 80/tcp
sudo ufw allow 53/tcp
sudo ufw allow 53/udp
sudo ufw allow 67/tcp
sudo ufw allow 67/udp
sudo ufw allow 546:547/udp


sudo docker compose up -d
sudo docker ps

https://docs.pi-hole.net/main/post-install/

nastavitev naprav https://discourse.pi-hole.net/t/how-do-i-configure-my-devices-to-use-pi-hole-as-their-dns-server/245

## 