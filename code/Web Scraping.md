---
marp: true
theme: gaia
---

# Web Scraping

Proceso de extracción automática de datos de páginas web.

1. Envia solicitudes HTTP a una página web

2. Analiza código HTML o XML resultante

3. Extrae la información relevante

Existen bibliotecas y herramientas en Python que facilitan el proceso de extracción de datos.


---

# Requests

Biblioteca de **Python** utilizada para realizar **solicitudes HTTP** de manera sencilla y eficiente.

Permite enviar solicitudes a servidores web y recibir respuesta.

Algunas de las características clave incluyen:

1. Sintaxis sencilla

2. Gestión de encabezados y parámetros

3. Autenticacion y cookies

---

4. Manejo de errores y redirecciones

5. Sesiones persistentes

---

## Solicitudes HTTP

Mensajes enviados entre un cliente y un servidor web para intercambiar información.

En el contexto del web scraping, se utilizan solicitudes HTTP para obtener el código fuente HTML de una página web.

1. GET

2. POST

3. PUT

4. DELETE

---

## Análisis del codigo HTML

Consiste en examinar el código HTML obtenido de una página web para identificar los elementos de interés que se desean extraer, como texto, imágenes o datos estructurados.

---

## HTML

Lenguaje de marcado utilizado para estructurar y presentar el contenido de una página web.

Define la estructura y organizacion de los elementos en la pagina mediante etiquetas.

---

## CSS

Lenguaje de estilo utilizado para describir la presentación y el diseño de una página web.

Permite controlar el color, fuente, tamaño y disposición de los elementos HTML en la página.

---

## Inspeccionar elementos

Proceso de examinar código fuente de una página web utilizando las herramientas de desarrollo de un navegador.

Permite ver la estructura HTML de la página, identificar elementos y obtener información sobre ellos, como sus clases, identificadores y atributos.

---

# BeautifulSoup

Biblioteca de **Python** utilizada para **analizar y extraer datos** de **archivos HTML y XML.** 

Proporciona una forma fácil y legible de navegar por el código fuente HTML y extraer información relevante.

Algunas características importantes de BeautifulSoup son:

1. Analisis y navegacion

2. Seleccion de elementos

---

3. Extraccion de datos

4. Limpieza y formateo

5. Integracion

---

# Análisis y navegación del código HTML

BS4 analiza el codigo fuente HTML y lo convierte en una estructura de árbol de objetos Python.

Esto permite navegar y explorar la estructura del HTML de manera intuitiva.

1. find()

2. find_all()

---

4. find_next_sibling()

5. find_all_next()

---

# Seleccion precisa de elementos

BS4 proporciona una amplia gama de opciones para seleccionar elementos especificos en una pagina web.

Esto es util cuando se necesita extaer datos de secciones particulares o cuando se desea filtrar eleentos basado en ciertos criterios.

Puedes utilizar selectores CSS para seleccionar elementos en funcion de clases, identificadores o estructura de etiquetas.

Ademas, los metodos de busqueda y filtrado permiten una seleccion mas precisa de los elementos deseados.

---

# Extracción de datos

Proceso de seleccionar y extraer información específica de una página web utilizando técnicas como la búsqueda de elementos HTML por etiquetas, clases, identificador o atributos.

BS4 proporciona metodos y atributos para extraer datos especificos de ellos.

Puedes extraer texto utilizando el atributo text, obtener atributos especificos utilizando el metodo get(), y buscar elementos hermanos o siguientes utilizando los metodos de navegacion.

BS4 tambien permite extraer datos estructurados, como tablas, listas u otros elementos HTML especificos, facilitando el proceso de extraccion y manipulacion de datos.

---

# Manejo de contenido mal formateado

Las paginas web pueden conteener contenido HTML mal formateado, etiquetas incorrectas o errores sintacticos.

BS4 es capaz de manejar y corregir estos problemas, lo que facilita el proceso de web scraping incluso en paginas con estructuras complicadas.

---

# Limpieza y formateo

BS4 proporciona metodos para limpiar y formatear el contenido HTML extraido.

Puedes eliminar etiquetas no deseadas, comentarios o espaciones en blaco innecesarios para obtener un contenido mas limpio y legible.

---

# Manejo de estructuras de datos

---

# Formularios y páginas dinámicas

---

# Proceso

1. Identificar la página web objetivo

2. Inspeccionar la estructura HTML

3. Importar las bibliotecas necesarias

4. Realizar solicitudes HTTP

5. Crear un objeto BeautifulSoup

---

6. Identificar los elementos de interés

7. Extraer los datos

8. Almacenar los datos

9. Limpieza y procesamiento de datos

10. Presentación y visualización de datos



---

