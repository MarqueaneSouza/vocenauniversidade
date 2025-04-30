from django.core.management.base import BaseCommand
import pandas as pd
from datetime import datetime
from alunos.models import Aluno

class Command(BaseCommand):
    help = 'Importa alunos da planilha para o banco de dados'

    def handle(self, *args, **options):
        # Caminho da planilha
        caminho_planilha = 'media/alunos.xlsx'  # ajuste esse caminho
        df = pd.read_excel(caminho_planilha, sheet_name='DADOS ESTUDANTES')

        for _, row in df.iterrows():
            try:
                # Tratamento das datas
                data_admissao = pd.to_datetime(row['DATA ADMISSÃO'], errors='coerce').date()
                previsao_format = pd.to_datetime(row['PREVISÃO FORMATURA'], errors='coerce').date()

                aluno, created = Aluno.objects.update_or_create(
                    cpf=row['CPF'],
                    defaults={
                        'nome': row['NOME'],
                        'telefone': str(row['TELEFONE']),
                        'email': row['E-MAIL'],
                        'universidade': row.get('UNIVERSIDADE', 'N/A'),
                        'curso': row['CURSO'],
                        'data_admissao': data_admissao,
                        'previsao_formatura': previsao_format,
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Aluno criado: {aluno.nome}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Aluno atualizado: {aluno.nome}"))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Erro com aluno {row.get('NOME', 'Desconhecido')}: {e}"))
