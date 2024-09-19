from django.db import models

# Create your models here.

class Tarea(models.Model):
    
    FINALIZADA = 'Finalizada'
    PENDIENTE = 'Pendiente'
    VENCIDA = 'Vencida'
    TERMINADA_VENCIDA = 'Terminada Vencida'
    
    TIPO_STATUS_CHOICES = [
        (FINALIZADA, 'Finalizada'),
        (PENDIENTE, 'Pendiente'),
        (VENCIDA, 'Vencida'),
        (TERMINADA_VENCIDA, 'Terminada Vencida'),
    ]
    
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    assigned_to = models.CharField(max_length=150)
    status = models.CharField(max_length=30, choices=TIPO_STATUS_CHOICES)
    
    def __str__(self):
        return self.title
    
