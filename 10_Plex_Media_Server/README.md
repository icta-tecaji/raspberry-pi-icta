# Del 10: Plex Media Server

Plex organizes video, music and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone Plex Media Server. Straightforward design and bulk actions mean getting things done faster.

- Docker image source: https://hub.docker.com/r/linuxserver/plex
- Official documentation: https://support.plex.tv/

## Run
- Move to folder: `cd ~/raspberry-pi-icta/10_Plex_Media_Server`
- Allow ports on firewall: `sudo ufw allow 32400/tcp`
- Run Docker Compose File: `sudo docker compose up -d`
- Check if Plex is running: `sudo docker compose ps`
- Check logs: `sudo docker compose logs`
- Connect to `http://<RP_IP>:32400/` with your [client](https://www.plex.tv/apps-devices/#players).

## Remove
- Stop Plex: `sudo docker compose down -v`