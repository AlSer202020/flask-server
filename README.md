# 🚀 Entorno de Desarrollo Python: Docker, uv y VS Code Dev Containers

Este proyecto define una arquitectura moderna y profesional para el desarrollo de aplicaciones web en Python. Está diseñado para garantizar que el código funcione exactamente igual en cualquier máquina, manteniendo el sistema operativo anfitrión (Windows/Mac/Linux) completamente limpio.

## 📁 Estructura del Proyecto

El entorno está compuesto por los siguientes archivos clave[cite: 1]:

* **`.devcontainer/devcontainer.json`**: Archivo de configuración que le indica a Visual Studio Code cómo conectarse al contenedor y qué extensiones internas (como Python y Ruff) debe instalar[cite: 1].
* **`.devcontainer/devcontainer-lock.json`**: Archivo generado automáticamente para fijar las versiones de las características del contenedor[cite: 1].
* **`docker-compose.yml`**: Orquesta el levantamiento de la infraestructura. Mapea nuestra carpeta raíz al contenedor para habilitar el *hot-reload* (recarga en vivo) de nuestro código[cite: 1].
* **`Dockerfile`**: Define la imagen base (`python:3.12-slim`), instala el gestor ultrarrápido `uv` y prepara el entorno aislado[cite: 1].
* **`pyproject.toml`** y **`uv.lock`**: Definen las dependencias del proyecto de forma estándar y bloquean las versiones exactas para garantizar la reproducibilidad[cite: 1].
* **`app/main.py`**: El código principal de nuestra aplicación web[cite: 1].
* **`app/src/app/__init__.py`**: Archivo que inicializa y marca el directorio como un paquete de Python[cite: 1].
* **`.gitignore`**: Excluye archivos temporales, cachés, carpetas como `.venv` y secretos para mantener el repositorio limpio y seguro[cite: 1].

## 🛠 Tecnologías Clave

* **Docker & Docker Compose:** Aislamiento total del entorno de ejecución.
* **VS Code Dev Containers:** El editor de código se ejecuta *dentro* del contenedor, ofreciendo autocompletado y depuración nativa con las librerías instaladas en Docker.
* **`uv` (de Astral):** Sustituto ultrarrápido de `pip` y `virtualenv` que instala dependencias en milisegundos.
* **Patrón "Sleep Infinity":** El contenedor no arranca el servidor web automáticamente al encenderse, sino que se queda despierto en reposo. Esto permite encender y apagar el servidor web manualmente desde la terminal para una mejor depuración.