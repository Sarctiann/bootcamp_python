# Proyecto Final - API

![banner](bootcamp3.png)

> [Volver al README principal](../README.md)

## Modulo 5 - Clase 11: Autenticación, Autorización y CORS

- ### [Capa de Servicios](#capa-de-servicios)

- ### ["Modelos-Multiples"](#modelos-multiples)

- ### [Autenticación y Autorización](#autenticación-y-autorización)

- ### [Middlewares](#middlewares)

- ### [CORS](#cors)

---

---

## [Capa de Servicios](.)

La capa de servicios nos sirve de interfaz entre las operaciones de base de datos
u otras dependencias de nuestra applicación con la funcionalidad de nuestra applicación.

De esta forma todo el código necesario para inicializar o comunicarnos con estos
servicios, queda encapsulado en la capa de servicios. la cual luego podemos consumir
en nuestra capa de rutas.

La logica que antes teniamos implementada en nuestras rutas ahora está en
[api/services/products.py](../api/services/products.py)
y nuestro archivo [api/routes/products.py](../api/routes/products.py) ahora está
mas legible, por lo que su responsabilidad va a estar limitada a la comunicación
con el cliente.

---

## [Modelos-Multiples](.)

> [fuente](https://fastapi.tiangolo.com/tutorial/extra-models/)

"Multiple Models" es una tecnica que consiste en definir diferentes versiones de
una misma entidad, y sirve para tener un mejor control sobre nuestros datos, en
fastapi, esto tiene mucho sentido ya que nos provee esta validación de forma
automática. Un ejemplo sencillo sería el de [api/models/products.py](../api/models/products.py)

Ahora tenemos dos versiones, una para insertar un nuevo producto, y otra para
representar un producto existente en la base de datos.

Como resultado el campo `id` ya no es opcional. Y esto representa mejor nuestro
modelo ya que en nuestra base de datos de seguro va a tener este campo.

---

## [Autenticación y Autorización](.)

> [manual implementation](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#hash-and-verify-the-passwords)

De la misma forma que evitamos mantener manualmente la serialización y deserialización
de los `ObjectId`s. Para implementar la autenticación y autorización en nuestra app
vamos a recurrir a la librería [`fastapi-jwt`](https://pypi.org/project/fastapi-jwt/)

Y vamos a implementarlo en nuestra capa de servicio [auth](../api/services/auth.py)
esta librería claramente sigue las convenciones de fastapi, por lo que nos estaremos
ahorrando escribir código que normalmente escribiriamos de la misma manera en
cualquier proyecto.

De la misma forma que fastapi nos provee de cla clase `Depends`, que nos permite
inyectar dependencias en nuestros controladores, también nos provee de la clase
`Security` que sirve para proteger nuestras rutas queririendo "autenticación" del
cliente.

Luego debemos implementar la autorización dependiendo del caso. Por ejemplo
"Si el usuario autenticado es "admin", puede crear un nuevo usuario con el rol
"seller" o "Si el usuario autenticado es "seller", puede crear un producto".

---

## [Middlewares](.)

Los Middlewares son funciones que se ejecutan antes o despues de una petición
de nuestra API. Interceptando las peticiones y respuestas de nuestra API.

Un buen caso de uso podría ser implementar la lógica de autorización en un middleware.
Si bien nosotros no lo vamos a hacer de esta manera la idea es bastante simple:

```
Cliente > Middleware > Request

    (procesamos la petición)

Response > Middleware > Cliente
```

Nosotros lo vamos a utilizar para configurar CORS (Cross-Origin Resource Sharing).
De esta forma vamos a tener como resultado un API totalmente funcional.

y ya solo queda trabajar en los requerimientos de nuestra API.

---

## [CORS](.)

> [fuente](https://fastapi.tiangolo.com/tutorial/cors/)

fastapi nos brinda el middleware `CORSMiddleware` para configurar CORS en nuestra
API. Si tuvieramos mas de un middleware, lo ideal sería crear un paquete para ellos
pero en nuestro caso vamos a implementarlos en nuestro [main.py](../main.py#L17)

---

---
