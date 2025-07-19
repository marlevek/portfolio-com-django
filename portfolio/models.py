from django.db import models


class Habilidade(models.Model):
    nome = models.CharField(max_length=10)

    def __str__(self):
        return self.nome 

    
class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    tecnologia = models.CharField(max_length=150)
    github = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.titulo 