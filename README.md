# BOOTCAMP 3.0

Este repositorio contiene los ejercicios del curso de Python.

---

Para poder ejecutar este código primero vas a necesitar preparar el entorno de
este repositorio, seguí los pasos a continuación:

## Windows (cmd)

```bash
python -m venv .ejercicios_venv
.ejercicios_venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

## Windows (PowerShell)

```bash
python -m venv .ejercicios_venv
.ejercicios_venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Unix-like (Mac o Linux)

```bash
python3 -m venv .ejercicios_venv
source .ejercicios_venv/bin/activate
# Note que llamamos a python y no a python3 en la siguiente linea
python -m pip install -r requirements.txt
```

> Estamos creando un entorno virtual, activándolo y luego instalando las dependencias
> necesarias.
> Luego vamos a tratar este tema con mas detalles.

Como ejercicio, Intente configurar este nuevo entorno virtual (.ejercicios_venv)
por defecto en su editor de texto.

Teniendo activado el entorno virtual, podés ejecutar los ejercicios de la siguiente
manera:

```bash
pytest ./modulosX/claseY/test_claseY.py -vv
```

Donde por supuesto deberá reemplazar X e Y con el módulo y la clase correspondiente.

---

Resumen

### Modulo 1 ( conceptos básicos )

- Clase 1. Introducción a Python3
- Clase 2. Conceptos Generales
- Clase 3. Control de flujo en Python3

### Modulo 2 ( empezando a programar )

- Clase 4. Funciones
- Clase 5. Manejo de datos

### Modulo 3 ( OOP )

- Clase 6. Programación orientada a objetos - Parte 1
- Clase 7. Programación orientada a objetos - Parte 2

### Modulo 4 ( Desarrollo web )

- Clase 8. Introducción a FastAPI
- Clase 9. Fundamentos de las REST APIs con FastAPI

### Modulo 5 ( Creación de una pequeña app )

- Clase 10. Creación de una REST API - Parte 1
- Clase 11. Creación de una REST API - Parte 2
- Clase 12. Autenticación, autorización y servicios en REST APIs

> Sebastián Atlántico Rodríguez Capurro.
