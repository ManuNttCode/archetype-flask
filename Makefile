
#[Change according to your project]

build:
	docker image build -t [ms-example]:v1.0 .

run:
	docker container run -d --name [ms-example] -p 6060:80 [ms-example]:v1.0

exec:
	docker container exec -it [ms-example] /bin/sh

logs:
	docker container logs [ms-example]

test:
	pytest --setup-show

all: test build run