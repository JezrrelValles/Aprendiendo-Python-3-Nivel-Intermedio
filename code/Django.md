---
marp: true
theme: gaia

---

### Django

**Web Framework** para la creación de aplicaciones web en **Python**.

---

### Instalación

Abre una terminal o linea de comandos y ejecuta el siguiente comando para instalar **Django** usando ```pip```

```python
pip install django
```

---
### Crear un nuevo proyecto

Una vez que **Django** esté instalado, puedes crear un nuevo proyecto. 

En la terminal, navega hasta la ubicación donde deseas crear tu proyecto y ejecuta el siguiente comando

```python
django-admin startproject nombre_proyecto
```

Reemplaza ```nombre_proyecto``` con el nombre que desees darle a tu proyecto. 

Esto creará una carpeta con el nombre del proyecto y contendrá la estructura inicial de tu proyecto **Django**.

---

### Iniciar el servidor de desarrollo

Dentro de la carpeta de tu proyecto, ejecuta el siguiente comando para iniciar el servidor de desarrollo de Django:

```python
cd nombre_proyecto
python manage.py runserver
```

El servidor se ejecutará en tu servidor local ```http://127.0.0.1:8000/```.

---

### Comprobar funcionalidad

Si accedes a ```http://127.0.0.1:8000/```, deberías ver una página de bienvenida de **Django** que indica que el servidor se está ejecutando correctamente.