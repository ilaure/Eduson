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
