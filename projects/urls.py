# Este línea importa la clase DefaultRouter desde el módulo routers de Django Rest Framework. 
# El router es responsable de automatizar la creación de rutas URL para las vistas.
from rest_framework import routers
# Aquí se importa la clase ProjectViewSet desde el módulo api del mismo paquete. ProjectViewSet 
# es una vista basada en clases que maneja operaciones CRUD (Create, Read, Update, Delete) para el modelo Project.
from .api import ProjectViewSet

# Debemos ejecutar el routers.
# Se crea una instancia de DefaultRouter, que es el tipo de router más comúnmente utilizado en DRF. 
# Este router se encargará de mapear las vistas a las rutas URL.
router = routers.DefaultRouter()
# Registramos la ruta, hacemos referencia al archivo api y nos traemos la case ProjectViewSet, 
# luego agregamos un nombre a la ruta creada, en este caso; 'projects'.
# 'api/projects': Es el prefijo de la URL. Esto significa que todas las rutas relacionadas con el 
# ProjectViewSet comenzarán con /api/projects/.
# ProjectViewSet: Es la vista que se va a mapear a esta ruta. 
# Esta vista maneja las operaciones CRUD para el modelo Project.
# 'projects': Es el nombre de la ruta, que se utiliza internamente por el router para identificar esta ruta.
router.register('api/projects', ProjectViewSet, 'projects')

# De igual manera debemos crear el urlpatterns.
# Finalmente, se asignan las URLs generadas por el router a la variable urlpatterns. 
# Esto es lo que se incluirá en el archivo urls.py principal del proyecto para que las rutas estén disponibles.
urlpatterns = router.urls