---
marp: true
theme: gaia
---

# Web Scraping

Proceso de extracción automática de datos de páginas web.

**1. Envia solicitudes HTTP a una página web para obtener su código fuente.**

**2. Analiza el código HTML o XML resultante.**

**3. Extrae la información relevante.**

Existen bibliotecas y herramientas en Python que facilitan el proceso de extracción de datos.


---

# Requests

Biblioteca de **Python** utilizada para realizar **solicitudes HTTP** de manera sencilla y eficiente.

Permite enviar solicitudes a servidores web y recibir respuestas.

**1. Sintaxis sencilla**

**2. Gestión de encabezados y parámetros**

**3. Autenticacion y cookies**

---

## Solicitudes HTTP

Mensajes enviados entre un cliente y un servidor web para intercambiar información.

En el contexto del web scraping, se utilizan **solicitudes HTTP** para obtener el código fuente HTML de una página web.

**1. GET**

Obtener información

**2. POST**

Crear información

---

**3. PUT**

Actualizar información

**4. PATCH**

Actualizar parcialmente información.

**5 DELETE**

Eliminar información

---

## Códigos de respuesta HTTP

Códigos númericos que indican el resultado de una solicitud HTTP realizada por un cliente a un servidor web.

El servidor comunique el estado de la solicitud y cualquier error o éxito que haya ocurrido durante el procesamiento de la misma.


Se dividen en 5 clases, cada una representada por el primer dógito del código.

**1. Respuestas informativas**

Indican que la solicutd ha sido recibida y el servidor está continunando el proceso.

* **100** Continuar
* **101** Cambio de protocolo

---

**2. Respuestas exitosas**

Indican que la solicitud se ha procesado correctamente por el servidor.

* **200** OK
* **201** Creado
* **204** Sin contenido

**3. Redirecciones**

Indican que se necesita una acción adicional para completar la solicitud.

* **301** Movido permanente
* **302** Encontrado
* **307** Redirección temporal

---

**4. Errores del cliente**

Indican que hubo un error en la solicitud realizada por el cliente.

* **400** Solicitud incorrecta
* **401** No autorizado
* **404** No encontrado

**5. Errores del servidor**

Indican que hubo un error en el servidor mientras procesaba la solicitud.

* **500** Error interno del servidor
* **503** Servicio no disponible

---

## Análisis del codigo HTML

Examinar el código fuente obtenido de una página web para identificar los elementos de interés que se desean extraer, como texto, imágenes o datos estructurados.

---

## Inspeccionar elementos

Proceso de examinar código fuente de una página web utilizando las herramientas de desarrollo de un navegador.

Permite ver la estructura HTML de la página, identificar elementos y obtener información sobre ellos, como sus clases, identificadores y atributos.

---

## HTML

Lenguaje de marcado utilizado para estructurar y presentar el contenido de una página web.

Define la estructura y organizacion de los elementos en la pagina mediante etiquetas.

```python
<div class="titulo" id="titulo" title="titulo">Hola, mundo!</div>

<a href="https://www.ejemplo.com/">Link</a>

<img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
```

---

## CSS

Lenguaje de estilo utilizado para describir la presentación y el diseño de una página web.

Permite controlar el color, fuente, tamaño y disposición de los elementos HTML en la página.

---

# BeautifulSoup

Biblioteca de **Python** utilizada para **analizar y extraer datos** de **archivos HTML y XML.** 

Proporciona una forma fácil y legible de navegar por el código fuente HTML y extraer información relevante.

**1. Analisis y navegacion**

**2. Seleccion de elementos**

---

**3. Extraccion de datos**

**4. Limpieza y formateo**

**5. Integracion**

---

# Análisis y navegación del código HTML

Con **BeautifulSoup** puedes analizar el código fuente HTML y convertirlo en una estructura de árbol de objetos **Python**.

Esto permite navegar y explorar la estructura del HTML de manera intuitiva.

1. find()

2. find_all()

