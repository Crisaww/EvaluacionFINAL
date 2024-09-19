from rest_framework import serializers
# Se importa el modulo serializer

from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    
    #Agregar los campos necesarios a mostrar
    #si se desea agregar todos los campos se 
    #puede utilizar la función __all__
    
    class Meta:
        model=Tarea
        fields ='__all__'
        # fields = {
        #     'id',
        #     'titulo',
        #     'autor',
        #     'isbn',
        #     'genero',
        #     'num_ejem_disponibles',
        #     'num_ejem_ocupados'
        # }