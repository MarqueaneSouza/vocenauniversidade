from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField()
    universidade = models.CharField(max_length=100)
    curso = models.CharField(max_length=50)
    semestre_admissão = models.IntegerField(choices=[(1, '1º semestre'), (2, '2º semestre')])
    ano_admissao = models.IntegerField()
    semestre_formatura = models.IntegerField(choices=[(1, '1º semestre'), (2, '2º semestre')])
    ano_formatura = models.IntegerField()
    data_exclusao = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        self.nome = self.nome.upper()
        self.curso = self.curso.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
    
    @property
    def admissao_formatada(self):
        return f"{self.semestre_admissao}º Semestre de {self.ano_admissao}"

    @property
    def formatura_formatada(self):
        return f"{self.semestre_formatura}º Semestre de {self.ano_formatura}"

class Acompanhamento(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='acompanhamentos')
    ano = models.IntegerField()
    periodo = models.IntegerField()
    rendimento = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.aluno.nome} - {self.ano}/{self.periodo}"
    
