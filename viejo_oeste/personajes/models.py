from django.db import models
from django.core.exceptions import ValidationError

class vaquero(models.Model):
    SEXO_CHOICES = [('M', 'Masculino'), ('F', 'Femenino')]
    
    nombre = models.CharField(max_length=25,blank=True)
    apellido = models.CharField(max_length=25,blank=True)
    edad = models.IntegerField(blank=True)
    buscado = models.BooleanField(default=False)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES,blank=True)

    def clean(self):
        super().clean()

        # Validar nombre
        nombre_limpio = self.nombre.strip()  # Eliminar espacios en blanco al inicio y al final

        if not nombre_limpio:
            raise ValidationError({'nombre': 'Tienes que ingresar el nombre'})
        if len(nombre_limpio) < 2 or len(nombre_limpio) > 25:
            raise ValidationError({'nombre': 'El nombre debe tener entre 2 y 25 caracteres'})
        if not nombre_limpio.isalpha():
            raise ValidationError({'nombre': 'El nombre solo puede contener letras y sin espacios'})
        if not nombre_limpio[0].isupper():
            raise ValidationError({'nombre': 'El nombre debe comenzar con una letra mayuscula'})

        # Validar apellido
        apellido_limpio = self.apellido.strip()  # Eliminar espacios en blanco al inicio y al final

        if not apellido_limpio:
            raise ValidationError({'apellido': 'Tienes que ingresar el apellido'})
        if len(apellido_limpio) < 2 or len(apellido_limpio) > 25:
            raise ValidationError({'apellido': 'El apellido debe tener entre 2 y 25 caracteres'})
        if not apellido_limpio.isalpha():
            raise ValidationError({'apellido': 'El apellido solo puede contener letras y sin espacios'})
        if not apellido_limpio[0].isupper():
            raise ValidationError({'apellido': 'El apellido debe comenzar con una letra mayuscula'})

        # Validar edad
        if self.edad == 0:
            raise ValidationError({'edad': 'No puede tener 0 años, La edad debe estar entre 1 y 120 años'})
        if not self.edad:
            raise ValidationError({'edad': 'Tienes que ingresar la edad'})
        if self.edad < 0:
            raise ValidationError({'edad': 'No se permiten negativos ,La edad debe estar entre 1 y 120 años'})
        if self.edad > 120:
            raise ValidationError({'edad': 'La edad debe estar entre 1 y 120 años'})
        
        # Validar sexo
        if self.sexo not in ['M', 'F']:
            raise ValidationError({'sexo': 'Selecciona uno de los sexos'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
