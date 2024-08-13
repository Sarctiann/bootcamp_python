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
- [Crear nuestra dependencia de base de datos](#creación-de-DB-dependency)

### Continuamos con la arquitectura de nuestro proyecto

- [Reubicamos nuestros endpoints](#reubicamos-nuestros-endpoints)

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

1. `poetry init` para iniciar un nuevo proyecto (creará el entorno virtual y los
   archivos de configuración de dependencias)
1. `poetry add fastapi[standard]` para instalar fastapi.
1. `poetry add pymongo` para instalar pymongo.
