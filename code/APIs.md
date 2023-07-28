---
marp: true
theme: gaia

---

# Application Programming Interface (API)

Las interfaces de programación de aplicaciones (API) son un conjunto de reglas y protocolos que permite que diferentes aplicaciones se comuniquen entre sí.

Es una capa de software que permite que dos sistemas interactuen y compartan datos de manera predifinida y estructurada.

---

Permiten que diferentes aplicaciones o servicios se conecten y colaboren de manera segura y eficiente.

Facilitan la integración de funcionalidades y datos de un sistema en otro.

---

Define los métodos, formatos de datos y reglas que otros desarrolladores pueden utilizar para interactura con un sistema específico.

Cuando un desarrollador quiere utilizar una API, envía una solicitud a través de la API con ciertos parámetros y, a cambio, recibe una respuesta con los datos o resultados que necesita.

---

## Tipos de APIs

**1. API Web**

Permiten la comunicación a través de internet. Se basan en el protocolo **HTTP** y se utilizan para acceder a recursos y servicios en la web.

**2. API REST**

Tipo de **API Web** que sigue los principios de **REST** *(Representational State Transfer)*. Utiliza los métodos **HTTP** *(GET, POST, PUT, DELETE)* para realizar operaciones en recursos identificados por URLs.

---

**3. API SOAP**

Utilizan el protocolo **SOAP** *(Simple Object Access Protocol)* para la comunicación. Son más complejas que las **API REST** y estan basadas en **XML**.

**4. API GraphQL**

Lenguaje de consulta y manipulación de datos que permite a los clientes solicitar solo la información que necesitan. A diferencia de las **API REST**, donde el servidor determina el formato de los datos, en **GraphQL**, el cliente específica que datos quiere recibir.

---

## Autenticación y Autorización

Muchas APIs requieren autenticación para asegurarse de que solo usuarios autorizados tengan accesos a ciertos recursos o funcionalidades.

La **autenticación** verifica la identidad del usuario, mientras que la **autorización** determina que acciones tiene permitido realizar.

---

# HTTP

Protocolo de comunicación utilizado en la **World Wide Web** para transferir datos entre un cliente y un servidor web.

El cliente envía solicitudes HTTP al servidor, y el servidor responde con respuestas HTTP que contienen los datos solicitados.

---

## Métodos HTTP

Definen las acciones que se pueden realizar en los recursos identificados por URLs.

**1. GET**

Solicita datos de un recurso específico.

**2. POST**

Envía datos para que sean procesados por un recurso identificado.

---

**3. PUT**

Actualiza por completo un recurso existente o crea uno nuevo si no existe.

**4. DELETE**

Elimina un recurso específico identificado por la URL.

**5. PATCH**

Actualiza parcialmente un recurso existente.

---

# REST

Estilo arquitectónico utilizado para diseñar APIs Web. Se basa en el concepto de recursos, que son entidades o datos que pueden ser accedidos y manipulados a través de URLs.

**1. Recursos**

Entidades identificables, como usuarios, publicaciones o productos, que pueden ser accedidos a través de URLs.

**2. Métodos HTTP**

**REST** utiliza los métodos **HTTP** *(GET, POST, PUT, DELETE, PATCH)* para operar en los recursos.

---

**3. Estado representacional**

Las respuestas de las solicitudes HTTP en REST suelen contener una representación del estado del recurso.

**4. Sin estado**

Cada solicitud HTTP a un servicio REST debe contener toda la informacion necesaria para entender y procesar la solicitud. 

El servidor no debe almacenar ningún estado de la sesión del cliente.

---

**5. URI**

Uniform Resource Identifier.

Las URLs en REST deben ser únicas y representar de manera significativa los recursos a los que se accede.

**6. Formatos de datos**

REST generalmente utiliza formatos de datos como JSON (JavaScript Object Notation) o XML (eXtensible Markup Language) para intercambiar información.

---

# FastAPI

Framework web moderno y de alto rendimiento para construir APIs en Python.


---

## Instalación

Para instalar FastAPI es necesario contar con la versión Python 3.6 o posterior y un servidor web basado en ASGI.

```python
pip install fastapi uvicorn
```

---

## ASGI

**Asynchronous Server Gateway Interface**

Especificacion para servidores y aplicaciones web en Python que permite el procesamiento asíncrono de solicitudes HTTP.

---

## WSGI

**Web Server Gateway Interface**

Especificación para servidores y aplicaciones web en Python que permite el procesamiento síncrono de solicitudes HTTP.

---

# Uvicorn

Servidor web ASGI de alto rendimiento que se utiliza principalmente para ejecutar aplicaciones web y APIs escritas en Python.

**1. Asincronía**

Procesamiento asíncrono de solicitudes. 

Esto permite que maneje múltiples conexiones simultáneamente sin bloquear el proceso principal, lo que mejora significativamente el rendimiento y la capacidad de respuesta del servidor.

---

**2. Integración con ASGI**

Compatible con aplicaciones web escritas siguiendo la especificación ASGI, como FastAPI, Starlette, etc.

**3. Modo de desarrolo con recarga automática**

Uvicorn proporciona una opción `--reload` que, cuando se habilita, recargará automáticamente la aplicación cada vez que detecte cambios en el código fuente, lo que facilita el desarrollo y la depuración.

---

## Primeros pasos

Crea un archivo `main.py` y comienza con un "Hola, mundo!".

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return{"Hello": "World"}
```

---

## Ejecutar la aplicación

```python
uvicorn main:app --reload
```

`main` es el nombre del archivo `main.py` y `app` es el nombre de la instancia de **FastAPI** que se encuentra dentro del archivo.

---

## Definición de rutas y parámetros

FastAPI utiliza decoradores para definir rutas y operaciones HTTP.

Puedes especificar parámetros en las rutas para recibir datos de solicitud.

---

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}
```

---

## Modelos y validaciones

**FastAPI** permite definir modelos **Pydantic** y utilizarlos para validar y convertir automáticamente los datos de entrada y salida.

---

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return item
```

---

# Pydantic

Biblioteca de Python que proporciona una forma rápida y sencilla de definir y validar datos mediante el uso de modelos de datos.

La principal funcionalidad de Pydantic es permitir la definicion de modelos de datos con anotaciones de tipo.

Esos modelos de datos pueden representar estructuras complejas, como diccionarios anidados o listas, y contener tipos de datos especificos para cada atributo.

---

**1. Validación de datos**

Pydantic se encarga de la validacion automatica de los datos proporcionados para asegurarse de que cumplan con las restricciones definidads en el modelo.

**2. Conversión de tipos**

Podemos convertir automáticamente los datos a los tipos adecuados, si es posible, según las anotaciones de tipo del modelo.

---


**3. Documentación automatica**

Los modelos definidos con Pydantic pueden utilizarse para generar automáticamente documentación detallada sobre los campos, tipos y restricciones.


**4. Serialización y deserialización**

Pydantic facilita la conversiÓn de los modelos a formatos de serializaciÓn como JSON o XML.
