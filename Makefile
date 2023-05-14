
#[Change according to your project]

build:
	docker image build -t ms-example:v1.0 .

run:
	docker container run -d --name ms-example -p 6060:6060 ms-example:v1.0

build-dev:
	docker build -t ms-example:v1.0-dev -f Dockerfile.dev .

dev:
#Aquí, $(PWD) es una variable que representa el directorio de trabajo actual en tu máquina local y /code es el directorio de trabajo en el contenedor que estableces en tu Dockerfile con WORKDIR /code.
	docker container run -d --name ms-example-dev -p 6060:6060 -v $(PWD):/code ms-example:v1.0-dev

exec:
	docker container exec -it ms-example /bin/sh

logs:
	docker container logs ms-example

test:
	pytest --setup-show

all: test build run