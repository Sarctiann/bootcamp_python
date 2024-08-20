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
[usuarios](../api/routes/users.py).

Esto también requiere que mejoremos nuestra capa de servicio, ya que teníamos
servicios que no estaban retornando, data serializable.
([products.update_one](../api/services/products.py#L38), o
[products.delete_one](../api/services/products.py#L53))

### Agregamos parametros de consulta

Cualquier endpoint puede tomar query-params, pero es prácticamente oblicatorio
proveer básicamente los parametros de paginado (limit y offset), otros parámetros
muy comunes (y dependiendo del caso, igualmente importantes) son filter y sort.

| Query-Param        | Description                                             |
| ------------------ | ------------------------------------------------------- |
| limit              | Cantidad de elementos a retornar.                       |
| offset             | Cantidad de elementos a saltar. `(limit * page_number)` |
| sort (`sort_by`)   | Criterio de ordenamiento. (ordenar por un campo)        |
| order (`sort_dir`) | Ordenamiento. (ascendente o descendente)                |
| filter (`q`)       | Criterio de filtrado. (coincidencia de algún tipo)      |

Para esto creemos una nueva dependencia [QueryParamsDependency](../api/__common_deps.py#L11)
que vamos a usar en nuestros endpoints que retornen "una lista" de elementos.

### Creamos la Entidad "Orders"

- [model](../api/models/orders.py)
- [service](../api/services/orders.py)
- [route](../api/routes/orders.py)

## [Archivos de Configuración](.)

Ahora que tenemos todas las funcionalidades básicas de nuestra app implementadas,
es momento de moverla a su propio repositorio. (Ustedes probablemente ya tengan sus
applicaciones en otro repositorio).

Tenemos muchisimas formas diferentes de desplegar nuestra aplicación. Pero para
propósitos demostrativos esta vez lo vamos a hacer en un servicio que nos ofrece
una capa gratuita

### [Koyeb](https://koyeb.com)

Koyeb es una plataforma que como muchas otras, están preparados para desplegar
aplicaciones en varios lenguajes con una configuración mínima. Para desplegar
nuestra app necesitamos tener dos archivos:

- [`Procfile`](../Procfile) el Procfile (archivo de proceso) es un archivo donde
  definimos una lista de procesos que la plataforma necesita ejecutar para levantar
  nuestra app. (Koyeb parece ejecutar únicamente el proceso `web`, por lo que tendremos
  que correr nuestras configuraciones por nuestra cuenta).

- [`requirements.txt`](../requirements.txt) nuestro viejo amigo... para generar
  este archivo solo tendremos que correr:

```shell
poetry export --without-hashes -o requirements.txt
```

Además vamos a necesitar configurar algunas variables de entorno más en
[.env](../.env.example). Para luego poder extender nuestros
["origenes admitidos"](../api/config/security.py#L9)

---

## [Scripts de Inicialización](.)

Como habiamos visto antes, en nuestro archivo de configuración de base de datos
teniamos definida una función que se ejecutaba siempre que nuestro servidor se
inicializaba. El problema con esto es que deberíamos modificar el archivo si quisieramos
que esta función se ejecute o se deje de ejecutar.

La solución a este problema es definir scripts como
[create_super_user](../scripts/create_super_user.py) o
[seed_database](../scripts/seed_database.py) de inicialización que vamos a ejecutar
nosotros una única vez, o las veces que lo queramos hacer, independientemente de
la inicialización de nuestro servidor.

Ahora bien, este script se encuenta en un directorio de scripts. Por lo que para
importar módulos de nuestra app. tendríamos problemas ya que necesitamos referirnos
a paquetes que están fuera del paquete scripts. Por lo que lo vamos a ejecutar con

```shell
python -m scripts.create_super_user
# y
python -m scripts.seed_database
```

de esta forma nuestro script se ejecutará como un módulo y podrá realizar importaciones
relativas.

---

## [Despliegue](.)

Para desplegar nuestra app en Coyeb:

1. Nos registramos en [Koyeb](https://koyeb.com) con nuestra cuenta de GitHub
1. Para crear un nuevo servicio, vinculamos nuestro Github
1. Elegimos el repositorio de nuestra app.
1. Luego de elegir la "región". vamos a ver un Menu con varias opciones desplegables.
1. Buscamos "Environment variables" y seteamos las variables como las tenemos en
   nuestro `.env`
1. Le damos al botón "Deploy" y debería ocurrir la magia.
1. Ahora Koyeb nos va a dar un dominio para nuestra app. Hay que copiarlo y pegarlo
   actualizar la variable de entorno `HOST_URL` (en la configuración de nuestra app).

---

---
