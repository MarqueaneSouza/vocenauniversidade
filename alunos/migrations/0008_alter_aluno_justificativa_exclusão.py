# Generated by Django 5.2 on 2025-05-12 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0007_aluno_justificativa_exclusão_aluno_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='justificativa_exclusão',
            field=models.TextField(blank=True, null=True, verbose_name='Informe o motivo da exclusão'),
        ),
    ]
