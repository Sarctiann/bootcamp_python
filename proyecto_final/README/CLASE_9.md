# Proyecto Final - API

![banner](bootcamp3.png)

> [Volver al README principal](../README.md)

## Modulo 4 - Clase 9: Fundamentos de las REST APIs

### Módelo Cliente/Servidor

- [¿Que es un servidor?](#server) (contexto aplicación web)
  `[protocol, host, port, handler, uri, response]`
- [¿Que es un cliente?](#client) (mismo contexto)
  `[resource, request]`
- [Verbos HTTP](#verbos-http)
  [fuente](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
  `[GET, POST, PUT, DELETE]`
- [Códigos de status del protocolo HTTP](#códigos-de-status),
  [fuente](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
  `[200, 300, 400, 500]`

### Continuamos con FastApi

- [Creación de un Modelo básico](#creación-de-un-modelo-básico)
  (Producto)
- [Validación del Modelo](#validacioó-del-modelo)
- [Verificación en swagger](#verificacion-en-swagger)
- [Verificación en Postman](#verificación-en-postman)
- [Notas sobre otros clientes](#notas-sobre-otros-clientes)

---

---

### [Server](.)

"Un "servidor" es un programa que se encarga de procesar las peticiones de un
cliente" En nuestro caso vamos a trabajar con un servidor web, esto significa que
nuestro servidor es un programa que recibe peticiones de clientes a través de una
red. Hay 3 cosas que tenemos que tener en cuenta ANTES del servidor:

- #### Protocol:

  El protocolo es el tipo de red que utilizamos. Por ejemplo: `http`, `https`,
  `ftp`. Para nuestra aplicación web, vamos a utilizar dos protocolos: `http` y
  `https` (http secure).
  En realidad el protocolo es prácticamente el mismo pero en `https` las peticiones
  se cifran.
  En nuestro local solo vamos a trabajar con http, pero cuando vamos a trabajar con
  un servidor externo, vamos a trabajar con https.

- #### Host:

  El host es la IP o nombre (DNS) de la red donde se encuentra el servidor.
  Por ejemplo: `localhost`, `127.0.0.1` (estos dos son la IP de nuestra red local).
  Cuando "despleguemos" nuestro servidor esto será reemplazado por la ip o el
  nombre que nos proporcione el servicio de hosting.

- #### Port:
  Esto es el puerto de red que utilizamos con nuestra API. Por ejemplo: `80`,
  `8080`. En nuestra API vamos a pedirle a nuestro host que nos proporcione el
  puerto. Si el puerto está disponible se levantará el servidor en el mismo y
  montará nuestra API. Cuando trabajamos con un servidor externo, el puerto queda
  incluido en el DNS.

Desde nuestro servidor vamos a configurar estas 3 cosas, que como podemos ver,
tienen que ver con "la computadora" y "la red", donde vamos a levantar nuestro
servidor.

Luego tenemos la parte divertida, la API. Donde vamos a desarrollar nuestra
aplicación. Normalmente en este contexto nos referimos a esto como "el servidor".
Aunque como ya vimos esto puede ser un poco ambiguo. Una forma mas adecuada sería
referirnos a esta parte como "la API" o "la aplicación".

Y acá podemos destacar otras 3 responsabilidades:

- #### Handler:

  El handler (o manejador) es justamente el programa que se encarga de procesar
  las peticiones de un cliente (es decir, la applicación que vamos a crear)
  ni bien instalamos fastapi, e instanciamos la app (app = FastAPI()).
  Estamos listo para ejecutar: `fastapi dev | run` y todo lo anterior se va a
  configurar y ejecutar con valores por defecto. Sin embargo nuestro handler está
  vacio. es decir que nuestra aplicación no puede hacer nada aún.

- #### URI:

  La URI (Uniform Resource Identifier) es la parte de la URL que indica que tipo
  de recurso estamos solicitando. Por ejemplo: `/` (home), `/users` (users).
  acá es donde somos nosotros donde necesariamente tenemos que definir estas rutas
  y como las vamos a "manejar", a este par de `[ruta, funcionalidad]` las llamamos
  puntos finales (endpoints).

- #### Response:

  Finalmente resnponse, no es otra cosa que una respuesta HTTP que le damos a
  nuestro cliente. Esta respuesta puede ser de diferentes maneras, pero los 3
  partes que nos interesa son:

  - `status_code`: es un código númerica que indica el estado resultante de la
    petición.
  - `headers`: es información del protocolo HTTP en una lista de pares `key:value`.
  - `body`: Si todo va bien, esta es la información que solicitamos.

---

### [Client](.)

El cliente es el programa que va a hacer las peticiones a los servidores.
En nuestro caso el cliente va a ser una app front-end que va a hacer peticiones
desde un navegador. Estas peticiones lógicamente tienen que respetar el mismo
protocolo y tienen que considerar dos factores:

- #### Resource:

  El "Recurso" es la applicación del cliente, que se obtiene de la petición al
  servidor que sirve nuestro cliente. En nuestro caso la applicación que van a
  trabajar en el segmento de FrontEnd es de tipo "SPA" (single page application).
  Esto significa que el servidor frontend, va a enviar un "único recurso"
  (la app). Y luego esta app va a realizar las peticiones al servidor backend,
  sin recargar la pagina.

- #### Request:

  Las peticiones (requests) se crean y se envian a los servidores de backend. Y
  tienen la siguiente estructura: `protocolo://host:port/uri`. Además van
  acompañadas de el Método (hablaremos de esto pronto), los Headers (hablaremos de
  esto luego), y el Body (de ser necesario). Lógicamente en nuestra API nosotros
  tendremos que crear nuestros **endpoints** teniendo en cuenta estos Métodos,
  Headers y Body.

---

### [Verbos HTTP](.)

Los verbos http (HTTP verbs) son las acciones que podemos realizar con las
peticiones. Nosotros vamos a utilizar los verbos GET, POST, PUT, DELETE. Pero
hay varios más que pueden investigar en el enlace adjunto en el índice.
Notros podríamos solicitar cualquier tipo de recurso con cualquiera de estos
métodos en realidad. Pero por convención vamos a utilizar estos 4 asociados a las
diferentes operaciones CRUD (Create, Read, Update, Delete):

| Verbos | Acciones |
| :----: | :------: |
|  GET   |   Read   |
|  POST  |  Create  |
|  PUT   |  Update  |
| DELETE |  Delete  |

---

### [Códigos de status](.)

Los códigos de status se corresponden con los resultados de las peticiones.
A nosotros nos interesan 4 grupos principalmente, los 200s, 300s, 400s y 500s.
Pueden consultarlos en el enlace adjunto en el índice para una información mas
detallada pero de momento nos vamos a enfocar en la idea general:

| Códigos |     Acciones      |
| :-----: | :---------------: |
|   200   | Success Responses |
|   300   |   Redirections    |
|   400   |  Request Errors   |
|   500   |   Server Errors   |

---

---

# Continuamos con el Proyecto

### [Creación de un modelo básico](.)

Los módelos no son mas que clases que nos permiten representar esquemas de datos.
estos esquemas van a ser consistentes entre nuestro front-end, back-end y base
de datos.
Para esto, vamos a empezar a estructurar nuestra app como se debe, por lo que
primero vamos a eliminar el código de la clase anterior (lo de pelis).
Luego vamos a crear un **paquete** `models` que contenga nuestros módelos. Dentro
vamos a crear un archivo [`products.py`](../models/products.py) que contenga nuestra
clase `Product`.

También vamos a exponerlo en nuestro archivo [`__init__.py`](../models/__init__.py)
para poder importarlo directamente en [`main.py`](../main.py#L5).

---

### [Validación del modelo](.)

Como podemos ver en el endpoint [`POST /products`](../main.py#L52), la validación
de los datos se hace de manera automatica gracias a fastapi y pydantic.

---

### [Verificación en swagger](.)

Levantemos nuestra app y vayamos a [DOCS](http://localhost:8000/docs) para ver como
funciona.

---

### [Verificación en Postman](.)

Probemoslo con un cliente diferente. En vez de postman vamos a utilizar ThunderClient
el cual vamos a tener integrado en vscode.

---

### [Notas sobre otros clientes](.)

Es importante tener en cuenta que la comunicación entre el cliente y el servidor
tiene algunos mecanismos para el intercambio de recursos, uno de ellos es
[CORS](https://developer.mozilla.org/es/docs/Web/HTTP/CORS), los navegadores tienen
un mecanismo de seguridad que restringe el cruce de recursos. Por lo que probablemente
tendremos que configurar CORS en nuestra app.

---

---
