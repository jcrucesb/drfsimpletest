# Llamamos al modelo Proyect.
from .models import Proyect
# Importamos rest_framework.
from rest_framework import viewsets, permissions
# Llamamos al serializers creado anteriormente.
from .serializers import ProjectSerializers

#En Django Rest Framework (DRF), la clase ModelViewSet es una herramienta poderosa 
# y versátil que permite crear vistas para manejar operaciones CRUD (Create, Read, Update, Delete) de manera eficiente.
# viewsets.ModelViewSet; maneja todas las operaciones CRUD para el modelo Project utilizando el serializador 
# ProjectSerializer. 
# Esto significa que con solo estas pocas líneas de código, se crean endpoints para listar, recuperar, crear, 
# actualizar y eliminar proyectos
class ProjectViewSet(viewsets.ModelViewSet):
    # Que consultas se pueden hacer; UPDATE, DELETE,ETC.
    # Este vendría siendo el QUERYSET.
    queryset = Proyect.objects.all()
    # Verificamos los permisos. Creamos una lista que tan solo tendrá quienm tiene permitido realizar las queryset,
    # en este casos, para ejemplo del proyecto, todos tienen permitido realizar lasconsultas o queryset.
    # Este sería para que las consulta las pueda realizar alguien logueado; permission_classes = [permissions.auth]
    #permission_classes = [permissions.auth]
    permission_classes = [permissions.AllowAny]
    # 
    serializer_class = ProjectSerializers
    

