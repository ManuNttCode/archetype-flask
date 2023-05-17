# ms-template-flask

## Introducción

Ejemplo de creación de una plantilla para un microservicio desarrollado en Python con la librería Flask.

Todo el código definido en el proyecto tiene como objetivo describir elementos básicos necesarios
con una finalidad didáctica.

```

## Docker 

Existen dos ambientes producción y desarrollo para ejecutar en local

0.- Antes de correr cualquier ambiente, ve al archivo Makefile y cambia los valores que estan entre [ms-example] con el nombre de microservicio y eliminando los []

1.- Creación de la imagen. Operación **build** del fichero Makefile.
``` 
docker image build -t alvaroms/[ms-example]:v1.0 .

>make build
```

2.- Arrancar el contenedor. Operación **run** del fichero Makefile.
``` 
docker container run -d --name [ms-example] -p 6060:80 alvaroms/[ms-example]:v1.0

>make run
```

3.- Creación de la imagen para desarrollo. Operación **build-dev** del fichero Makefile.
``` 
docker build --no-cache -t [ms-example]:v1.0-dev -f Dockerfile.dev .

>make build-dev
```

4.- Arrancar el contenedor. Operación **dev** del fichero Makefile.
``` 
docker container run -d --name [ms-example]-dev -p 6060:6060 -v $(PWD):/code [ms-example]:v1.0-dev

>make dev
```

5.- Entrar en la consola del contenedor. Operación **exec** del fichero Makefile.
``` 
docker container exec -it [ms-example] /bin/sh

>make exec
```

6.- Visualizar los logs del contenedor. Operación **logs** del fichero Makefile.
``` 
docker container logs [ms-example]

> make logs
```

7.- Ejecuta los test. Operación **test** del fichero Makefile.
``` 
pytest --setup-show

> make test
```

8.- Ejecuta el reporte de coverage de los test. Operación **test-cov** del fichero Makefile.
``` 
pytest --cov=src

> make test-cov
```

9.- Para la ejecución conjunto de las operaciones básicas: test, creación de la imagen y arranque
se emplea el comando **all** del fichero Makefile.

```

