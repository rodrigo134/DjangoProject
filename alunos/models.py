from django.db import models

# Create your models here.

class Aluno(models.Model):
    
    nome = models.CharField(max_length=255)
    idade = models.PositiveIntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.nome