# Eduson
## Различные файлы для уроков в Eduson:
### DockerForTesting:
#### [Для локального запуска Unit-теста (main.py) и сборки образа из dockerfile](DockerForTesting/unitTest/):
Основные команды для локального запуска:  
Проверьте, что docker доступен:  
```
docker
```
Проверьте, какие образы сейчас есть:  
```
docker images
```
Находясь в той же директории где dockerfile, чтобы собрать образ (например, с именем "autotestlocal") достаточно выполнить:  
```
docker build -t autotestlocal .
```
Для запуска контейнера (например, с именем "autotestlocal_container") с использованием созданного образа достаточно выполнить:  
```
docker run --name autotestlocal_container -it autotestlocal
```
#### [Для локального запуска OWASP Juice Shop и примера одного теста (test.py) из dockerfile](DockerForTesting/juiceShopTest/):
Скачайте образ сайта OWASP Juice Shop:  
```
docker pull bkimminich/juice-shop
```
Создайте сеть testnet:  
```
docker network create testnet
```
Запустите контейнер (например, с именем "testweb") с сайтом juice-shop:  
```
docker run --net testnet --rm -p 3000:3000 --name testweb bkimminich/juice-shop
```
Находясь в той же директории где dockerfile, собрать образ (например, с именем "autotest_web_container"):  
```
docker build -t autotest_web_container .
```
Находясь в той же директории где test.py, запустим контейнер (для Windows ${PWD}, для Mac или Linux $(pwd)):  
```
docker run -it -v ${PWD}:/user/test/ -w /user/test/ autotest_web_container python test.py
```
