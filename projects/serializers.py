# Hacemos referencia a el módulo de restframework e importamos los serializers.
from rest_framework import serializers
# Ahora debemos llamar al modelo de la BD que hemos creado anteriormente.
from .models import Proyect

# Creamos el nombre de nuestra clase.
# serializers.ModelSerializer, convierte los modelos de la BD, en datos que pueden ser consultados.
class ProjectSerializers(serializers.ModelSerializer):
    # Creamos la clase meta:
    class Meta:
        model = Proyect
        # Ahora agregamos los campos que pueden ser consultados.
        # Creamos una TUPLA.
        fields = ('id', 'title', 'description', 'technology')
        # Campo de solo lectura. Esto es para NO modifiquen la fecha de creación, tampo eliminar, etc.
        read_only_fields = ('created_at',)