from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=30)
    cpf = models.CharField(max_length=30)



# Create your models here.
