from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField()
    universidade = models.CharField(max_length=100)
    curso = models.CharField(max_length=50)
    data_admissao = models.DateField()
    previsao_formatura = models.DateField()
    data_exclusao = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Acompanhamento(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='acompanhamentos')
    ano = models.IntegerField()
    periodo = models.IntegerField()
    rendimento = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.aluno.nome} - {self.ano}/{self.periodo}"
    
