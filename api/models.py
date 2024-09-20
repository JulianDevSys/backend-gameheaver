from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
class Persona(models.Model):
    username = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    password=models.CharField(max_length=250)

    def __str__(self):
        return f"bienvenido a la applicacion {self.username}"
    
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)