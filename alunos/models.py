from django.db import models


MESES = [
    ('01', 'Janeiro'),
    ('02', 'Fevereiro'),
    ('03', 'Março'),
    ('04', 'Abril'),
    ('05', 'Maio'),
    ('06', 'Junho'),
    ('07', 'Julho'),
    ('08', 'Agosto'),
    ('09', 'Setembro'),
    ('10', 'Outubro'),
    ('11', 'Novembro'),
    ('12', 'Dezembro'),
]

ANOS = [(str(ano), str(ano)) for ano in range(2000, 2035)]

STATUS_CHOICES = [
    ('ativo', 'Ativo'),
    ('inativo', 'Inativo',)
]

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField()
    universidade = models.CharField(max_length=100)
    curso = models.CharField(max_length=50)

    mes_admissao = models.CharField(max_length=2, choices=MESES, blank=True, null=True)
    ano_admissao = models.IntegerField(blank=True, null=True)
    mes_formatura = models.CharField(max_length=2, choices=MESES, blank=True, null=True)
    ano_formatura = models.IntegerField(blank=True, null=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='ativo'
    )

    justificativa_exclusão = models.TextField(
        blank=True,
        null=True,
        verbose_name="Informe o motivo da exclusão"
    )
    
    def clean(self):
        from django.core.exceptions import ValidationError

        if self.status == 'inativo' and not self.justificativa_exclusão:
            if self.status == 'inativo' and not self.justificativa_inatividade:
             raise ValidationError({'justificativa_inatividade': 'Obrigatório informar a justificativa se o aluno estiver inativo.'})
    
    def admissao_formatada(self):
        if self.mes_admissao and self.ano_admissao:
            return f"{self.mes_admissao}/{self.ano_admissao}"
        elif self.ano_admissao:
            return f"{self.ano_admissao}"
        return "-"

    def formatura_formatada(self):
        if self.mes_formatura and self.ano_formatura:
            return f"{self.mes_formatura}/{self.ano_formatura}"
        elif self.ano_formatura:
            return f"{self.ano_formatura}"
        return "-"

    data_exclusao = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.nome:
            self.nome = self.nome.upper()
        if self.universidade:   
            self.universidade = self.universidade.upper()
        if self.curso:
            self.curso = self.curso.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Acompanhamento(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='acompanhamentos')
    ano = models.IntegerField()
    periodo = models.IntegerField()
    rendimento = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.aluno.nome} - {self.ano}/{self.periodo}"
    
