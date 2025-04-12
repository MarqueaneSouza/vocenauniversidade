from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    telefome = models.CharField(max_length=20)
    #cpf = models.CharField(max_length=14)
    cpf = models.CharField(max_length=14, unique=True) #restrição para garantir cpf com valores únicos. Dado por outra IA
    email = models.EmailField()
    universidade = models.CharField(max_length=100)
    curso = models.CharField(max_length=50)
    data_admissao = models.DateField()
    previsao_formatura = models.DateField()
    data_exclusao = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome
    