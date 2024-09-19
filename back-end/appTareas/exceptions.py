# exceptions.py
from rest_framework.views import exception_handler
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # Personaliza el mensaje para NotFound
    if isinstance(exc, NotFound):
        return Response({"error": "Tarea no encontrada"}, status=404)

    # Puedes agregar más personalizaciones aquí si es necesario

    return response
