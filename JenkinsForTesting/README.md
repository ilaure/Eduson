# Eduson
## Различные файлы для уроков в Eduson:
### JenkinsForTesting:
#### Проверьте, что docker доступен:
```
docker
```
Если Docker не установлен, нужно поставить [https://www.docker.com/](https://www.docker.com/)
#### Проверьте, какие образы сейчас есть:
```
docker images
```
#### Создаём сеть в докере которую будем использовать:
```
docker network create jenkins
```
#### Чтобы выполнять команды Docker внутри узлов Jenkins, потребуется ещё один образ docker:dind запустим сразу его:
```
docker run --name jenkins-docker --rm --detach ^
  --privileged --network jenkins --network-alias docker ^
  --env DOCKER_TLS_CERTDIR=/certs ^
  --volume jenkins-docker-certs:/certs/client ^
  --volume jenkins-data:/var/jenkins_home ^
  --publish 2376:2376 ^
  docker:dind
```
#### Чтобы запустить Jenkins агента внутри Docker, потребуется ещё один образ (https://hub.docker.com/r/alpine/socat/):
```
docker run --name jenkins-socat -d --restart=always -p 4444:2375 ^
  --network jenkins ^
  -v /var/run/docker.sock:/var/run/docker.sock ^
  alpine/socat ^
  tcp-listen:2375,fork,reuseaddr ^
  unix-connect:/var/run/docker.sock
```
#### Используя Dockerfile из репозитория запустить сборку:
```
docker build -t myjenkins-blueocean:2.389 .
```
#### Запустить контейнер:
```
docker run --name jenkins-blueocean --restart=on-failure --detach ^
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 ^
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 ^
  --volume jenkins-data:/var/jenkins_home ^
  --volume jenkins-docker-certs:/certs/client:ro ^
  --publish 8080:8080 --publish 50000:50000 myjenkins-blueocean:2.389
```
#### Переходим на http://localhost:8080/ и нам нужно предоставить пароль из /var/jenkins_home/secrets/initialAdminPassword, для этого:
```
docker exec jenkins-blueocean cat /var/jenkins_home/secrets/initialAdminPassword
```
