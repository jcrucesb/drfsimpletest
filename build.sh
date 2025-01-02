#!/usr/bin/env bash
# Exit on error
set -o errexit

# Este comando instala todas las dependencias especificadas en el archivo requirements.txt usando pip. 
# Este archivo lista todas las bibliotecas y paquetes necesarios para el funcionamiento del proyecto Django.
pip install -r requirements.txt

# collectstatic: Este comando es una herramienta de Django que recopila todos los archivos estáticos 
#(como CSS, JavaScript, imágenes, etc.) de todas las aplicaciones instaladas y los copia a un directorio central 
# especificado por la configuración STATIC_ROOT en el archivo settings.py de Django.
# --no-input: Esta opción evita que el comando pida confirmación del usuario durante su ejecución, 
# lo que es útil en entornos de despliegue automatizados o en pipelines de CI/CD
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate