# Proyecto Final - API

![banner](bootcamp3.png)

> [Volver al README principal](../README.md)

## Modulo 5 - Clase 10: Poetry y creación de base de datos

### Poetry

- [Instalación de Poetry](#instalación-de-poetry)
- [Configuración de Poetry](#configuración-de-poetry)
- [Usando Poetry](#usando-poetry)

### Base de datos (mongodb)

- [Creación de la base de datos](#creación-de-la-base-de-datos)
- [Configuración de la base de datos](#configuración-de-la-base-de-datos)

### Continuamos con la arquitectura de nuestro proyecto

- [Creamos el paquete api](#creamos-el-paquete-api)
- [Creamos el paquete config](#creamos-el-paquete-config)
- [Creamos el paquete routes](#creamos-el-paquete-routes)

---

---

### [Instalación de Poetry](.)

([fuente](https://python-poetry.org/docs/#installation))

Poetry es una herramienta que nos permite manejar las dependencias de nuestros
proyectos. A su vez se encarga de generar el entorno virtual y respeta la versión
de python que nuestro proyecto requiera.

Primero eliminemos nuestro entorno virtual y nuestro archivo
[`requirements.txt`](../requirements.txt):

Luego para instalar Poetry, debemos hacerlo de manera global, ya que Poetry va
administrar las dependencias de nuestro proyecto el no puede ser una de ellas.

- En Windows podrian instalarlo directamente con: `py -m pip install --user poetry`
- O podrian instalar `pipx` como es el caso de Linux o Mac:

  - Segundo debemos instalar `pipx`
    ([fuente](https://github.com/pypa/pipx?tab=readme-ov-file#install-pipx))
  - Finalmente podemos instalar Poetry con: `pipx install poetry`

### [Configuración de Poetry](.)

Por defecto Poetry va a crear un entorno virtual en una ruta del sistema. Nosotros
queremos que el entorno virtual siempre esté en nuestro proyecto, para que nuestras
herramientas de desarrollo lo puedan inferir. Para eso podemos configurar este
comportamiento con el siguiente comando:

- `poetry config virtualenvs.in-project true`

### [Usando Poetry](.)

Listo! ahora podemos utilizar poetry para administrar nuestro proyecto:

1. `poetry init` para iniciar un nuevo proyecto (creará el archivo de configuración)
1. `poetry install` para crear el entorno virtual e instalar las dependencias.
1. `poetry add "fastapi[standard]"` para agregar (e instalar) fastapi.

---

### [Creación de la base de datos](.)

Para nuestro proyecto vamos a utilizar mongodb, por lo que en esta oportunidad vamos
ver como crear una base de datos en [MongoDB Atlas](https://www.mongodb.com/atlas).

No nos vamos detener en el paso a paso, porque hay mucho material que pueden seguir
para hacerlo. Sin embargo esimportante tener en cuenta algunas cosas:

1. Iniciar sesión en MongoDB Atlas.
1. Crear "un Proyecto"
1. Crear "un Cluster"

IMPORTANTE: En algún punto van a tener que configurar un usuario y contraseña
(GUARDAR MUY BIEN EL PASSWORD QUE CONFIGURAMOS).

La creación del cluster puede tomar unos minutos, pero luego de eso podremos
verlo en el tablero de MongoDB Atlas. y tenemos que presionar en el botón

#### "Connect"

y se nos va a abrir un modal en el que vamos a presionar en la opción

#### "Drivers"

1. Seleccionemos "Python" y la versión que estemos utilizando (Notaran que en nuestro
   proyecto, el archivo pyproject.toml tiene esta version).
1. Se nos informa quenecesitamos instalar el driver "pymongo". Pero vamos a reemplazar
   la primer parte `python -m pip install` por `poetry add`.
1. Por último se nos brinda un "connectionString" lo vamos a copiar.

### [Configuración de la base de datos](.)

En nuestro proyecto vamos a crear uns archivo: [`.env`](../.env)
y vamos a crear esta variable de entorno:

```shell
MONGODB_CONNECTION_STRING=el_connection_string_que_copiamos
```

Este archivo lo tenemos que agregar a nuestro [`.gitignore`](../../.gitignore) ya
que no queremos que seguarde en nuestro repositorio (porque contiene secretos).

Luego tenemos que asegurarnos de reemplazar `<password>` por el password que
tenemos configurado en MongoDB Atlas.

---

### [Creamos el paquete api](.)

A medida que nuestro proyecto va creciendo nuestros paquetes y módulos comienzan
a mezclarse, por lo que finalmente vamos a reestructurar nuestro proyecto. Lo que
también implica que tengamos que modificar nuestras rutas de importación.
