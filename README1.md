Docker Commands
## Install Docker-Compose
```
curl -L "https://github.com/docker/compose/releases/download/1.28.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
which docker-compose
docker-compose --version
```
## Attache a Volume
```
docker container run -d --name testapp -p 8080:5000 -v  /root/docker_app/app/src:/code testapp:v1
```

```
docker-compose images
```
```
docker-compose push
```
###Docker compose conatiner logs (live)
```
docker-compose up
docker-compose down
```
```
docker-compose up -d --build
```
```
docker image build -t devapp:v1  . -f dockerfile-dev
docker-compose -f docker-compose-dev.yaml build
docker-compose -f docker-compose/docker-compose-dev.yaml build
```
```
docker-compose up -d
```
```
docker-compose  -f docker-compose-dev.yaml up -d
docker-compose  -f docker-compose-dev.yaml down
```
```
docker container inspect myapp
```
```
docker network inspect docker-compose_myapp_network
```
```
docker volume inspect docker-compose_myapp_volume
```
```
docker ps -a --filter volume=docker-compose_myapp_volume
```
```
docker ps -a --filter network=docker-compose_myapp_network
```
```
docker ps -a --filter network=bridge
```
```
cd /var/lib/docker/volumes/
cd docker-compose_myapp_volume/
cd _data/
```
### Network
```
docker network ls
docker network create mynetwork

```

```
docker container run -d --name apache --network mynetwork  -p 8081:80 httpd:latest
```
```
docker container run -ti  --name centos --network mynetwork centos:latest
```
```
docker network inspect bridge
```
```
docker container run -i -t -- name centos centos:latest
docker container exec -ti apache bash
```