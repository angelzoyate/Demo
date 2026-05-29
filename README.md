Aplicación web
Ejercicios de Aplicaciones Web con Python3, SQLite3 y web.py

## 1. Crear un entorno virtual
Crear el entorno virtual para la instalación de las librerías necesarias para el proyecto.

python3 -m venv .venv
## 2. Crear el archivo .gitignore
Cree el archivo .gitignore para configurar los recursos que no necesitamos que se sincronicen con el reportitorio.

*.pyc
_pycache_/
.venv/
## 3. Activar el entorno virtual
Activar el entorno virtual para realizar la instalación de las librerías necesarias.

source .venv/bin/activate
## 4. Actualizar PIP
Actualizar el instalador de paquetes de python pip (python installer packer). Nota: Recomendable hacerlo para actualizar a la versión correcta.

pip install --upgrade pip
## 5. Crear el archivo runtime.txt
Cree el archivo runtime.txt con la versión utilizada de python3.

python3 -V > runtime.txt
## 6. Instalar el micro-framework web.py
Instalar el micro-framework web.py en el ambiente virtual.

pip install web.py
## 7. Crear el archivo requisitos.yxy
Cree el archivo requirments.yxy con las versiones de las librerías instaladas en el ambiente virtual.

pip freeze > requirements.txt
## 8. Indexar el contenido del repositorio
Indexar todo el contenido del repositorio para incluir todos los archivos nuevos y las modificaciones realizadas al código.

git add .
## 9. Crear un compromiso o punto de control
Crear un punto de control ( commit ) con los cambios realizados al proyecto.

git commit -m "CREATED configuración del ambiente virtual"
## 10. Realiza un push hacia el repositorio
Realiza un push hacia el repositorio para sincronizar los cambios realizados en el proyecto.

git push -u origin main

# demos_web
Web application with Python web.py, HTML and CSS

# Lista de ejercicios 

Lista de ejercicios con web.py

| No.|Archivo|Descripcion| 
|--|--|--|
|1|hello_mundo| Hello word of web.py|