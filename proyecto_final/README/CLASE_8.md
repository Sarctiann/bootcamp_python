# Proyecto Final - API

![banner](bootcamp3.png)

> [Volver al README principal](../README.md)

## Modulo 4 - Clase 8: Introducción a FastApi

- [Librerías externas y el uso de pip](#librerías-externas-y-el-uso-de-pip)
- [Global vs Local (packages)](#global-vs-local-packages)
- [¿Que son los entornos virtuales?](#entornos-virtuales)
- [Algunas nociones sobre sistemas](#algunas-nociones-sobre-sistemas)
- [Comandos pip para el manejo de entornos virtuales](#manejo-de-entornos-virtuales)
- [Instalación de FastAPI](#instalación-de-fastapi)
- [Creación de una app básica](#creación-de-una-app-básica)
- [Creamos algunas rutas (endpoints) GET](#creamos-algunas-rutas)
- [aclaraciones sobre JSON (de ser necesario)](#aclaraciones-sobre-json)
- [FastApi "/docs" and "/redoc"](#fastapi-docs-and-redoc)

---

### [Librerías externas y el uso de pip](.)

Como ya podríamos haber notado, tenemos 4 maneras de agregar funcionalidad a nuestro
código.

1. útilizando las funcionalidades integradas (clases, funciones, decoradores) que
   podemos útilizar sin tener que importar nada.
1. importandolas desde nuestros paquetes y modulos definidos en el proyecto.
1. importandolas desde la librería standard de Python.
1. o lo que nos interesa en esta oportunidad. Instalando una librería externa. Una
   vez instalada, la importamos como si formara parte del sistema de Python.

---

### [Global vs Local (packages)](.)

A diferencia de JavaScript, Python funciona de manera global por defecto. Esto
significa que si instalamos una librería externa, la podemos importar en cualquier
proyecto. Esto podría parecer una ventaja, sin embargo es un problema, ya que cuando
trabajamos con varios proyectos, estos pueden tener diferentes requerimientos o
diferentes versiones de librerías.

Para solucionar esto en cada proyecto debemos aislar las dependencias y sus respectivas
versiones. Junto con la versión del interprete que vamos a utilizar.

---

### [Entornos Virtuales](.)

Entornos virtuales nos permiten realiar este "aislamiento" de las dependencias y
nuestro interprete especifico.
Un entorno virtual es un directorio que contiene una referencia a un interprete de
Python que tenemos instalado en nuestro sistema (podemos tener varios interpretes),
además en este directorio tenemos el arbol de archivos necesarios para gestionar
las dependencias externas de manera local (local al proyecto).

---

### [Algunas nociones sobre sistemas](.)

Finalmente para tener una comprensión de como funcionan estos entornos virtuales,
y para tener ciertas precauciones a tener en cuenta, vamos a ver algunas nociones
sobre sistemas:

- Rutas relaativas y rutas absolutas

Las Rutas (paths) son representaciones de ubicaciones de directorios y archivos
dentro de un sistema. Para sistemas de tipo Unix estas los nombres de carpetas y
archivos se separan por "/". Para sistemas de tipo Windows estas
los nombres de carpetas y archivos se separan por "\".

Pero en ambos casos si la ruta empieza con una "barra" ("/" o "\") es una ruta
absoluta, esto significa que es la "ruta completa" desde el directorio raiz hasta
el punto final (directorio o archivo).

En cambio, si la ruta empieza con un punto o directamente el nombre de un archivo
o directorio, se trata de una ruta relativa (es decir, una ruta desde nuestro
directorio actual). Para movernos un directorio padre usamos "\.\." y para mayor
consistencia, nos referimos al directorio actual con "."

- cwd

(current working directory) es el directorio actual. Este es un concepto muy
importante ya que es el punto de partida para las rutas relativas. Y es importante
para nosotros porque para ejecutar correctamente nuestros proyectos de python
necesitamos hacerlo desde el directorio correcto. de otra manera las referencias
a "paquetes" y "módulos" probablemente se rompan.

- variables de entorno (PATH)

Las variables de entorno son similares a las variables de Python, pero existen en
la "instancia de consola", es decir, cada vez que abrimos una terminal, esta contiene
variables de entorno como por ejemplo la ruta al interprete de Python.

- links

Finalmente un "link" (enlace) es una referencia a un directorio o archivo. Es decir,
es un archivo que apunta a otro archivo o directorio.

---

### [Manejo de Entornos virtuales](.)

Teniendo en cuenta lo anterior, tenemos que saber que cuando creamos un entorno
virtual, este creará un link a uno de los interpretes que tenemos instalados.
Por ejemplo si creamos el entorno virtual con Python3.12 el interprete de este
entorno virtual será Python3.12.

Otra cosa a tener en cuenta es que los archivos y variables de entorno del entorno
virtual contienen rutas relativas. Por lo que una vez creado, no lo podemos mover
a otro directorio. Porque dejaría de funcionar. En tal caso simplemente habria que
y crear uno nuevo en el directorio correcto. (Normalmente la raíz de nuestro proyecto).

Para trabajar con entornos virtuales necesitamos conocer algunos comandos:

- Para crear un entorno virtual, podemos usar el siguiente comando:

  - `python -m venv .nombre_del_virtual_env`
  - `python3 -m venv .nombre_del_virtual_env` (para sistemas Unix)

- Para activar un entorno virtual, podemos usar el siguiente comando:

  - `.nombre_del_virtual_env\Scripts\activate.bat` o `activate.ps1`
  - `source .nombre_del_virtual_env/bin/activate` (para sistemas Unix)

- Para instalar una librería en un entorno virtual, podemos usar el siguiente comando:

  - `python -m pip install nombre_de_la_libreria` (para ambos sistemas)

- Si nuestro proyecto contiene un archivo [**"requirements.txt"**](requirements.txt), podemos usar el
  siguiente comando para instalar todas las dependencias del proyecto:

  - `python -m pip install -r requirements.txt`

- Si necesitamos crear o actualizar el archivo "requirements.txt",
  podemos usar el siguiente comando:

  - `python -m pip freeze > requirements.txt`

---

### [Instalación de FastAPI](.)

Para instalar FastAPI, primero necesitamos crear y activar nuestro entorno virtual,
y luego instalar este paquete:

- `python -m pip install "fastapi[standard]"`

como hemos agregado una dependencia a nuestro proyecto debemos recordar correr
el comando `python -m pip freeze > requirements.txt`

---

### [Creación de una app básica](.)

Ahora solo nos queda crear nuestra primer app en FastAPI. Creemos un archivo
["main.py"](./main.py) y agreguemos el siguiente código:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello World"}
```

FastAPI nos provee los comandos `dev` y `run` para correr nuestra app.
Para correr nuestra app en modo de desarrollo debemos ejecutar el siguiente comando:

- `fastapi dev`

Esto va a "levantar" nuestra app en modo de desarrollo. Es decir que va a estar
atento a los cambios que realizamos en el código y se van a sincronizar sin necesidad
de reiniciar nuestro servidor.

Ahora podemos ir a la url `localhost:8000` y ver que nuestra app funciona.

---

### [Creamos algunas rutas](.)

- En algunas ocaciones necesitam∫os retornar una vista (HTML), modifiquemos la funcion
  `home` para que retorne una pagina HTML.
  [fuente](https://fastapi.tiangolo.com/advanced/templates/)
- Por otra parte nuestra API tiene que ser capas de enviar información al cliente
  para esto útilizamos el formato JSON. Creemos 2 endpoints que retornen las dos
  colecciones de Python que se pueden "serializar" en JSON válido.

---

### [aclaraciones sobre JSON)](.)

- El formato JSON (JavaScript Object Notation) es un formato de datos que nos permite
  enviar y recibir datos de forma eficiente entre sistemas. En si es un string de
  bytes. Y su estructura es analogica con la de las listas y diccionarios de Python.
  con la excepción de que las claves deben ser siempre strings.

- Con JSON nos sirve de lenguaje intermedio entre el cliente y el servidor.

---

### [FastApi docs and Redoc](.)

- Pro último, observemos que fastapi nos provee la documentación de la API.
  Sin necesidad de agregar ninguna configuración o dependencia.
  - [/DOCS (swagger)](http://localhost:8000/docs)
  - [/Redoc (ReDoc)](http://localhost:8000/redoc)

---

---