---

4. find_next_sibling()

5. find_all_next()

---

# Selección precisa de elementos

**BeautifulSoup** proporciona una amplia gama de opciones para seleccionar elementos especificos en una página web.

Esto es útil cuando se necesita extaer datos de secciones particulares o cuando se desea filtrar elementos basados en ciertos criterios.

Puedes utilizar selectores **CSS** para seleccionar elementos en función de clases, identificadores o estructura de etiquetas.

Además, los métodos de búsqueda y filtrado permiten una selección más precisa de los elementos deseados.

---

# Extracción de datos

Proceso de seleccionar y extraer información específica de una página web utilizando técnicas como la búsqueda de elementos **HTML** por etiquetas, clases, identificador o atributos.

**BeautifulSoup** proporciona métodos y atributos para extraer datos específicos de ellos.

Puedes extraer texto utilizando el atributo text, obtener atributos específicos utilizando el metodo get(), y buscar elementos hermanos o siguientes utilizando los metodos de navegación.

Tambien permite extraer datos estructurados, como tablas, listas u otros elementos HTML específicos, facilitando el proceso de extracción y manipulación de datos.

---

# Manejo de contenido mal formateado

Las páginas web pueden contener lenguaje HTML mal formateado, etiquetas incorrectas o errores sintácticos.

**BeautifulSoup** es capaz de manejar y corregir estos problemas, ya que ofrece una serie de analizadores para lidiar con el contenido mal formateado.

```python
soup = BeautifulSoup(html, 'html.parser')
```

---

# Limpieza y formateo

**BeautifulSoup** proporciona métodos para limpiar y formatear el contenido HTML extraído.

Puedes eliminar etiquetas no deseadas, comentarios o espaciones en blanco innecesarios para obtener un contenido más limpio y legible.

Utilizando el método extract() de **BeautifulSoup**, puedes eliminar etiquetas específicas o secciones completas del contenido que no necesitas.

---


# Paginación

Concepto común en la web que refiere a la división de contenido en varias páginas para mejorar la experiencia del usuario y facilitar la carga y visualizacion del contenido.

**BeautifulSoup** no realiza la paginación de manera automática, ya que su función principal es analizar y extraer datos de páginas web. Sin embargo, puedes combinar **BeautifulSoup** con otras bibliotecas o técnicas para navegar a traves de las páginas paginadas y extraer datos de cada una de ellas.

Es importante tener en cuenta que el proceso de paginación puede variar según el sitio web que estés scrapeando. Algunos sitios utilizan enlaces numéricos para la paginación, mientras que otros pueden tener botones "siguiente" y "anterior".

---

# Expresiones regulares

Patrones que se utilizan para buscar y manipular texto mediante reglas específicas.

Python contiene un módulo especializado en analizar y comprender expresiones regulares.

```python
import re
```

**1. Búsqueda de patrones**

Puedes usar la función ```re.search()``` para buscar un patrón específico en una cadena de texto.

---

**2. Coincidencia de patrones múltiples**

Puedes utilizar la función ```re.findall()``` para encontrar todas las ocurrencias del patrón en una cadena y obtenerlos como una lista.

**3. Extracción utilizando grupos**

Puedes utilizar paréntesis en el patrón para crear grupos y luego extraer partes específicas de la coincidencia utilizado la funcion ```group()```.

**4. Reemplazo de patrones**

Puedes utilizar la función ```re.sub()``` para reemplazar un patrón específico en una cadena con otro texto.

---

# Web Scraping para Análisis de Datos

**1.** Identificar la página web objetivo

**2.** Inspeccionar la estructura HTML

**3.** Importar las bibliotecas necesarias

**4.** Realizar solicitudes HTTP

**5.** Crear un objeto BeautifulSoup

---

**6.** Identificar los elementos de interés

**7.** Extraer los datos

**8.** Almacenar los datos

**9.** Limpieza y procesamiento de datos

**10.** Presentación y visualización de datos

