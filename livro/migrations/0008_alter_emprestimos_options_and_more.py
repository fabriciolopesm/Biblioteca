# Generated by Django 4.1.7 on 2023-03-04 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("livro", "0007_alter_emprestimos_nome_emprestado"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="emprestimos", options={"verbose_name": "Empréstimo"},
        ),
        migrations.AlterField(
            model_name="emprestimos",
            name="data_devolucao",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="emprestimos",
            name="data_emprestimo",
            field=models.DateField(blank=True, null=True),
        ),
    ]
