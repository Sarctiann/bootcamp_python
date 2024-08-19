# Proyecto Final - API

![banner](bootcamp3.png)

> [Volver al README principal](../README.md)

## Modulo 5 - Simple Despliegue

- ### [Completamos las Entidades Básicas](#completamos-las-entidades-básicas)

- ### [Archivos de Configuración](#archivos-de-configuración)

- ### [Scripts de Inicialización](#scripts-de-inicialización)

- ### [Despliegue](#despliegue)

---

---

## [Completamos las Entidades Básicas](.)

Ya tenemos implementada la configuración de **CORS**, la conección a la
**Base de Datos** y la autenticación con **JWT**.

También tenemos definidas las entidades **Users** y **Products**.

### Separar Users de Auth

Lo primero que vamos a hacer es separar el servicio **auth** en
[auth](../api/services/auth.py) y [users](../api/services/users.py).

También vamos a crear las rutas para [users](../api/routes/users.py).

De esta forma vamos a tener la posibilidad de hacer operaciones CRUD con usuarios
que no sean nuestro propio "usuario".

Por otra parte, necesitamos separar la funcionalidad de [auth](../api/services/auth.py#L20)
y [security](../api/services/auth.py#L50) un poco, ya que todo endpoint con
nuestra AuthServiceDependency sería protegido. Y eso no nos permitiria registrarnos
o logearnos.

### Completamos nuestras operaciones CRUD

Ahora completamos nuestras rutas de [productos](../api/routes/products.py) y
[usuarios](../api/routes/users.py)

---

## [Archivos de Configuración](.)

---

## [Scripts de Inicialización](.)

Como habiamos visto antes, en nuestro archivo de configuración de base de datos
teniamos definida una función que se ejecutaba siempre que nuestro servidor se
inicializaba. El problema con esto es que deberíamos modificar el archivo si quisieramos
que esta función se ejecute o se deje de ejecutar.

La solución a este problema es definir un [script](../scripts/init_db_collections.py)
de inicialización que vamos a ejecutar nosotros una única vez, o las veces que lo
queramos hacer, independientemente de la inicialización de nuestro servidor.

Ahora bien, este script se encuenta en un directorio de scripts. Por lo que para
importar módulos de nuestra app. tendríamos problemas ya que necesitamos referirnos
a paquetes que están fuera del paquete scripts. Por lo que lo vamos a ejecutar con

```shell
python -m scripts.init_db_collections
```

de esta forma nuestro script se ejecutará como un módulo y podrá realizar importaciones
relativas.

---

## [Despliegue](.)

---

---

# TODO:

- queryParams (para paginado y filtro)
- compras (models, services, routes)
- koyeb
