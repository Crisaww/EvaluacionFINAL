from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import Tarea
from .serializer import TareaSerializer

class TareaView(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    queryset = Tarea.objects.all()

    def retrieve(self, request, *args, **kwargs):
        try:
            # Obtener el objeto usando el método get_object
            instance = self.get_object()
        except NotFound:
            # Si no se encuentra el objeto, retorna un mensaje personalizado
            return Response({'error': 'Tarea no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        # Si el objeto se encuentra, serializarlo y devolver la respuesta
        serializer = self.get_serializer(instance)
        
         # Si el objeto se encuentra, retornar una respuesta vacía con el estado 204
        return Response(serializer.data)

    def get_object(self):
        """
        Override to use the custom exception handling
        """
        queryset = self.get_queryset()
        filter_kwargs = {self.lookup_field: self.kwargs.get(self.lookup_field)}
        obj = queryset.filter(**filter_kwargs).first()
        if obj is None:
            raise NotFound()
        return obj
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Tarea eliminada con éxito'}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
