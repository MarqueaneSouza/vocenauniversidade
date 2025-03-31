from django.db import models

# Este código define cinco modelos Django que representam entidades do mundo real em um contexto acadêmico: 
# 1. Universidade, 2. Curso, 3. Aluno e 4. Rendimento

class Universidade(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    
    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    duracao_semestres = models.IntegerField()
    universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nome} - {self.universidade.nome}"

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_admissao = models.DateField()
    previsao_formatura = models.DateField()
    data_exclusao = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome

class Rendimento(models.Model):
    SEMESTRES = [
        ('1', '1º Semestre'),
        ('2', '2º Semestre')
    ]
    
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=1, choices=SEMESTRES)
    disciplinas_cursadas = models.IntegerField()
    disciplinas_aprovadas = models.IntegerField()
    media_geral = models.DecimalField(max_digits=4, decimal_places=2)
    observacoes = models.TextField(blank=True)
    
    class Meta:
        unique_together = ('aluno', 'ano', 'semestre')
    
    def __str__(self):
        return f"{self.aluno.nome} - {self.ano}/{self.semestre}"